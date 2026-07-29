# Extraction scripts

Tooling that turns a legally acquired copy of *The Encyclopedia of Double Bass Drumming (Revised Edition)* into structured metadata the training manual can reference.

## Prerequisites

- Python 3.10 or later
- One dependency: `pdfplumber`

Install into a virtual environment (recommended, especially on macOS where the system Python is externally managed):

```
python3 -m venv .venv
source .venv/bin/activate
pip install pdfplumber
```

## Place the PDF

Put your legally acquired copy of the book under `source-material/` at the repo root. The filename does not matter — the script matches any `*.pdf` in that directory. The directory is gitignored, so the PDF never gets committed.

## Run the script

From the repo root:

```
python scripts/extract_source_data.py
```

The script writes two things:

- `data/source-index.json` — the whole-book index in one file
- `data/chapters/chapter-NN.json` — one file per chapter (23 files, `chapter-01.json` through `chapter-23.json`)

`data/` is gitignored. The output is meant to be regenerated locally, not shared.

## What the output contains

Each chapter entry has:

- `number` — chapter number
- `title` — chapter title (from the book's table of contents)
- `start_book_page`, `end_book_page` — the book's own page numbers
- `start_pdf_page`, `end_pdf_page` — 1-indexed page numbers within the PDF file
- `section_labels` — which of `Warm-Ups`, `Beats`, `Fills` appear as headings in that chapter, in book order. Some chapters have no such headings; the list is empty in that case.

Exercise numbering is deliberately not extracted. The book's exercise numbers are entangled with musical notation, and pdfplumber's text stream cannot separate them reliably. Per-chapter working sheets should count exercises visually against the book.

## Reproducibility

The script is deterministic. Running it twice against the same PDF produces byte-identical output. Verify with:

```
python scripts/extract_source_data.py
cp -r data /tmp/data-run1
rm -rf data
python scripts/extract_source_data.py
diff -r /tmp/data-run1 data
```

If the two runs ever differ, that is a bug worth reporting.

## Copyright note

The script indexes your own copy of the book. It does not distribute the book, and its output (`data/`) is gitignored precisely so that extracted structural data does not leak into a public repository. The copyright of the source book belongs to Modern Drummer Media LLC; nothing in this project reproduces the book's content beyond what is needed to reference structural landmarks (chapter titles, page numbers, section headings).
