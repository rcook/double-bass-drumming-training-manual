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

### CI-001—Ex. 1.1 pattern description does not match source PDF

- Filed: 2026-07-30
- Location: [chapter-01.md](chapter-01.md)—Core table, exercise 1
- Observed: the sheet describes Ex. 1.1 as "Quarter-note alternating between feet". The revised-edition notation (R&L p. 6) is a 2-bar pattern—bar 1 is four quarter notes on the beat; bar 2 is four 8th-rest + 8th-note pairs (notes on the offbeats). No R/L stickings are shown in the score.
- Concern: the description drops bar 2 entirely, and "alternating between feet" is not supported by the score—it also contradicts the chapter's own framing, which places single-stroke rolls between the feet at Ex. 8–12, not Ex. 1. Ex. 1 reads more naturally as a weak-foot isolation study given the chapter's intro bullets.
- Next: rewrite the Pattern cell for Ex. 1 in `chapter-01.md` so both bars are described and no sticking is asserted. Cross-check against the original-edition PDF before closing.
- Update: 2026-07-31—original filing pointed at Ex. 1.10 based on a first-read impression. Visual read of PDF pp. 8–9 (revised edition) confirmed Ex. 10 (continuous 16ths) and Ex. 11 (8th-note triplets) match their `chapter-01.md` descriptions and are consistent with the intro bullet framing Ex. 8–12 as single-stroke rolls between the feet. The real defect is at Ex. 1; ticket re-scoped.

## Resolved

(No entries yet.)
