#!/usr/bin/env python3
"""Regenerate Mercer TL-paid salary increase bar chart with updated title."""
from pathlib import Path

import matplotlib.pyplot as plt

CHARTS_DIR = Path(__file__).resolve().parent
years = ["2023", "2024", "2025"]
pct = [75, 65, 40]  # median full-year salary increase (Mercer, all companies)

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(years, pct, color=["#1f77b4", "#ff7f0e", "#2ca02c"], edgecolor="black", linewidth=0.8)
ax.set_ylabel("Median full-year salary increase (%)")
ax.set_xlabel("Year")
ax.set_title("Mercer-reported annual salary increase for TL-paid employees")
ax.set_ylim(0, max(pct) * 1.15)
for b in bars:
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f"{int(b.get_height())}%", ha="center", fontsize=12)
plt.tight_layout()
out = CHARTS_DIR / "mercer_turkey_salary_increase_trend.png"
plt.savefig(out, dpi=200)
plt.close()
print(f"Saved: {out}")
