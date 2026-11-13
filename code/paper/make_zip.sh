#!/bin/sh
# Rebuild every table, figure and PDF, then pack a self-contained LaTeX bundle (sources, generated tables, data
# figures, image prompts, compiled PDFs) into paper/dist/. Add illustrations to figures/ and compile; see
# README_COMPILE.md inside the zip.
set -e
cd "$(dirname "$0")"
./build.sh
stamp=$(date +%Y%m%d-%H%M)
tmp=$(mktemp -d)
dst="$tmp/c2v-paper"
mkdir -p "$dst/sections" "$dst/tables" "$dst/figures" "$dst/pdf"
cp main.tex report.tex long_report.tex preamble.tex refs.bib README_COMPILE.md "$dst/"
cp sections/*.tex "$dst/sections/"
cp tables/*.tex "$dst/tables/"
cp figures/*.pdf figures/IMAGE_PROMPTS.md "$dst/figures/"
for f in figures/*.png figures/*.jpg; do [ -f "$f" ] && cp "$f" "$dst/figures/"; done
cp main.pdf report.pdf long_report.pdf "$dst/pdf/"
# the result files behind the final numbers, frozen with the PDFs
for d in layout-study novel12-ladder mmmc-n12-seed0-ladder noise-model; do
  [ -d "../bench/results/$d" ] && mkdir -p "$dst/results/$d" && cp ../bench/results/$d/*.json ../bench/results/$d/*.md "$dst/results/$d/" 2>/dev/null || true
done
cp tables/pilot_frozen.json "$dst/results/" 2>/dev/null || true
mkdir -p dist
(cd "$tmp" && zip -qr "c2v-paper-$stamp.zip" c2v-paper)
mv "$tmp/c2v-paper-$stamp.zip" dist/
cp "dist/c2v-paper-$stamp.zip" dist/c2v-paper-latest.zip
rm -rf "$tmp"
echo "dist/c2v-paper-$stamp.zip ($(du -h dist/c2v-paper-$stamp.zip | cut -f1))"
