"""Boomerang - Simple URL shortening/redirecting

Boomerang allows users to create and manage custom short links.
Hosted via Github Pages, generated via Python and Github Actions.
"""
__author__ = "Anitej Biradar (@anitejb)"
__license__ = "MIT"

import os

def get_link_files():
    """Return a list of all markdown files in the current directory."""
    link_file_names = []
    _, _, files = next(os.walk("."))
    for f in files:
        if f[-3:] == ".md" and f != "README.md":
            link_file_names.append(f[:-3])
    return link_file_names

def create_index_files(link_file_names):
    """Return a list of index.html strings for each short link."""
    with open("./template.html", "r") as f:
        template = f.read()

    index_files = []
    for linkf in link_file_names:
        with open(f"./{linkf}.md", "r") as f:
            index_files.append(template.format(url=f.readline().strip()))

    return index_files

def build(link_file_names, index_files):
    """Create a build directory with index.html files for short links."""
    os.mkdir("./build")
    for linkf, index in zip(link_file_names, index_files):
        os.mkdir(f"./build/{linkf}")
        with open(f"./build/{linkf}/index.html", "w+") as f:
            f.write(index)

if __name__ == "__main__":
    link_file_names = get_link_files()
    index_files = create_index_files(link_file_names)
    build(link_file_names, index_files)
