# Content issues

Log of discrepancies between this manual and the source book, plus editorial gaps noticed while actually using the manual. Newest entries at the top. Close entries in place with a short resolution note; do not delete resolved entries.

Scope is **content only**—extractor bugs, tooling issues and repo mechanics go elsewhere (see [DEVELOPMENT.md](DEVELOPMENT.md)).

## How to file an entry

- Give it an ID `CI-NNN`, one higher than the highest existing ID (open or resolved).
- Record the date filed in ISO 8601.
- Point at the specific location in the manual (file + section, or file + table row).
- State what you observed and why it seems wrong.
- Suggest a next step. It is fine if the next step is "investigate"—you do not need to know the fix to file the entry.

When resolved, move the entry to the **Resolved** section and add a one-line resolution note with the date and what changed.

## Open

### CI-005—Chapter-sheet template for propagating Ch. 1 shape to Stage 2+ chapters

- Filed: 2026-08-20
- Location: template candidate location [DEVELOPMENT.md](DEVELOPMENT.md) or a new `chapter-template.md`. Downstream target: `chapter-02.md` through `chapter-23.md`.
- Observed: [chapter-01.md](chapter-01.md) is the reference implementation for a working chapter sheet, now validated through ~3 weeks of real Core-block practice. Every other chapter file has only the "Skeleton sheet" banner. Propagation was deliberately shelved on 2026-08-03 pending real-session validation; that validation has now happened.
- Concern: filling in chapter-02.md in ~1–2 weeks (when Stage 2 unlocks) will require a template. Doing that as a one-off risks 22 more chapters copy-pasting bugs from Ch. 2. Better to design the template once and apply consistently.
- Next step: draft the template covering (a) which Ch. 1 sections generalise unchanged, (b) how sections adapt for a Stage 2+ chapter — different session role (Ch. 1 is the whole session before Stage 2 unlocks; Ch. 2+ occupies focus and application blocks per [approach.md §6](approach.md#6-the-session-template)), (c) which per-chapter decisions must be made when instantiating: unlock bpm (see CI-006), target bpm from [approach.md §4](approach.md#4-the-tempo-target-and-clean-pass-rule) material-type table, "Moving on to…" criterion, adaptations of "Your first session" for a chapter that is not first. Depends on CI-006 being resolved first (the template will reference the unlock-bpm scheme).

### CI-003—Per-chapter log-line examples in chapters 2–23 missing per-exercise duration

- Filed: 2026-08-10
- Location: `chapter-02.md` through `chapter-23.md`, each chapter's "Log line format" (or equivalent trailing) section. Concretely: `chapter-02.md:59`, `chapter-03.md:55`, `chapter-06.md:55`, `chapter-09.md:57`, `chapter-10.md:53`, `chapter-11.md:51`, `chapter-12.md:51`, `chapter-13.md:43`, `chapter-14.md:53`, `chapter-15.md:52`, `chapter-16.md:55`, `chapter-17.md:57`, `chapter-18.md:51`, `chapter-19.md:55`, `chapter-20.md:56`, `chapter-21.md:53`, `chapter-22.md:56`, `chapter-23.md:51`.
- Observed: `approach.md` §8 was updated on 2026-08-10 so each log line is `chapter.exercise  bpm  duration  verdict  note`—a five-field format that adds per-exercise duration. `chapter-01.md` was updated to match. The trailing "Log line format" example in every other chapter still shows the old four-field shape (e.g. `2.5  70 bpm  pass  even`).
- Concern: not urgent—Ch. 1 is the reference implementation, and later chapters are not yet in use. Deliberately deferred per the Ch. 1-first validation policy (see the shelved-propagation notes in memory).
- Next step: when propagating validated Ch. 1 conventions to chapters 2–23, update each footer example to the five-field form: `<chapter>.<exercise>  <bpm> bpm  <duration> min  <verdict>  <note>`. Chapters with sub-sections (12, 13, 14, 17, 19, 20, 21) keep their identifier convention; just insert the duration field before the verdict.

## Resolved

### CI-004—chapter-01.md log-entry references retain compact-line phrasing after §8 tabular rewrite

- Filed: 2026-08-20
- Location: [chapter-01.md](chapter-01.md) — "Your first session" step 8 (`Write one line in your session log`), "Your third session" steps 3–5 (`Log: 1.1  64 bpm  2 min  …`), "Log line format" section header near the bottom, and the trailing prose line in that section.
- Observed: 2026-08-20 (commit `da6049f`) rewrote approach.md §8 to lead with a tabular presentation of the session log and demoted the compact-line form to a plain-text-file alternative. approach.md §7 was updated in the same commit to neutral "Add a log entry" phrasing. chapter-01.md was not touched and still used "Write one line" wording and compact-line examples throughout, so it diverged from approach.md §7.
- Concern: minor — the compact-line form is still valid per new §8, so ch1's examples were not wrong. But a reader following ch1's "Your first session" walkthrough with a Google Docs table open would find "Write one line" jarring, and the "Log line format" section header read as line-based when the primary shape is tabular.
- Resolved: 2026-08-26—rewrote the four references in [chapter-01.md](chapter-01.md) to neutral "Add a log entry" phrasing matching approach.md §7: step 8 of "Your first session" ("Write one line in your session log" → "Add a log entry to your session log"); the three "Log:" prefixes in "Your third session" steps 3–5 → "Add a log entry:"; the section header "## Log line format" → "## Log entry format"; and the trailing prose "Log this chapter's work in your tracking document…" reworked to "Log entries for this chapter use…" with a cross-reference to approach.md §8 for both entry shapes (tabular and compact-line). Compact-line examples in the trailing prose kept as-is per CI-004's own next-step guidance.

### CI-007—"Two consecutive practice sessions" is ambiguous for Rotation exercises

- Filed: 2026-08-26
- Location: [approach.md §4](approach.md#4-the-tempo-target-and-clean-pass-rule) — advancement rule (currently the paragraph beginning "Advancement rule: when the current bpm yields a clean pass in two consecutive practice sessions…").
- Observed: the rule read "two consecutive practice sessions (i.e. two sessions in a row on the days you actually practise, not two sessions on the same day…)". This was unambiguous for Core exercises worked every session, but for Rotation exercises (Ch. 1 Ex. 12 and Ex. 13, and analogous rotation exercises in later chapters) that only get played every third or fourth session by design, "two consecutive practice sessions" had two readings: (a) two consecutive calendar practice sessions—in which case a Rotation exercise could never advance, because it structurally skipped sessions; or (b) two consecutive sessions in which the exercise was actually played—in which case intervening sessions where the exercise was not played did not break the streak. [chapter-02.md line 54](chapter-02.md) stated reading (b) directly for a worked Ch. 2 example ("The two passes accrue across sessions on the days you actually work Ex. 1, not back-to-back days on the calendar"), and [chapter-01.md line 94](chapter-01.md) stated it for Ch. 1 Rotation ("two consecutive `pass` sessions at the same bpm earn the +4 bpm raise—but the two sessions accrue across weeks rather than back-to-back days"), so the intended interpretation was clear in chapter sheets, but [approach.md §4](approach.md#4-the-tempo-target-and-clean-pass-rule) itself did not spell it out.
- Concern: a reader working straight from `approach.md` could reasonably read (a) and conclude the Rotation slot was a dead-end ladder. The advancement rule is a core operational rule; a rotation-specific clarification should not live only in a chapter sheet.
- Resolved: 2026-08-26—applied the light-touch swap in [approach.md §4](approach.md#4-the-tempo-target-and-clean-pass-rule)'s parenthetical: "two sessions in a row on the days you actually practise" → "two sessions in a row in which you actually work this exercise". The new wording covers Core exercises worked every session and Rotation exercises worked every third or fourth session identically—the streak is now explicitly per-exercise participation, not per-calendar-practice-day, so reading (a) is no longer available. Same-day exclusion is preserved by the following clause. Chapter-01 line 94 and chapter-02 line 54 continue to carry the worked-example detail that a reader who wants the concrete illustration can find them there; no downstream changes were needed.
- Lessons: the residual second-order question ("does an off-kit or `near` session at the exercise count towards the streak?") was already answered elsewhere in §4—off-kit sits outside the streak per [§7 off-kit session](approach.md#off-kit-session), and `near` resets the streak to zero per the `near` rule adopted in §4 alongside this filing. Once those two rules were in place, the (a)/(b) reading was the only remaining ambiguity and a wording swap was sufficient.

### CI-006—Unlock bpm scheme undefined for stage transitions beyond Stage 1 → 2

- Filed: 2026-08-20
- Location: [approach.md §5](approach.md#5-the-chapter-progression). Downstream: `chapter-02.md` through `chapter-13.md`, each of which will need a "Moving on to…" section citing the scheme.
- Observed: only Stage 1 → Stage 2 has a concrete unlock bpm (90 bpm on Ch. 1 Ex. 1, 10 and 11, validated through Richard's practice log 2026-07-30 → 2026-08-20). Every other transition in §5 is either vague ("once Stage 2 core beats hold ~90 bpm cleanly") or ungated. Within-stage sequences (Ch. 2 → 3 → 4 → 5, Ch. 6 → 7) are described as "strict sequence" but with no bpm numbers.
- Concern: chapter-02.md will need an unlock bpm in its "Moving on to…" section when Stage 2 unlocks (realistically ~1–2 weeks from filing). Without a scheme in place, that decision gets made in isolation rather than as part of a coherent stage-graph design.
- Resolved: 2026-08-21—rewrote [approach.md §5](approach.md#5-the-chapter-progression) around the four-rule scheme (gate exercises prep the next chapter's material; between-stage gates on 2–3 exercises, within-stage on 1; unlock bpm ≈ material-type target − 25%, rounded to a ladder step, per-transition rationale allowed; Stages 4/5/6 carry no unlock bpm). Numbers committed for the near-term transitions in a "Concrete unlock criteria (staging table)" alongside the scheme: Ch. 2 → 3 gates on Ch. 2 Ex. 10 at 82 bpm; Ch. 3 → 4 on Ch. 3 Ex. 12 at 82 bpm; Ch. 4 → 5 on Ch. 4 Ex. 12 at 82 bpm; Stage 2 → 3 on Ch. 1 Ex. 11 at 100 bpm plus Ch. 5 Ex. 13 at 88 bpm (both with tighter-than-25% margins per the between-stage override clause). Stage 3 internal (Ch. 6 → 7) and every transition at Stage 4, 5 or 6 remain deferred until those chapter sheets get their skeleton fill—captured in the closing sentence of the scheme block and in CI-005.
- Lessons: the staging table lives in §5 as a bridge until CI-005 (chapter-sheet template) lands and each row can migrate to its chapter sheet's "Moving on to…" section. Keeping numbers centralized while the target sheets are skeletons avoids the split-brain problem of half-filled chapter sheets.

### CI-002—Ch. 1 Reference exercises (2–9) mislabelled as "accent-variation studies"

- Filed: 2026-08-03
- Location: [chapter-01.md](chapter-01.md)—intro paragraph ("How to use this sheet"), rotation guidance paragraph, and Reference section body
- Observed: three places described exercises 2–9 as "accent-variation studies", and one of them additionally called them "quarter-note and 8th-note patterns". Visual inspection of the source PDF against a strong-foot / weak-foot / accent transcription (s = strong foot, w = weak foot, S = strong-foot accent, W = weak-foot accent) shows: Ex. 1.2 is 8ths, `ssssWWWWssssWWWW` (foot-grouping, no accents); Ex. 1.3 is 8ths, `ssssssssWWWWWWWW` (foot-grouping, no accents); Ex. 1.4 is 8ths, `SsssWwwwSsssWwww`; Ex. 1.5 is 8ths, `SsSsWwWwSsSsWwWw`; Ex. 1.6 is 8ths, `SssSssSsWwwWwwWw`; Ex. 1.7 is 8ths, `SssSsSsSWwwWwWwW`; Ex. 1.8 is 8ths, `SwsWsWsWsWsWsWsW`; Ex. 1.9 is 8ths, `SwsWSwsWSwsWSwsW`.
- Concern: the description is wrong on two counts—2 and 3 carry no accents at all (they vary foot grouping only), and none of 2–9 contain quarter notes. Readers using the Reference block as a menu would look for accent content in 2 and 3 that isn't there.
- Resolved: 2026-08-03—rewrote the three affected passages in `chapter-01.md`. The intro now splits 2–3 (foot-grouping, no accents) from 4–9 (accent variations on 8ths). The rotation-guidance line uses the same split. The Reference section body describes each sub-range in full and notes that 8–9 are single-stroke alternations between the feet (consistent with the book's own note on p. 6 that 8–12 are single-stroke rolls).
- Lessons: the extractor (`scripts/extract_source_data.py`) explicitly strips music notation—any line containing a notehead (`œ`), rest (`‰`) or clef (`÷`) is dropped, and the docstring calls out that exercise numbering "is entangled with music notation and cannot be parsed reliably." That means per-exercise rhythmic and accent descriptions in this manual are human-inspected against the score, not derived from `data/chapters/*.txt`. Same class of unreliability as CI-001: treat AI-assisted visual reads of R&L notation as reliable for gross layout only, and verify rhythm, foot assignment and accents by eye.

### CI-001—Ex. 1.1 pattern description does not match source PDF

- Filed: 2026-07-30
- Location: [chapter-01.md](chapter-01.md)—Core table, exercise 1 and walkthrough
- Observed: the sheet described Ex. 1.1 as "Quarter-note alternating between feet". The notation on R&L p. 6 is a 2-bar pattern—bar 1 is four quarter notes; bar 2 is four 8th-rest + 8th-note pairs (notes on the offbeats). Foot assignment is encoded via staff position per the "Key" panel on the intro page (BD I = strong foot, BD II = weak foot; see [approach.md §3.1](approach.md#31-notation-strong-foot--weak-foot-vs-rls-bd-i--bd-ii)).
- Concern: the description dropped bar 2 entirely, and the "alternating between feet" claim did not reflect what the score actually says.
- Edition discrepancy: **the two editions differ on this exercise.** The Original Edition places bar 1 on BD I (strong foot) and bar 2 on BD II (weak foot)—a strong-foot / weak-foot alternation across bars, which fits the chapter's stated purpose of isolating and developing the weak foot. The Revised Edition places both bars on BD I (strong foot); this appears to be a printing error. The manual takes the Original Edition as authoritative for this specific exercise.
- Resolved: 2026-07-31—updated Ex. 1's Pattern cell in `chapter-01.md` (Core table) and the walkthrough line to "Bar 1: quarter notes (strong foot). Bar 2: 8ths on the offbeats (weak foot).", following the Original Edition. Added an inline note under the Core table calling out the edition discrepancy. Introduced the strong-foot / weak-foot terminology across the manual and added [approach.md §3.1](approach.md#31-notation-strong-foot--weak-foot-vs-rls-bd-i--bd-ii) to explain both the terminology and the general edition policy (Revised default, per-exercise overrides logged here).
- Lessons: the original filing pointed at Ex. 1.10 based on a first-read impression, and my initial visual read of the Revised Edition PDF mistakenly claimed the two editions were identical for Ex. 1—both errors stemmed from reading rhythmic content (durations, groupings, tuplet markers) without reliably reading foot assignment (BD I vs BD II by staff position). Treat AI-assisted visual reads of R&L notation as reliable for rhythm and unreliable for foot assignment; verify stickings by eye.
