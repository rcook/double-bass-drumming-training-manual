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

(No open entries.)

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
