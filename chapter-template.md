# Chapter-sheet template

Reference template for filling in R&L chapter working sheets. [Chapter 1](chapter-01.md) (Stage 1) and [Chapter 2](chapter-02.md) (Stage 2+) are the reference implementations that shaped this template; when they and this template disagree, they win—this template lags them.

## When to fill a chapter

Fill a chapter sheet only when the previous chapter is close to its unlock bpm in your own practice, or when there is a specific reason to do it now (e.g. the sheet author wants the next chapter reachable before a break). Sheets filled far ahead of real practice accrete errors that the first real session surfaces — see the resolved-issues history for concrete examples (Ch. 2 Core exercise misreads, first-session boredom-trap carve-outs, Role-cell omissions).

The order that has worked twice (Ch. 1, then Ch. 2):

1. Confirm the previous chapter's unlock is imminent, or the sheet is genuinely needed now.
2. **Transcribe every Core and Rotation exercise bar-by-bar against the source score**, and add each transcription to `exercises.json` (root of the private repo) before drafting Role cells. `exercises.json` is source-of-truth for chapter-sheet Role cells and per-exercise descriptions.
3. Draft the chapter sheet against the transcriptions.
4. Run the first real session on it, log any mismatches, patch, and file issues for anything that persists.

Do not skip step 2. Two chapters of prior experience say AI-assisted visual reads of R&L notation are unreliable for foot assignment, exercise character, rhythmic placement and density-per-bar.

## Which sections generalise unchanged, which adapt

The eight sections common to both Ch. 1 and Ch. 2 (present in every chapter sheet):

- **Title (H1) + metadata block.** Always: Stage, Book pages, Total exercises (with section-label counts), Section labels present, Session role.
- **How to use this sheet.** Prose introduction to the chapter's material. Chapter-specific.
- **Core (most sessions).** Table + "Why these N?" rationale paragraph. Table columns are `Ex.`, `Section`, `Role`, `Start`, optional `Unlock`, `Target`, optional `Increment`.
- **Rotation (some sessions).** Table + optional Cadence note. Same table columns as Core, minus `Unlock`.
- **Reference (discretionary).** Short prose paragraph listing what is not in Core / Rotation.
- **Practice notes.** Bulleted list of per-chapter tips.
- **Moving on to [next chapter or stage].** Gate criterion + choice of common-vs-overlap path when the next chapter opens.
- **Log entry format.** Short example matching [Approach §8](approach.md#8-tracking), 5-field form: `chapter.exercise  bpm  duration  verdict  note`.

Stage-specific additional sections:

- **Stage 1 ([Chapter 1](chapter-01.md) only).** "Your first session" + "Your third session" walkthroughs. Stage 1 uses **hold-only** single-block sessions—the student holds the current bpm for the whole block, no within-session probing.
- **Stage 2+ ([Chapter 2](chapter-02.md) onwards).** "Your first [Ch. N] session" walkthrough + "Rotating through the Core" section. Stage 2+ uses the **three-block session template** ([Approach §6](approach.md#6-the-session-template))—warm-up (Ch. 1), focus, application, cool-down—and the focus and application blocks run [Approach §7](approach.md#7-running-a-session)'s **hold-and-probe** loop within the block.

When-applicable additions:

- **Kit-setup callout** in "How to use this sheet" when a chapter introduces a new kit element (hi-hat for Ch. 2 Beats; other elements later). Cross-reference [Approach §3.3](approach.md#33-kit-setup).
- **Increment-differs paragraph** in "How to use this sheet" when the chapter has both Warm-Ups (feet-only, +4 bpm) and Beats / Fills (hands + feet, +2 bpm). See [Approach §4](approach.md#4-the-tempo-target-and-clean-pass-rule).
- **Increment column** in the Core / Rotation tables for the same reason.

## Per-chapter decisions

When instantiating for a new chapter, decide each of these before drafting:

| Decision | Source |
| --- | --- |
| Stage | [Approach §5](approach.md#5-the-chapter-progression) chapter progression |
| Book pages | R&L table of contents |
| Total exercises + section-label breakdown | R&L source |
| Section labels present | R&L source |
| Session role wording | Stage 1 = "the whole session"; Stage 2+ = "focus and application blocks" |
| Starting / target bpm | [Approach §4](approach.md#4-the-tempo-target-and-clean-pass-rule) material-type table |
| Increment (+4 / +2) | [Approach §4](approach.md#4-the-tempo-target-and-clean-pass-rule)—feet-only → +4, hands + feet → +2 |
| Unlock bpm (only if this chapter gates a stage transition) | [Approach §5](approach.md#5-the-chapter-progression) staging table |
| Core exercise selection | Chapter-specific pedagogical judgment against the transcribed grids |
| Rotation / Reference selection | Same |
| "Moving on to…" gate criterion | [Approach §5](approach.md#5-the-chapter-progression) staging table |
| Log-line prefix | `<N>.` for standard numbering; `<N>.<section-id>N` when a chapter's section labels restart numbering (Ch. 14, 17, 19, 20, 21 currently) |

## Anti-patterns from prior chapter fills

Lessons the manual has already paid for, worth avoiding on any new fill:

- **Do not draft Role cells from a visual read of the score without transcribing bar-by-bar first.** The `a828030` fill of [Chapter 2](chapter-02.md) drafted five Core Role cells without transcription; every one of them turned out to be wrong or misleading on the first real session (foot lead flipped, placement axis wrong, "sustained" density mis-called). The `exercises.json` transcription is the load-bearing input; draft after it, not before.
- **Do not apply Stage 1's "hold, do not probe" first-ever-session rule to Stage 2+ chapters.** The Stage 1 rule assumes a true beginner with no coordination floor. Any Stage 2+ chapter unlocks only after the student cleared 90 bpm on the Ch. 1 Core—so 50 bpm on the new chapter's first-ever session sits well below the student's coordination floor by construction. A student holding 50 bpm for the full 15-minute focus block will quit out of boredom. Stage 2+ walkthroughs must reference [Approach §7](approach.md#7-running-a-session)'s hold-and-probe loop from minute one.
- **List every kick per bar in a Beat's Role cell, not just the distinguishing feature.** "Doubled 16ths on 2& + 2a and 4& + 4a" tells the student only two of the six kicks in the actual pattern; the missing single kicks on 1& and 3& are also part of the exercise. Convention: identifying feature + anchor kicks + strong-foot / weak-foot lead.
- **Cross-check the [Approach §5](approach.md#5-the-chapter-progression) staging table when resolving a description-of-exercise issue.** The staging table's Ch. X → Y row often carries the same phrasing that lives in the chapter sheet; when one changes, grep the other. Same for any wording that lives in more than one place (`exercises.json` notes, per-exercise descriptions).

## Instantiation checklist

Before landing a new chapter sheet:

- [ ] Every Core and Rotation exercise has a verified transcription in `exercises.json`.
- [ ] Role cells cite the transcription's placement / lead-foot / density-per-bar, not a visual read.
- [ ] Starting / target bpm match [Approach §4](approach.md#4-the-tempo-target-and-clean-pass-rule)'s material-type table for this chapter's material.
- [ ] Increment column present if the chapter mixes Warm-Ups and Beats / Fills.
- [ ] Unlock bpm matches [Approach §5](approach.md#5-the-chapter-progression)'s staging table (blank if this chapter does not gate a stage transition).
- [ ] Kit-setup callout present if a new kit element enters this chapter.
- [ ] "Your first [Ch. N] session" references [Approach §7](approach.md#7-running-a-session)'s hold-and-probe loop (Stage 2+); does not restate the Stage 1 hold-only rule.
- [ ] Working-state update wording defers to [Approach §8](approach.md#8-tracking) rather than restating it (§8 is the canonical spec for `current bpm` and `last pass bpm` updates).
- [ ] "Moving on to…" section names the gate exercise and unlock bpm from the staging table and describes the common vs. overlap path.
- [ ] Log-entry example uses the 5-field format `<N>.<exercise>  <bpm> bpm  <duration> min  <verdict>  <note>`.
