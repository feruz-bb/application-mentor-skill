#!/usr/bin/env python3
"""
Read an application document and report its text plus the metrics reviewers care about.

Handles .docx .doc .pptx .xlsx .rtf .txt .md natively with no third-party packages
(macOS textutil + Python's stdlib zip/XML). PDFs are NOT handled here — use the Read
tool on a PDF directly, it renders pages far better than any text dump would.

Usage:
    python3 read_document.py <file> [--stats-only] [--json]

Why the stats block matters: almost every application has a hard word or page limit,
and "one page" is the single most common CV instruction. Counting by eye is unreliable
and going over a stated limit is a mechanical rejection at many programs, so count
before you critique.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import zipfile
from xml.etree import ElementTree as ET

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
S = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"

# Rough page estimate for prose. Real pagination depends on font and margins, so treat
# this as a flag to check the PDF, not as ground truth.
WORDS_PER_PAGE = 500


def pptx_text(path):
    out = []
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        slides = sorted(
            (n for n in names if re.match(r"ppt/slides/slide\d+\.xml$", n)),
            key=lambda n: int(re.search(r"(\d+)", n).group(1)),
        )
        for i, s in enumerate(slides, 1):
            root = ET.fromstring(z.read(s))
            texts = [t.text for t in root.iter(A + "t") if t.text and t.text.strip()]
            out.append(f"\n===== SLIDE {i} =====")
            out.extend(texts)
            note = f"ppt/notesSlides/notesSlide{i}.xml"
            if note in names:
                nroot = ET.fromstring(z.read(note))
                ntexts = [t.text for t in nroot.iter(A + "t") if t.text and t.text.strip()]
                if ntexts:
                    out.append("--- speaker notes ---")
                    out.extend(ntexts)
    return "\n".join(out)


def xlsx_text(path):
    out = []
    with zipfile.ZipFile(path) as z:
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            for si in root.iter(S + "si"):
                shared.append("".join(t.text or "" for t in si.iter(S + "t")))
        for sh in sorted(n for n in z.namelist()
                         if re.match(r"xl/worksheets/sheet\d+\.xml$", n)):
            out.append(f"\n===== {os.path.basename(sh)} =====")
            root = ET.fromstring(z.read(sh))
            for row in root.iter(S + "row"):
                cells = []
                for c in row.iter(S + "c"):
                    v = c.find(S + "v")
                    if v is None or v.text is None:
                        cells.append("")
                    elif c.get("t") == "s":
                        idx = int(v.text)
                        cells.append(shared[idx] if idx < len(shared) else "")
                    else:
                        cells.append(v.text)
                if any(x.strip() for x in cells):
                    out.append(" | ".join(cells))
    return "\n".join(out)


def textutil(path):
    r = subprocess.run(
        ["textutil", "-convert", "txt", "-stdout", path],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        raise RuntimeError(f"textutil failed: {r.stderr.strip()}")
    return r.stdout


def plain(path):
    with open(path, "r", errors="replace") as f:
        return f.read()


def extract(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pptx":
        return pptx_text(path)
    if ext == ".xlsx":
        return xlsx_text(path)
    if ext in (".docx", ".doc", ".rtf", ".odt", ".html", ".htm"):
        return textutil(path)
    if ext in (".txt", ".md", ".text", ""):
        return plain(path)
    if ext == ".pdf":
        raise SystemExit(
            "PDF detected. Do not use this script — read the PDF directly with the Read "
            "tool (it supports a `pages` parameter). You will see layout and formatting, "
            "which matters for CV review and is lost in a text dump."
        )
    raise SystemExit(f"Unsupported file type: {ext}")


def stats(text):
    words = re.findall(r"[^\s]+", text)
    # Characters excluding whitespace — several application portals count this way.
    chars_no_space = len(re.sub(r"\s", "", text))
    paragraphs = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]
    longest = max(sentences, key=lambda s: len(s.split())) if sentences else ""
    return {
        "words": len(words),
        "characters_with_spaces": len(text),
        "characters_without_spaces": chars_no_space,
        "paragraphs": len(paragraphs),
        "sentences": len(sentences),
        "estimated_pages": round(len(words) / WORDS_PER_PAGE, 2),
        "avg_words_per_sentence": round(len(words) / len(sentences), 1) if sentences else 0,
        "longest_sentence_words": len(longest.split()),
        "longest_sentence": longest[:300],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--stats-only", action="store_true",
                    help="print only the metrics block, not the text")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    if not os.path.isfile(args.file):
        raise SystemExit(f"No such file: {args.file}")

    text = extract(args.file).strip()
    st = stats(text)

    if args.json:
        print(json.dumps({"file": args.file, "stats": st,
                          "text": None if args.stats_only else text},
                         ensure_ascii=False, indent=2))
        return

    print(f"FILE: {args.file}")
    print("--- METRICS ---")
    print(f"words: {st['words']}    "
          f"chars(no spaces): {st['characters_without_spaces']}    "
          f"chars(with spaces): {st['characters_with_spaces']}")
    print(f"paragraphs: {st['paragraphs']}    sentences: {st['sentences']}    "
          f"~pages: {st['estimated_pages']} (prose estimate, verify against the PDF)")
    print(f"avg words/sentence: {st['avg_words_per_sentence']}    "
          f"longest sentence: {st['longest_sentence_words']} words")
    if st["longest_sentence_words"] > 40:
        print(f"  ^ that sentence starts: {st['longest_sentence'][:120]}...")
    if not args.stats_only:
        print("\n--- TEXT ---")
        print(text)


if __name__ == "__main__":
    main()
