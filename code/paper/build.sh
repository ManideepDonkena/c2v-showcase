#!/bin/sh
# Rebuild every table and number from the result files, then both PDFs.
set -e
cd "$(dirname "$0")"
/home/mani/manim/lessonforge/.venv/bin/python make_tables.py 2>/dev/null | tail -1
/home/mani/manim/lessonforge/.venv/bin/python make_figures.py 2>/dev/null | grep -c figure | sed "s/$/ figures/"
/home/mani/manim/lessonforge/.venv/bin/python make_layout_examples.py 2>/dev/null | tail -1
for d in main report long_report; do
  pdflatex -interaction=nonstopmode -halt-on-error $d.tex > /dev/null
  bibtex $d > /dev/null || true
  pdflatex -interaction=nonstopmode -halt-on-error $d.tex > /dev/null
  pdflatex -interaction=nonstopmode -halt-on-error $d.tex > /dev/null
  echo "$d.pdf: $(pdfinfo $d.pdf | awk '/Pages/{print $2}') pages, $(grep -c 'Overfull' $d.log) overfull boxes"
done
