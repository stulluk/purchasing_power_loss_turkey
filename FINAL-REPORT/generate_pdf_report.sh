#!/usr/bin/env bash
# Generate the final PDF report from the Markdown source.
# Run from the project root (parent of FINAL-REPORT).

set -e
TOPDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$TOPDIR"

MD="FINAL-REPORT/Purchasing_Power_Loss_in_Turkey_for_USD_Earning_Personnel_2023-2026.md"
PDF="FINAL-REPORT/Purchasing_Power_Loss_in_Turkey_for_USD_Earning_Personnel_2023-2026.pdf"

pandoc "$MD" -o "$PDF" \
  --pdf-engine=xelatex \
  --resource-path=.:etc:charts

echo "Generated: $PDF"
