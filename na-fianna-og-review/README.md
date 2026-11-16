# SPG U20 v Na Fianna Óg — Player Review
Match: 13 November 2026. SPG 3–11, Na Fianna Óg 1–9.

## Status
All six original chart PNGs have been recovered from the existing Site and added to this branch. The new review remains separate from the older pages. GitHub Pages currently builds `main` from the repository root; its latest build and deployment succeeded. Browser verification and publication of this draft remain pending.

Existing published Site: https://spg-u20-player-review.user36537288929.chatgpt.site/

## Included
- 14 clips in the agreed order: **Turnovers → Defensive Awareness → Positive Play**.
- Sean Tuohy’s clip first, **04:17–04:21**.
- Clip 27 starts **52:40**. Clip 21 starts **34:18**.
- Large presentation text, **Main Points** heading, one YouTube player and Previous/Next controls.
- Existing SPG crest reused from the older GitHub review.
- Six chart positions reordered to match the main points. The red ellipse remains over the **12–6 breaking-ball figures** in the Kickouts Overview.
- No existing review page is changed.

## Clip order
Turnovers: 1, 3, 19, 20, 34.
Defensive Awareness: 4, 5, 26, 27, 43.
Positive Play: 18, 21, 36, 42.

Total footage: 5 minutes 15 seconds.

## Original graphics to import
Keep the PNGs from the existing Site, or export these exact pages from **SPG v Na Fianna Og Stats Overview_261116_082826.pdf** (Library ID: libfile_5a7289f7114c819186cc11b89aa25e9f):

| Main point | Order | File beneath this folder | PDF page |
| --- | --- | --- | --- |
| Accuracy & our kickouts | 1 | graphics/total-kickouts.png | 20 |
| Accuracy & our kickouts | 2 | graphics/kickouts-overview.png | 18 |
| Careless turnovers | 3 | graphics/balls-lost.png | 26 |
| Careless turnovers | 4 | graphics/opposition-funnel.png | 8 |
| Second-half momentum | 5 | graphics/opposition-kickouts.png | 22 |
| Second-half momentum | 6 | graphics/shots-timeline.png | 13 |

`export_graphics.py` renders the original PDF pages at 2400 × 1350 pixels using PyMuPDF:
```sh
python3 export_graphics.py "/path/to/SPG v Na Fianna Og Stats Overview_261116_082826.pdf"
```
The ellipse is a separate SVG overlay in the HTML. Do not paint over or alter the original chart data.

The Shots Timeline ends at **23–24**, while Liam’s written half-by-half figures total **22–23**. The page labels this source difference without changing either.

## Finish and publish
1. Completed: all six original PNGs are present in `graphics/` on this branch.
2. Open the HTML and verify the enlarged text, all 14 clips, six original charts, the ellipse and the full-size chart dialog.
3. Merge this branch into `main` using the existing GitHub Pages root deployment.

The new review will be in the `na-fianna-og-review/` subfolder, with older reviews retained. This repository is public; robots/noindex settings discourage indexing but do not provide access control.
