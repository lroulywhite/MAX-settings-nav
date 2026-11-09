# MAX | Explore Settings (explorer)

An interactive explorer for the **Settings** area of MAX (MomentusMAX). The product screen is the real captured Settings page, running live. Learners move around in one way: by pages.

- **Select any page in the left list**, and the page on the right changes.
- A **green check** appears next to every page you have viewed, in the list and in the guide.
- The **guide panel** shows the page's group, what it does, who can see it, and key points (collapsed until opened).
- **Next page / Previous** walk through all 21 pages in order. **All pages** returns to an index of every group and page, so you can jump anywhere without scrolling the list.
- The header keeps a running count ("5 of 21 pages viewed") with a progress bar, and a message appears when every page has been viewed.
- Arrow keys also move between pages.

## Quick start

Open `index.html` in a browser. It is one self-contained file with no server and no install (about 2.6 MB).

| File | Purpose |
|---|---|
| `index.html` | The built explorer. GitHub Pages serves this file. |
| `dist/settings-walkthrough.html` | The same file, for Genially or any embed. |
| `build.py` | Builds both files from `src/`. Run `python3 build.py` after any edit. |
| `src/outer.template.html` | The explorer (layout, guide, groups, checkmarks, navigation). Edit this file. |
| `src/stage.html` | The real Settings page: product shell, page list, and the HTML of all 21 pages. |
| `src/ex.json` | Page names, descriptions, key points, and role notes from the interaction file. |
| `src/MANIFEST.json` | Source and modification record for the product capture. |
| `tools/extract_stage.py` | Rebuilds `src/stage.html` and `src/ex.json` from the interaction file. |

Suggested repository name: `MAX-settings-nav`. For GitHub Pages, publish the repository root.

## How it works

- Clicks on the left list are handled by the explorer, which swaps in the saved HTML of the chosen page and adds the check. Every other click shows a short "Select a page in the Settings list on the left." message, and nothing in the product can be changed. Scrolling still works.
- The product fills the whole left side at its natural size, with no outer scrolling. The page list and each page keep their own scrolling, as in the real product. Selecting a page scrolls it into view in the list.
- The layout adapts to screen size: guide on the right on desktop, stacked on a phone, with a readable minimum size for the product and sideways scrolling if needed.
- Group names and one-line group descriptions are in `GROUPS` in `src/outer.template.html`. Each page number (0 to 20) matches its position in the list.
- Theme: the same mid-tone theme as the other walkthroughs, with no dark mode.

## Edit the copy

Page descriptions, key points, and role notes are in `src/ex.json` (from the interaction file). Group names and descriptions are in `GROUPS`. Keep copy short, with no contractions. Then run `python3 build.py`. Confirm role notes with Product when pages or roles change.

## UI fidelity

The product UI is locked. Do not edit `src/stage.html` by hand. If the Settings page changes, supply a new interaction file or capture and run `python3 tools/extract_stage.py`. The capture shows illustrative data (the venue "Riverview Center" and example email addresses). It is not a formal versioned snapshot.

## Known gaps and open items

- Search, filters, tabs, and buttons inside the pages do not work; only the left list does.
- Page descriptions and role notes come from the interaction file and still use the name "MomentusMAX". Confirm wording with Product.
- Mobile layout was checked in a headless browser, not on physical devices.

## License

Internal Momentus Technologies training content. Add the license or confidentiality notice required by company policy before making this repository public.
