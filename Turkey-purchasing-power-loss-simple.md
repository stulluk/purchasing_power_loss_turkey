# Purchasing Power of a Fixed USD Salary in Turkey

A USD salary earned in Turkey loses value when Turkish inflation outpaces the USD/TRY exchange rate gain. This document tracks that gap using three independent inflation sources.

### Sources

| Source | What it is |
| :--- | :--- |
| **TÜİK** | Government statistics agency — official nationwide CPI |
| **İTO** | Istanbul Chamber of Commerce — Istanbul-specific CPI |
| **ENAG** | Independent academic group — alternative CPI, generally higher than TÜİK |
| **TCMB** | Central bank — official USD/TRY exchange rates |

### How it works

Starting from a baseline of 100 in December 2023, each month we adjust for two things: how much more TRY you get per dollar (good), and how much prices went up (bad). When prices rise faster than the exchange rate, purchasing power drops.

Formula: `PP_new = PP_old × (1 + USD/TRY change) / (1 + inflation)`

### Cumulative change since December 2023

| Period | USD/TRY gained | TÜİK inflation | İTO inflation | ENAG inflation |
| :--- | :---: | :---: | :---: | :---: |
| Dec 2023 → Jan 2025 (13 mo) | +21.5% | +51.6% | +59.0% | +96.0% |
| Dec 2023 → Jan 2026 (25 mo) | +47.2% | +98.1% | +116.5% | +200.3% |

The exchange rate gained 47% over two years, but prices rose 98–200% depending on the source. The gap is the purchasing power loss.

### Purchasing Power Index

100 = December 2023 baseline. Lower = less buying power.

| Date | USD/TRY | USD/TRY change | TÜİK inflation | **PP (TÜİK)** |
| :--- | :---: | :---: | :---: | :---: |
| **Dec 2023** | 29.4913 | — | — | **100.00** |
| **Jan 2024** | 30.3497 | +2.9% | +6.7% | **96.45** |
| **Jan 2025** | 35.8274 | +21.5% | +51.6% | **80.12** |
| **Jan 2026** | 43.4195 | +47.2% | +98.1% | **74.31** |

### What this means

As of January 2026, a person earning a fixed USD salary in Turkey can buy:

| Source | Purchasing power left | Loss |
| :--- | :---: | :---: |
| TÜİK (government) | 74% | **~26%** |
| İTO (Istanbul chamber) | 68% | **~32%** |
| ENAG (independent) | 49% | **~51%** |

The real impact likely falls in the İTO–ENAG range. In practical terms, a USD earner in Turkey has lost roughly **one-third to one-half** of their purchasing power in just two years.

### Data sources

- **USD/TRY rates:** [TCMB daily exchange rate bulletins](https://www.tcmb.gov.tr/kurlar/today.xml) (ForexSelling rate)
- **TÜİK CPI:** [TÜİK data portal](https://veriportali.tuik.gov.tr/)
- **İTO CPI:** [İTO statistics](https://bilgibankasi.ito.org.tr/tr/istatistik-verileri/genel)
- **ENAG CPI:** [ENAGrup bulletins](https://enagrup.org/) (archived via [Wayback Machine](https://web.archive.org/web/*/https://enagrup.org/*))
- **Full monthly breakdown:** See the detailed version of this document with all 25 months, exact MoM rates, and source links.
