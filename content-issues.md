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

### CI-001—Ex. 1.10 pattern description may not match source PDF

- Filed: 2026-07-30
- Location: [chapter-01.md](chapter-01.md)—Core table, exercise 10
- Observed: the sheet describes Ex. 1.10 as "16th-note single-stroke roll between feet".
- Concern: the sheet music in R&L p. 6 (per a first read-through by the user) does not appear to match that description.
- Next: re-read the source PDF pp. 6–7 with the sheet music in hand; confirm the pattern actually notated for Ex. 10 (and Ex. 11 for consistency, since it is described here as an 8th-note-triplet single-stroke roll); update `chapter-01.md` if the description is wrong, or close this entry with a note if the description is right.

## Resolved

(No entries yet.)
