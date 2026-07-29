#!/usr/bin/env python3
"""Extract structural metadata from the source PDF.

Reads a single PDF file from source-material/ and writes deterministic JSON
output to data/. Captures chapter number, title, book-page range, PDF-page
range and the section labels present (Warm-Ups / Beats / Fills).

Does NOT extract musical notation, verbatim intro bullets, footings tables or
exercise-number ranges. The book's exercise numbering is entangled with music
notation and cannot be parsed reliably from the PDF text stream.

Usage: python scripts/extract_source_data.py

See scripts/README.md for full usage instructions.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    sys.stderr.write(
        "pdfplumber is not installed. Install it with `pip install pdfplumber` "
        "and re-run. See scripts/README.md for details.\n"
    )
    sys.exit(1)


REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_MATERIAL_DIR = REPO_ROOT / "source-material"
DATA_DIR = REPO_ROOT / "data"
CHAPTERS_DIR = DATA_DIR / "chapters"
INDEX_PATH = DATA_DIR / "source-index.json"

CHAPTER_MARKER = re.compile(r"^\s*Chapter\s+(\d+)\s*$", re.MULTILINE)
SECTION_HEADINGS = ("Warm-Ups", "Beats", "Fills")
BACK_MATTER_MARKERS = ("Double Bass Time Line", "Double Bass Discography")

# Right-side footer, plain rendering: "... Encyclopedia Of Double Bass Drumming 5"
FOOTER_RIGHT_PLAIN = re.compile(
    r"Encyclopedia\s+Of\s+Double\s+Bass\s+Drumming\s+(\d+)\b"
)
# Right-side footer, bold rendering makes pdfplumber emit each character twice —
# the marker becomes "EEnnccyyccllooppeeddiiaa OOff ... DDrruummmmiinngg 1199" (= "19").
FOOTER_RIGHT_DOUBLED = re.compile(
    r"EEnnccyyccllooppeeddiiaa\s+OOff\s+DDoouubbllee\s+BBaassss\s+DDrruummmmiinngg\s+(\d+)\b"
)
# Left-side footer, plain rendering: "74 Encyclopedia Of Double Bass Drumming"
FOOTER_LEFT_PLAIN = re.compile(
    r"(?m)^\s*(\d+)\s+Encyclopedia\s+Of\s+Double\s+Bass\s+Drumming\b"
)
# Left-side footer, bold rendering: number precedes the doubled-letter marker.
FOOTER_LEFT_DOUBLED = re.compile(
    r"(?m)^\s*(\d+)\s+EEnnccyyccllooppeeddiiaa"
)

# Chapter titles from the book's table of contents (R&L p. 2).
# Hardcoded because the PDF's visual layout puts the title above "Chapter N"
# and pdfplumber reads Ch. 8 out of visual order; hardcoding is safer than
# heuristic reconstruction from the extracted text.
CHAPTER_TITLES: dict[int, str] = {
    1: "Starters",
    2: "Two Consecutive 16th Notes",
    3: "Three Consecutive 16th Notes",
    4: "Four Consecutive 16th Notes",
    5: "Five To Sixteen Consecutive 16th Notes",
    6: "8th-Note Triplets",
    7: "16th-Note Triplets",
    8: "32nd-Notes and 32nd-Note Triplets",
    9: "The Blues",
    10: "8th Notes",
    11: "Power Threes",
    12: "Linear Cross Rhythms",
    13: "Linear Cross-Rhythm Combinations",
    14: "Fast Track Double Bass",
    15: "Starters — Double Strokes",
    16: "Feet Only",
    17: "Binary Beats and Fills",
    18: "Feet Only — Triplets",
    19: "Ternary Beats and Fills",
    20: "Skiplets",
    21: "Turn the Beat Around (Turnarounds)",
    22: "The Ladder",
    23: "Double-Stroke Hands, Single-Stroke Feet",
}


@dataclass
class ChapterInfo:
    number: int
    title: str
    start_book_page: int
    end_book_page: int
    start_pdf_page: int
    end_pdf_page: int
    section_labels: list[str]


def find_pdf() -> Path:
    if not SOURCE_MATERIAL_DIR.exists():
        raise SystemExit(
            f"source-material/ directory not found at {SOURCE_MATERIAL_DIR}.\n"
            "See scripts/README.md — put your legally acquired PDF under source-material/."
        )
    pdfs = sorted(SOURCE_MATERIAL_DIR.glob("*.pdf"))
    if not pdfs:
        raise SystemExit(
            "No PDF found under source-material/.\n"
            "See scripts/README.md — put your legally acquired PDF under source-material/."
        )
    if len(pdfs) > 1:
        raise SystemExit(
            "Multiple PDFs found under source-material/: "
            f"{', '.join(p.name for p in pdfs)}\n"
            "Keep only one and re-run."
        )
    return pdfs[0]


def dedouble(digits: str) -> str | None:
    """Undo pdfplumber's doubled-character reading for the bold left-side footer.

    "1122" -> "12"; "7700" -> "70"; "66" -> "6". Returns None if the string is
    not cleanly doubled (odd length, or paired digits do not match).
    """
    if len(digits) % 2 != 0 or not digits:
        return None
    out: list[str] = []
    for i in range(0, len(digits), 2):
        if digits[i] != digits[i + 1]:
            return None
        out.append(digits[i])
    return "".join(out)


def extract_book_page_number(page_text: str) -> int | None:
    right_plain = FOOTER_RIGHT_PLAIN.search(page_text)
    if right_plain:
        return int(right_plain.group(1))
    right_doubled = FOOTER_RIGHT_DOUBLED.search(page_text)
    if right_doubled:
        dedoubled = dedouble(right_doubled.group(1))
        if dedoubled is not None:
            return int(dedoubled)
    left_plain = FOOTER_LEFT_PLAIN.search(page_text)
    if left_plain:
        return int(left_plain.group(1))
    left_doubled = FOOTER_LEFT_DOUBLED.search(page_text)
    if left_doubled:
        dedoubled = dedouble(left_doubled.group(1))
        if dedoubled is not None:
            return int(dedoubled)
    return None


def find_chapter_starts(pages_text: list[str]) -> list[tuple[int, int, str]]:
    """Return (pdf_page_0based, chapter_number, chapter_title) sorted by chapter number.

    Detects each chapter's PDF page by locating the "Chapter N" marker;
    titles come from the hardcoded CHAPTER_TITLES map (see comment there).
    """
    results: dict[int, int] = {}
    for pdf_idx, text in enumerate(pages_text):
        for match in CHAPTER_MARKER.finditer(text):
            chapter_num = int(match.group(1))
            if chapter_num in results:
                continue
            results[chapter_num] = pdf_idx

    missing = sorted(set(CHAPTER_TITLES) - set(results))
    if missing:
        raise SystemExit(
            f"Chapters not detected in the PDF: {missing}. "
            "The PDF layout may differ from the expected edition."
        )
    unexpected = sorted(set(results) - set(CHAPTER_TITLES))
    if unexpected:
        raise SystemExit(
            f"Unexpected chapter numbers found in the PDF: {unexpected}. "
            "The PDF layout may differ from the expected edition."
        )
    return [(pdf_idx, num, CHAPTER_TITLES[num]) for num, pdf_idx in sorted(results.items())]


def find_back_matter_start(pages_text: list[str], after_pdf_idx: int) -> int | None:
    """PDF page index (0-based) of the first back-matter page, searching only
    after the last chapter's start page to avoid matching the table of contents.
    """
    for pdf_idx in range(after_pdf_idx + 1, len(pages_text)):
        text = pages_text[pdf_idx]
        for marker in BACK_MATTER_MARKERS:
            if re.search(rf"^\s*{re.escape(marker)}\s*$", text, re.MULTILINE):
                return pdf_idx
    return None


def find_section_labels(chapter_text: str) -> list[str]:
    """Return the section-heading labels present in a chapter, in book order.

    Detects the label at line-start followed by end-of-line, or followed by a
    bullet-continuation on the same line — the PDF's layout sometimes puts a
    section heading on the same visual line as the last intro bullet.

    Exercise numbering is not extracted — the book's numbering is entangled
    with musical notation in ways that pdfplumber cannot reliably parse.
    Per-chapter sheets should count exercises visually against the book.
    """
    positions: list[tuple[int, str]] = []
    for label in SECTION_HEADINGS:
        pattern = rf"(?m)^{re.escape(label)}(?:\s*$|\s+•)"
        for match in re.finditer(pattern, chapter_text):
            positions.append((match.start(), label))
    positions.sort(key=lambda p: p[0])
    seen = set()
    result: list[str] = []
    for _, label in positions:
        if label not in seen:
            seen.add(label)
            result.append(label)
    return result


def build_chapters(pages_text: list[str]) -> list[ChapterInfo]:
    chapter_starts = find_chapter_starts(pages_text)
    if not chapter_starts:
        raise SystemExit("No chapter headings detected. The PDF may not be the expected book.")

    last_chapter_start_pdf_idx = chapter_starts[-1][0]
    back_matter_pdf_idx = find_back_matter_start(pages_text, last_chapter_start_pdf_idx)
    last_content_pdf_idx = (
        back_matter_pdf_idx - 1 if back_matter_pdf_idx is not None else len(pages_text) - 1
    )

    chapters: list[ChapterInfo] = []
    for i, (start_pdf_idx, chapter_num, title) in enumerate(chapter_starts):
        if i + 1 < len(chapter_starts):
            next_start = chapter_starts[i + 1][0]
            end_pdf_idx = max(start_pdf_idx, next_start - 1)
        else:
            end_pdf_idx = last_content_pdf_idx

        start_book_page = extract_book_page_number(pages_text[start_pdf_idx])
        end_book_page = extract_book_page_number(pages_text[end_pdf_idx])
        if start_book_page is None:
            raise SystemExit(
                f"Could not detect start book page for chapter {chapter_num}. "
                "The PDF layout may differ from the expected edition."
            )
        if end_book_page is None:
            end_book_page = start_book_page

        chapter_text = "\n".join(pages_text[start_pdf_idx : end_pdf_idx + 1])
        section_labels = find_section_labels(chapter_text)

        chapters.append(
            ChapterInfo(
                number=chapter_num,
                title=title,
                start_book_page=start_book_page,
                end_book_page=end_book_page,
                start_pdf_page=start_pdf_idx + 1,
                end_pdf_page=end_pdf_idx + 1,
                section_labels=section_labels,
            )
        )
    return chapters


def chapter_to_dict(ch: ChapterInfo) -> dict:
    return {
        "number": ch.number,
        "title": ch.title,
        "start_book_page": ch.start_book_page,
        "end_book_page": ch.end_book_page,
        "start_pdf_page": ch.start_pdf_page,
        "end_pdf_page": ch.end_pdf_page,
        "section_labels": ch.section_labels,
    }


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    pdf_path = find_pdf()
    with pdfplumber.open(pdf_path) as pdf:
        pages_text = [(page.extract_text() or "") for page in pdf.pages]

    chapters = build_chapters(pages_text)

    index = {
        "book": {
            "title": "The Encyclopedia of Double Bass Drumming (Revised Edition)",
            "authors": ["Bobby Rondinelli", "Michael Lauren"],
        },
        "chapter_count": len(chapters),
        "chapters": [chapter_to_dict(ch) for ch in chapters],
    }
    write_json(INDEX_PATH, index)

    for ch in chapters:
        write_json(CHAPTERS_DIR / f"chapter-{ch.number:02d}.json", chapter_to_dict(ch))

    sys.stdout.write(f"Wrote {INDEX_PATH.relative_to(REPO_ROOT)}\n")
    sys.stdout.write(
        f"Wrote {len(chapters)} chapter files under "
        f"{CHAPTERS_DIR.relative_to(REPO_ROOT)}/\n"
    )


if __name__ == "__main__":
    main()
