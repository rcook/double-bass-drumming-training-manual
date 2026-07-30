# Development notes

Orientation for editing this repository. Not for students following the manual—students should start at [approach.md](approach.md).

## What this repo contains

- [approach.md](approach.md) and `chapter-NN.md`—the student-facing manual. Treat these as the primary product.
- [scripts/](scripts/)—Python tooling that turns a legally acquired copy of the source PDF into a structural index the manual can reference. See [scripts/README.md](scripts/README.md) for the low-level how-to.
- [data/](data/)—extractor output (a whole-book index and cleaned per-chapter text). Gitignored—regenerate locally.
- [source-material/](source-material/)—where the local PDF lives. Gitignored.
- [content-issues.md](content-issues.md)—running log of content discrepancies noticed while using the manual. Content only; tooling issues do not go here.

## Editing the manual

- The audience of `approach.md` and the chapter sheets is the student. Nothing developer-facing belongs there. Development notes go in this file, or in `scripts/README.md` if they are about the extractor specifically.
- The chapter sheets are meant to be concrete enough that a first-time student can act on them without additional context—set the metronome, set a timer, play, log. If a sheet leaves the student guessing at the mechanical loop, that is a bug; see the session runbook in [approach.md](approach.md).
- When a chapter sheet changes shape (e.g. adds a "first session" walkthrough), the same shape usually needs to propagate to the other 22 sheets. Do that as a follow-up rather than trying to hit all 23 in one edit—small blast radius, easy to revert.

## Style and linking conventions

Enforced across every markdown file in the repo (`approach.md`, `chapter-NN.md`, `README.md`, `content-issues.md`, this file):

- **"towards", not "toward".** UK/Commonwealth spelling. Applies uniformly.
- **Em-dashes (U+2014) are unspaced.** Write `word—word`, not `word — word`. This applies inside headings too. Inside fenced code blocks, leave text alone.
- **En-dashes (U+2013) are used only for numeric ranges** (`50–110 bpm`, `pp. 6–7`) and stay unspaced.
- **Cross-references to `approach.md` sections are markdown links with anchors**, not bare text. Write `[approach.md §4](approach.md#4-the-tempo-target-and-clean-pass-rule)`, not `` `approach.md` §4``. GitHub auto-generates anchors from headings by lowercasing, replacing spaces with hyphens, and stripping punctuation—so `## 4. The tempo-target and clean-pass rule` becomes `#4-the-tempo-target-and-clean-pass-rule`. If you renumber or rename a section, update every incoming link.
- **Cross-references to other chapter sheets** should also be markdown links: `[chapter-05.md](chapter-05.md)`, not bare `chapter-05.md`.
- **Section headers inside a document** use `## N. Title` for top-level sections (so anchors get the numeric prefix) and `### Subtitle` for sub-sections. Do not put full stops at the ends of headings.

## Things to do later

Parking lot for changes we know we want but are not doing yet. Delete an item when it lands.

- **Students who only own the original edition of R&L.** The manual currently targets the *Revised Edition*. Add guidance—or a variant sheet—for anyone working from the original edition: what maps 1:1, what is missing (the Rondinelli-authored Stage 6 chapters, at minimum), and how to adapt the stage progression accordingly.
- **Propagate the chapter-01 "Your first session" shape to Ch. 2–23** once the shape is validated on Ch. 1.
- **Explicit Core / Rotation processes on Ch. 2–23.** The clarification landed in `chapter-01.md`—every other chapter sheet needs the same treatment.

## Regenerating the data files

From the repo root, after placing the PDF under `source-material/`:

```
python3 -m venv .venv
source .venv/bin/activate
pip install pdfplumber
python scripts/extract_source_data.py
```

Full detail in [scripts/README.md](scripts/README.md), including reproducibility notes and what the JSON / text output contains.

## Filing content issues

Discrepancies between the manual and the source PDF, and editorial gaps noticed while using the manual, go in [content-issues.md](content-issues.md). The file's own header explains the entry format. Extractor bugs and tooling issues do not belong there—file those against the appropriate script or open an issue against the repo.

## Licence

The [LICENCE](LICENCE) file (Creative Commons Attribution-ShareAlike 4.0 International) covers the original content of this repository—the methodology, the working sheets and the extraction tooling. The source book's copyright is unaffected.
