# Double Bass Drumming Training Manual

## What this is

A training manual built around Bobby Rondinelli and Michael Lauren's *The Encyclopedia of Double Bass Drumming (Revised Edition)*. The source book is a reference of exercises; this manual wraps a method around it, focused on strength and accuracy for a self-directed beginner.

## Repository structure

- `approach.md` — the training method. Start here.
- `scripts/` — extraction tooling. See `scripts/README.md` for how to reproduce the data files from your own copy of the book.
- `data/` — extracted structural index of the source book (chapter titles, page ranges, section labels) plus cleaned per-chapter text. Gitignored; regenerate locally with the script above.
- `source-material/` — where you place your legally acquired copy of the PDF. Gitignored.
- `LICENCE` — Creative Commons Attribution-ShareAlike 4.0 International

Per-chapter working sheets live at the repo root as `chapter-01.md` through `chapter-23.md`, one file per chapter of the source book. Your own practice log is not a repo file — see `approach.md` §7.

## How to use

Start with `approach.md` — it establishes the method (the tempo-target and clean-pass rule, the stage-based chapter progression, the session template and the tracking format). Per-chapter working sheets and session logs slot in on top of that foundation as they are produced. This README deliberately does not restate the method; it points at `approach.md` instead.

## Source book

*The Encyclopedia of Double Bass Drumming (Revised Edition)* by Bobby Rondinelli and Michael Lauren is © 2000, 2022 Modern Drummer Media LLC. The PDF is not distributed via this repository — `source-material/` is git-ignored. This manual assumes you have your own legally acquired copy of the book. Nothing here reproduces the source material; the manual adds original methodology around it.

## Licence

The `LICENCE` file contains the Creative Commons Attribution-ShareAlike 4.0 International Public License. It covers only the original content of this repository — the methodology, the working sheets and the extraction tooling. The source book's copyright is unaffected.
