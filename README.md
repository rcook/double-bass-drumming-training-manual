# Double Bass Drumming Training Manual

> **Following the course?** Start with [approach.md](approach.md).

## What this is

A training manual built around Bobby Rondinelli and Michael Lauren's *The Encyclopedia of Double Bass Drumming (Revised Edition)*. The source book is a reference of exercises; this manual wraps a method around it, focused on strength and accuracy for a self-directed beginner.

## Project status

The methodology in [approach.md](approach.md) and the chapter-01 working sheet ([chapter-01.md](chapter-01.md)) are the current reference implementation. Chapters 2–23 exist as skeletons—they have the metadata block, a brief "How to use this sheet" section, and Core / Rotation / Reference tables—but they have not yet been rewritten to the shape chapter-01 now has (first-session walkthrough, worked advancement example, explicit two-consecutive-passes loop, per-exercise rationale). The methodology is being validated on chapter-01 first; once the shape is stable, it propagates to the other 22 sheets. Each skeleton chapter sheet carries a banner at the top marking it as such. See [DEVELOPMENT.md](DEVELOPMENT.md) "Things to do later" for the outstanding items.

Feedback on the method or on chapter-01 specifically is welcome via [GitHub Issues](https://github.com/rcook/double-bass-drumming-training-manual/issues)—see the issue templates for the three feedback categories.

## Repository structure

- [approach.md](approach.md)—the training method. Start here.
- [content-issues.md](content-issues.md)—running log of content discrepancies noticed while using the manual. File an entry here if the manual disagrees with the source book.
- [scripts/](scripts/)—extraction tooling. See [scripts/README.md](scripts/README.md) for how to reproduce the data files from your own copy of the book.
- [data/](data/)—extracted structural index of the source book (chapter titles, page ranges, section labels) plus cleaned per-chapter text. Gitignored; regenerate locally with the script above.
- [source-material/](source-material/)—where you place your legally acquired copy of the PDF. Gitignored.
- [DEVELOPMENT.md](DEVELOPMENT.md)—orientation for anyone editing the manual (extractor pipeline, sheet conventions, issue tracker). Not needed if you are just following the course.
- [LICENCE](LICENCE)—Creative Commons Attribution-ShareAlike 4.0 International

Per-chapter working sheets live at the repo root as [chapter-01.md](chapter-01.md) through [chapter-23.md](chapter-23.md), one file per chapter of the source book. Your own practice log is not a repo file—see [approach.md](approach.md) §8.

## How to use

Start with [approach.md](approach.md)—it establishes the method (the tempo-target and clean-pass rule, the stage-based chapter progression, the session template and the tracking format). Per-chapter working sheets and session logs slot in on top of that foundation as they are produced. This README deliberately does not restate the method; it points at [approach.md](approach.md) instead.

## Source book

*The Encyclopedia of Double Bass Drumming (Revised Edition)* by Bobby Rondinelli and Michael Lauren is © 2000, 2022 Modern Drummer Media LLC. The PDF is not distributed via this repository—[source-material/](source-material/) is git-ignored. This manual assumes you have your own legally acquired copy of the book. Nothing here reproduces the source material; the manual adds original methodology around it.

The manual is written against the Revised Edition, but is fully compatible with the Original Edition for Stages 1–5 (R&L Ch. 1–14). Stage 6 (R&L Ch. 15–23) is Revised-only. See [approach.md §3.2](approach.md#32-original-edition-compatibility) for the enumerated differences.

## Licence

The [LICENCE](LICENCE) file contains the Creative Commons Attribution-ShareAlike 4.0 International Public License. It covers only the original content of this repository—the methodology, the working sheets and the extraction tooling. The source book's copyright is unaffected.
