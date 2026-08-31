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

- **Unlock-bpm scheme for every stage transition.** Only Stage 1→2 is decided (R&L Ch. 1 Ex. 1/10/11 at 90 bpm—see [chapter-01.md](chapter-01.md) "Moving on to Stage 2" and [approach.md §5](approach.md#5-the-chapter-progression), Stage 2). Every other stage transition (Stage 2→3, Stage 3→4, and the within-Stage-2 Ch. 2→3→4→5 sequence) still needs its gating exercises and their unlock bpm chosen. `§5`-of-`approach.md` edit. Do this before the chapter-sheet template below (the template's "Moving on to…" guidance has to reference the unlock scheme) and before propagating the chapter-01 shape (each chapter sheet's "Moving on to…" section needs the number). Wait until there is real session data on how Ex. 10 (16ths between the feet) tracks against Ex. 1 in the Ch. 1 Core—if Ex. 10 lags Ex. 1 as `chapter-01.md` predicts, that is confirming evidence for the "gate on the hardest of the group" shape and should inform the other gates.
- **Chapter-sheet template.** `chapter-01.md` is the only fully-written sheet. Before propagating its shape to Ch. 2–23, write a template document—candidate location: a new `chapter-template.md`, or a new section here—covering which sections generalise, how a Stage 2+ chapter differs from a Stage 1 chapter (in particular, whether the "Your first session" and "Your third session" walkthroughs still fit, or whether Stage 2+ chapters just point at [approach.md §7](approach.md#7-running-a-session)), and what per-chapter decisions the author has to make (starting bpm, unlock bpm if any, target bpm, Core vs. Rotation vs. Reference assignment, "Moving on to…" criterion). Depends on the unlock-bpm scheme above.
- **Propagate the chapter-01 "Your first session" shape to Ch. 2–23** once the shape is validated on Ch. 1. Depends on the two items above.
- **Explicit Core / Rotation processes on Ch. 2–23.** The clarification landed in `chapter-01.md`—every other chapter sheet needs the same treatment. Rolls into the propagation item above.

## Filing issues

Report content discrepancies, editorial gaps, tooling bugs, or anything else at the GitHub issue tracker: [https://github.com/rcook/double-bass-drumming-training-manual/issues](https://github.com/rcook/double-bass-drumming-training-manual/issues). That is the officially sanctioned channel for all defects and feature requests, whether they concern the manual content, the chapter sheets, or any tooling shipped alongside the manual.

When filing, point at the specific location (file + section, or file + table row), state what you observed and why it seems wrong, and suggest a next step if you have one. "Investigate" is a fine next step.

## Licence

The [LICENCE](LICENCE) file (Creative Commons Attribution-ShareAlike 4.0 International) covers the original content of this repository—the methodology and the working sheets. The source book's copyright is unaffected.
