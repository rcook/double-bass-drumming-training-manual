# Development notes

Orientation for editing this repository. Not for students following the manual—students should start at [approach.md](approach.md).

## What this repo contains

- [approach.md](approach.md) and `chapter-NN.md`—the student-facing manual. Treat these as the primary product.

## Editing the manual

- The audience of `approach.md` and the chapter sheets is the student. Nothing developer-facing belongs there. Development notes go in this file.
- The chapter sheets are meant to be concrete enough that a first-time student can act on them without additional context—set the metronome, set a timer, play, log. If a sheet leaves the student guessing at the mechanical loop, that is a bug; see the session runbook in [approach.md](approach.md).
- When a chapter sheet changes shape (e.g. adds a "first session" walkthrough), the same shape usually needs to propagate to the other 22 sheets. Do that as a follow-up rather than trying to hit all 23 in one edit—small blast radius, easy to revert.

## Style and linking conventions

Enforced across every markdown file in the repo (`approach.md`, `chapter-NN.md`, `README.md`, this file):

- **"towards", not "toward".** UK/Commonwealth spelling. Applies uniformly.
- **Em-dashes (U+2014) are unspaced.** Write `word—word`, not `word — word`. This applies inside headings too. Inside fenced code blocks, leave text alone.
- **En-dashes (U+2013) are used only for numeric ranges** (`50–110 bpm`, `pp. 6–7`) and stay unspaced.
- **Cross-references to `approach.md` sections are markdown links with anchors**, not bare text. Write `[approach.md §4](approach.md#4-the-tempo-target-and-clean-pass-rule)`, not `` `approach.md` §4``. GitHub auto-generates anchors from headings by lowercasing, replacing spaces with hyphens, and stripping punctuation—so `## 4. The tempo-target and clean-pass rule` becomes `#4-the-tempo-target-and-clean-pass-rule`. If you renumber or rename a section, update every incoming link.
- **Cross-references to other chapter sheets** should also be markdown links: `[chapter-05.md](chapter-05.md)`, not bare `chapter-05.md`.
- **Section headers inside a document** use `## N. Title` for top-level sections (so anchors get the numeric prefix) and `### Subtitle` for sub-sections. Do not put full stops at the ends of headings.

## Commit-message conventions

Commit messages in this repository (the public `_public` submodule) must not reference private-repo issue-tracker identifiers—**do not cite `TODOnnn`, `CI-nnn` or `ISS-nnn` in commit subjects or bodies.** Those IDs live in the private repo's `ISSUES.md` and carry no meaning for external readers of the public manual.

Describe the change on its own terms: what content changed, what the rationale was, and the observable effect on the manual. If a change was driven by a private-repo issue, put the substance of the issue in the commit body rather than the ID.

References to the public GitHub issue tracker at `https://github.com/rcook/double-bass-drumming-training-manual/issues` are fine—those numeric IDs (e.g. `#42`) are meaningful to external readers.

Existing commit messages that reference `TODOnnn` / `CI-nnn` / `ISS-nnn` remain as historical artefacts and should not be rewritten.

## Things to do later

Parking lot for changes we know we want but are not doing yet. Delete an item when it lands.

- **Propagate the chapter-sheet shape to Ch. 3–23.** [chapter-01.md](chapter-01.md) and [chapter-02.md](chapter-02.md) are the two fully-written sheets; the shape they share is documented in [chapter-template.md](chapter-template.md). Ch. 3–23 are still skeletons carrying only the metadata block and Core / Rotation / Reference tables. Fill each chapter one at a time when the previous chapter is close to its unlock bpm in real practice—see the "When to fill a chapter" note at the top of the template. Each fill is a self-contained piece of work with its own transcription pass, "Your first session" walkthrough, "Why these N?" rationale, and "Moving on to…" gate criterion.
- **Unlock-bpm scheme for later stage transitions.** [approach.md §5](approach.md#5-the-chapter-progression)'s staging table currently commits numbers for Stages 1→2, 2→3, 3→4, 4→5 and the Stage 2→3 between-stage transition. Stages 3-internal (Ch. 6→7), 4→5, 5→6 and everything at Stage 6 remain deferred until those chapter sheets get their fill. Each pending row wants real session data from the preceding chapter before its unlock bpm is chosen.

## Filing issues

Report content discrepancies, editorial gaps, tooling bugs, or anything else at the GitHub issue tracker: [https://github.com/rcook/double-bass-drumming-training-manual/issues](https://github.com/rcook/double-bass-drumming-training-manual/issues). That is the officially sanctioned channel for all defects and feature requests, whether they concern the manual content, the chapter sheets, or any tooling shipped alongside the manual.

When filing, point at the specific location (file + section, or file + table row), state what you observed and why it seems wrong, and suggest a next step if you have one. "Investigate" is a fine next step.

## Licence

The [LICENCE](LICENCE) file (Creative Commons Attribution-ShareAlike 4.0 International) covers the original content of this repository—the methodology and the working sheets. The source book's copyright is unaffected.
