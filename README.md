# James Dean’s website

Website: https://jamesdean595.github.io

| Location | Purpose |
| --- | --- |
| `docs/` | All website source, pages, photos, PDFs, theme files, and interactives |
| `archive/` | Retained AcademicPages examples and optional tools; not published |
| `scripts/` | Website validation tools |
| `.github/workflows/` | Automatic build checks; does not publish |

GitHub is your account; this repository is one project within it. You can create separate repositories for Stata code, Python projects, and papers without changing this website. You can also keep code outside `docs/` here; it will not be published by Pages once Pages is set to `master /docs`. This repository is public, so those files are still visible on GitHub.

## One-time publishing setup for this cleanup

**This change is staged on a branch. Do not merge it without also changing the Pages folder.**

1. Confirm the cleanup build and link checks pass and review the changes.
2. Merge the cleanup pull request into `master`.
3. Immediately open **Settings → Pages → Build and deployment**. Keep **Deploy from a branch**, choose **master** and **/docs**, then Save.
4. Under **Actions**, wait for **pages build and deployment** to finish successfully. Check the homepage, Research, Personal, CV, Teaching, and a practice exam.

The source folder is a repository setting, not something Markdown or this pull request can change. Until the folder is changed, Pages will build from the wrong location. Coordinate steps 2–3; do not treat merging alone as completion.

Website URLs remain the same: for example, `docs/Interactives/Derivatives.html` is published at `/Interactives/Derivatives.html`, **not** `/docs/Interactives/Derivatives.html`.

## Everyday editing

- **Page text:** edit the Markdown files in `docs/_pages/`.
- **Publications:** edit `docs/_pages/research.md`. Use `Author(s). (Year). “Title.” Journal, volume(issue), pages.` Keep journal names italicized and the title linked to its DOI or publisher. Omit unavailable issue/page details rather than guessing.
- **CV:** replace `docs/files/James_Dean_CV.pdf`. The embedded and downloadable CV both use this file. Older PDF URLs remain available.
- **Photos:** upload to `docs/images/personal/`, then add an entry to `docs/_data/personal_photos.yml`. Reorder entries to reorder the gallery. The gallery uses equal-sized frames, shows the entire photo without cropping, and links to the full-size image. No JavaScript is required.

```yaml
- file: "my-new-photo.jpg"
  alt: "A short description of what the photo shows"
  caption: "Optional caption"
```

- **Standalone interactives:** upload a complete HTML file to `docs/Interactives/` (or a subfolder). **Include the `.html` extension.** Keep the original capitalization in links. Add a link to `docs/_pages/interactives.md` if you want it listed.
- **New Markdown page:** add a file in `docs/_pages/` with front matter like this, then link to its permalink from an existing page or `docs/_data/navigation.yml`:

```markdown
---
title: "My New Page"
permalink: /my-new-page/
author_profile: true
---

Page text goes here.
```

A new file does not automatically add a navigation link. Changes must reach `master` and complete a successful Pages deployment before they appear online.

## If an update does not appear

1. Confirm the file is under `docs/` on `master`, and that Pages is set to `master /docs`.
2. Check **Actions → pages build and deployment**. A saved GitHub file and a successful website deployment are separate steps. Open a failed run to read its error before retrying.
3. Check the exact URL, capitalization, and file extension. `/Interactives/` and `/interactives/` are different paths.
4. After a successful deployment, allow for caching and refresh the page. For an HTML interactive, the URL should end in `.html` or point to a directory containing `index.html`.

## Local checks

With Ruby and Bundler installed:

```sh
cd docs
bundle install
bundle exec jekyll build --safe --destination ../_site
cd ..
python3 scripts/check_site.py _site
```

## Rollback

Before migration, the original site is commit `792d2e6c6366a07834b82e270ea40a10429f76d1`. To roll back after merging, revert the cleanup merge on `master` (do not erase history), then restore **Settings → Pages → master → /(root)**. Wait for deployment and verify the homepage. Archived examples can also be restored individually from `archive/template/`.

See [the audit](WEBSITE_AUDIT.md) for findings and preservation decisions.
