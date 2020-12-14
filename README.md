# Boomerang

## Table of Contents
- [Overview](#overview)
- ~~Requirements~~
- [Usage](#usage)
    - [Initial Setup](#initial-setup)
    - [Creating Short Links](#creating-short-links)
    - [Editing Short Links](#editing-short-links)
    - [Removing Short Links](#removing-short-links)
- [Helpful Tips](#helpful-tips)
- [License](#license)
- [Disclaimer](#disclaimer)

## Overview
Boomerang is a simple URL shortening/redirecting service with **zero** requirements, powered entirely by Github. With **just three clicks**, create a new short link that is readable, easily accessible, and forever customizable.

Built with [Python](https://www.python.org/), [Github Actions](https://github.com/features/actions), [Github Pages](https://pages.github.com/), and <3.

## Usage

### Initial Setup
1. Generate the repository.
    - Create your own version of this repository by clicking the [Use this template](https://github.com/anitejb/boomerang/generate) button.
    - Follow steps [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) if you need more help.
    - You can name the repository whatever you like. If you aren't using a custom domain, I would recommend naming it `b` to keep things short.
    - It can be either public or private. Note that private repositories will still create links that are publicly accessible.
    - Be sure to select the "Include all branches" option.

2. Enable Github Pages
    - This should be enabled by default, but it never hurts to double check :)
    - Go to Settings.
    - Under Github Pages, select the `gh-pages` branch and hit "Save".

3. Add your custom domain.
    - Follow the steps [here](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain).

### Creating Short Links
To create a new short link, follow the very simple steps below.

From the `main` branch,

1. Click "Add file" (this will open a dropdown menu)
2. Click "Create new file"
    - As the file name, type the name of the short link path that you want, followed by `.md`.
        - For example, if I want my short link to be `<example_domain>/covid`, my file name would be `covid.md`.
    - Inside the file, just paste the URL that you want your short link to redirect to.
        - Continuing the previous example, inside the file I would just type in my destination URL, `https://en.wikipedia.org/wiki/COVID-19_pandemic`.
3. Click "Commit new file"

Voila! Boomerang deploys in the background, and in seconds, your short link will be accessible from `https://<your_domain>/<short_link>`.

Your repository should come pre-built with one short link at `https://<your_domain>/covid`, redirecting to the Wikipedia page about the [COVID-19 Pandemic](https://en.wikipedia.org/wiki/COVID-19_pandemic). If desired, this can easily be [deleted](#removing-short-links).

Note: If you did not set up a custom domain, it will be accessible from `https://<your_github_handle>.github.io/b/<short_link>`. Yes, I know, this URL is quite long, and kind of defeats the purpose of shortening in the first place. However, Boomerang is still useful if you want to transform long URLs into readable links.

### Editing Short Links
Made a mistake, or just want to change a link? Follow these super simple steps below (also just 3 clicks!).

From the `main` branch,

1. Click the `<short_link>.md` file that you created.
2. Click the pencil icon that says "Edit this file" when you hover over it.
    - Edit either the short link (file name) or the destination URL (file contents). If you change the file name, make sure to keep the `.md` extension.
3. Click "Commit changes"

Changes should take no longer than the time it would have taken to deploy a new link. Watch out for browser caches (more about that [below](#helpful-tips)).

### Removing Short Links
Need to take a link down? Follow these super simple steps below (also just 3 clicks!).

From the `main` branch,

1. Click the `<short_link>.md` file that you created.
2. Click the trash bin icon that says "Delete this file" when you hover over it.
3. Click "Commit changes"

Just as fast as it went up, the short link will be taken down.

## Helpful Tips
So far, the only time Boomerang should break if you try to use invalid URLs. So don't do that.

Github Pages is finnicky. There will be times when builds fail, or a short link just doesn't work. While this is rare, there is a simple fix, which is to edit the short link file, and add an extra space or newline at the end of the long URL. Commiting that change will trigger a rebuild, which should fix the issues after a few minutes. In addition, these issues are isolated - links that already work should never be broken by trying to create new links.

Keep in mind that browsers cache URLs, so the latest version might not be what your browser is currently displaying.

Found something else? [Let me know!](https://github.com/anitejb/boomerang/issues)

## License
Copyright (c) 2020 Anitej Biradar. Released under the MIT License. See
[LICENSE](LICENSE) for details.

Questions? Reach out to [boomerang@anitejb.dev](mailto:boomerang@anitejb.dev), and I'll get right back to you!

## Disclaimer
Boomerang is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Github, or any of its subsidiaries or its affiliates.
