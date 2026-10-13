# Website cleanup audit — October 13, 2026

## Publishing findings

- The latest three completed Pages runs on October 13 succeeded. The current site is not generally unable to publish.
- All three October 5 runs failed: [37364560402](https://github.com/JamesDean595/jamesdean595.github.io/actions/runs/37364560402), [37366403805](https://github.com/JamesDean595/jamesdean595.github.io/actions/runs/37366403805), and [37369794467](https://github.com/JamesDean595/jamesdean595.github.io/actions/runs/37369794467). The last run’s build job was cancelled and deployment skipped; the reporting job recorded the conclusion as `abandoned`. Its log download returned `BlobNotFound`; the underlying cause cannot be established from the available logs. These failures explain why those commits did not immediately publish.
- The live `Interactives/PracticeExams/ECONFIN335Exam1` returns HTTP 200 but `Content-Type: application/octet-stream`, not HTML. Added the same contents as `ECONFIN335Exam1.html` and linked that version. Retained the old file to avoid removing an existing address.
- The live `Interactives/Derivatives.html` and `Interactives/PracticeExams/Exam1_PracticeExam.html` return HTTP 200 with HTML content types.
- Filenames and paths are case-sensitive. Uploading an interactive does not automatically create a link to it on Teaching.

## Changes

- Move website source into `docs/`. Keep URL paths unchanged. This requires changing the Pages source folder when merging; see README.
- Archive only identifiable template examples and optional generators; retain the theme’s layouts, includes, Sass, JavaScript and fonts.
- Preserve all existing interactives, PDFs, and images, including unused personal photos and old research PDFs. Lack of a navigation link does not prove a file is unused: it may be linked from Canvas, an email, or an old paper. No personal content was deleted.
- Add an interactive directory linked from Teaching.
- Replace uneven inline photos with a responsive, uncropped gallery controlled by a YAML list.
- Standardize publications, chapters, and reviews using author–year citations. Use the current repository CV plus publisher records. Correct the agricultural article title from “Three” to “Six,” Economics Bulletin volume from 40 to 46, and the Lawson–Dean author order and title. Preserve the student co-author designation and supplementary links.
- Remove references to nonexistent theme icon files and use the existing favicon in the manifest.
- Correct the Empirical Economics citation to volume 70, Article 35, as listed by Springer.
- Point the CV embed to the same current PDF as the download link; preserve the older file too.

## Citation sources

- Current repository `files/James_Dean_CV.pdf` (moved to `docs/files/James_Dean_CV.pdf`).
- https://doi.org/10.1016/j.inteco.2026.100732
- https://www.accessecon.com/Pubs/EB/2026/Volume46/EB-26-V46-I1-P22.pdf
- https://doi.org/10.1002/soej.70020
- https://reunido.uniovi.es/index.php/EBL/article/view/15513

## Scope of archiving

See `archive/README.md` for the precise list. Some template examples were technically reachable through the generated sitemap even though they were not in the personal navigation; archiving intentionally stops publishing those examples. The real site pages and the terms page are retained. Archived content remains visible in this public repository.

- https://doi.org/10.1007/s00181-025-02868-0

## Validation

- Built both the original and proposed sites with Jekyll 3.10.0 and the GitHub Pages gem bundle in safe mode. A local-only configuration disabled optional GitHub metadata lookup because this environment cannot perform the plugin’s DNS check; site content, URLs, theme, plugins, and rendering were otherwise unchanged.
- Checked all 27 generated HTML files for broken local links and required page outputs: passed.
- Verified all 12 original interactives and all 20 PDFs are byte-for-byte unchanged at their original URL paths. All photo/image binaries are unchanged; only the broken icon manifest was corrected.
- Parsed all 13 interactive inline scripts with Node: no JavaScript syntax errors.
- Compared original and proposed output inventories: removed outputs are archived template examples/tools. The homepage HTML differs only by removal of nonexistent icon links, and main theme CSS is unchanged.
- Added a GitHub build/link-check workflow and pinned the local build dependencies in Gemfile.lock. The workflow checks the site but does not publish it.
