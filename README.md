# MAX | Explore Settings (explorer)

An interactive explorer for the **Settings** area of MAX (MomentusMAX). The product screen is the real captured Settings page, running live, and it fills the whole left side as large as the screen allows. Learners always know what to do next.

- **Callouts sit on the product, next to what they describe.** A pointer ("Start here: click Users & Access" / "Next: click Calendar Settings") is attached to the exact item to click in the page list, with a pulsing outline. After a page opens, a **What this page does** callout (blue) and a **Who can see it** callout (navy) are attached to the page's title with a dashed leader line. A **Hide these notes** button hides them, and the guide can show them again.
- **Only the written directions use the Momentus orange** (`#FFEDEA` box with a `#fe5545` border): the "Do this next" banner, and the message shown when a learner clicks something else. The "Start here / Next: click ..." pointer on the product is a blue button. Every other indicator stays indigo/blue: the ring on the list item, the numbered start steps, the checkmarks, the highlighted labels, and the page callouts.
- Select any page in the list, and the page on the right changes. A **green check** appears next to every page you have viewed, in the list and in the guide.
- The start screen is kept to one sentence and the orange "Start here" direction. Page names and descriptions only appear after the learner clicks a page.
- On small screens (when the product area is too small to hold the callouts), the **What this page does** and **Who can see it** notes move into the guide. The pointer on the list item always stays on the product.
- **Next page** (always the next page you have not viewed) and **Previous** are in a button bar at the bottom of the guide.
- The header keeps a running count ("5 of 21 pages viewed") with a progress bar. When every page has been viewed, the banner turns green and **Restart** appears.
- If a learner clicks anything other than the list, a large message tells them which page to click.
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
- The product fills the whole left side with no outer scrolling, at about its natural size or larger. It is laid out narrower (960 to 1300 layout pixels wide, like a smaller laptop window) and scaled up to fit, about 1.6 times its natural size on a large screen. Wide pages such as Import Records and Usage scroll sideways inside the page, as in the real product. The page list and each page keep their own scrolling. Selecting a page scrolls it into view in the list.
- The guide text is deliberately small and steady (about 16 px) so the product is the hero. The on-page callouts and the pointer are sized to match the product's own text, so they stay easy to read at any size.
- The layout adapts to screen size: guide on the right on desktop and laptop, stacked below the product on tablets and phones, with a readable minimum size and sideways scrolling if needed.
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
