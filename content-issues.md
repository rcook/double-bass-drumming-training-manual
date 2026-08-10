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

### CI-003—Per-chapter log-line examples in chapters 2–23 missing per-exercise duration

- Filed: 2026-08-10
- Location: `chapter-02.md` through `chapter-23.md`, each chapter's "Log line format" (or equivalent trailing) section. Concretely: `chapter-02.md:59`, `chapter-03.md:55`, `chapter-06.md:55`, `chapter-09.md:57`, `chapter-10.md:53`, `chapter-11.md:51`, `chapter-12.md:51`, `chapter-13.md:43`, `chapter-14.md:53`, `chapter-15.md:52`, `chapter-16.md:55`, `chapter-17.md:57`, `chapter-18.md:51`, `chapter-19.md:55`, `chapter-20.md:56`, `chapter-21.md:53`, `chapter-22.md:56`, `chapter-23.md:51`.
- Observed: `approach.md` §8 was updated on 2026-08-10 so each log line is `chapter.exercise  bpm  duration  verdict  note`—a five-field format that adds per-exercise duration. `chapter-01.md` was updated to match. The trailing "Log line format" example in every other chapter still shows the old four-field shape (e.g. `2.5  70 bpm  pass  even`).
- Concern: not urgent—Ch. 1 is the reference implementation, and later chapters are not yet in use. Deliberately deferred per the Ch. 1-first validation policy (see the shelved-propagation notes in memory).
- Next step: when propagating validated Ch. 1 conventions to chapters 2–23, update each footer example to the five-field form: `<chapter>.<exercise>  <bpm> bpm  <duration> min  <verdict>  <note>`. Chapters with sub-sections (12, 13, 14, 17, 19, 20, 21) keep their identifier convention; just insert the duration field before the verdict.

## Resolved

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
