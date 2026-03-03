# Turkish Economic Data & Purchasing Power Analysis (2024 - 2026)

This document tracks the real purchasing power of a fixed USD income relative to inflation and USD/TRY exchange rate fluctuations in Turkey, using three independent inflation sources.

### Glossary

| Term | What It Is |
| :--- | :--- |
| **TCMB / CBRT** | Turkey's central bank. Publishes official daily exchange rates. |
| **TÜİK** | Government statistics agency. Publishes the official nationwide inflation (CPI). |
| **İTO** | Istanbul Chamber of Commerce. Publishes Istanbul-specific consumer price index. |
| **ENAG** | Independent academic group. Calculates an alternative inflation rate, generally higher than TÜİK. |
| **MoM** | Month over Month — percentage change from end of previous month to end of current month. |
| **ForexSelling** | TCMB's indicative rate for electronic USD→TRY conversions (wire transfers, salary payments). |
| **PP** | Purchasing Power index. 100 = Dec 2023 baseline; 50 = half the buying power. |

### Methodology
* **Base:** Index = 100.00 as of December 31, 2023.
* **USD/TRY Rate:** TCMB ForexSelling from end-of-month XML bulletins.
* **Formula:** `Index_new = Index_old × (1 + USD_MoM) / (1 + inflation_MoM)`

| Date | USD/TRY MoM | CBRT Link | TÜİK MoM | TÜİK Source | İTO MoM | ENAG MoM | ENAG Source | **PP (TÜİK)** | **PP (İTO)** | **PP (ENAG)** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Dec 2023** | - | [Base](https://www.tcmb.gov.tr/kurlar/202312/29122023.xml) | - | - | - | - | - | **100.00** | **100.00** | **100.00** |
| **Jan 2024** | +2.91% | [Link](https://www.tcmb.gov.tr/kurlar/202401/31012024.xml) | 6.70% | [TÜİK 53622](https://veriportali.tuik.gov.tr/tr/press/53622) | 7.57% | 9.38% | [ENAG](https://web.archive.org/web/20250727013833/https://enagrup.org/bulten/oca24.pdf) | **96.45** | **95.67** | **94.09** |
| **Feb 2024** | +2.85% | [Link](https://www.tcmb.gov.tr/kurlar/202402/29022024.xml) | 4.53% | [TÜİK 53623](https://veriportali.tuik.gov.tr/tr/press/53623) | 3.99% | 4.32% | [ENAG](https://web.archive.org/web/20240326044118/https://enagrup.org/bulten/feb24.pdf) | **94.90** | **94.62** | **92.76** |
| **Mar 2024** | +3.61% | [Link](https://www.tcmb.gov.tr/kurlar/202403/29032024.xml) | 3.16% | [TÜİK 53613](https://veriportali.tuik.gov.tr/tr/press/53613) | 2.70% | 5.68% | [ENAG](https://web.archive.org/web/20240508143344/https://enagrup.org/bulten/mar24.pdf) | **95.32** | **95.46** | **90.95** |
| **Apr 2024** | +0.07% | [Link](https://www.tcmb.gov.tr/kurlar/202404/30042024.xml) | 3.18% | [TÜİK 53614](https://veriportali.tuik.gov.tr/tr/press/53614) | 4.17% | 5.02% | [ENAG](https://web.archive.org/web/20240516013550/https://enagrup.org/bulten/nis24.pdf) | **92.45** | **91.71** | **86.66** |
| **May 2024** | -0.54% | [Link](https://www.tcmb.gov.tr/kurlar/202405/31052024.xml) | 3.37% | [TÜİK 53615](https://veriportali.tuik.gov.tr/tr/press/53615) | 2.22% | 5.66% | [ENAG](https://web.archive.org/web/20240603235509/https://enagrup.org/bulten/may24.pdf) | **88.95** | **89.23** | **81.58** |
| **Jun 2024** | +2.15% | [Link](https://www.tcmb.gov.tr/kurlar/202406/28062024.xml) | 1.64% | [TÜİK 53616](https://veriportali.tuik.gov.tr/tr/press/53616) | 2.71% | 4.27% | [ENAG](https://web.archive.org/web/20240704203328/https://www.enagrup.org/bulten/haz24.pdf) | **89.40** | **88.75** | **79.92** |
| **Jul 2024** | +0.78% | [Link](https://www.tcmb.gov.tr/kurlar/202407/31072024.xml) | 3.23% | [TÜİK 53617](https://veriportali.tuik.gov.tr/tr/press/53617) | 3.99% | 5.91% | [ENAG](https://web.archive.org/web/20240805162753/https://enagrup.org/bulten/tem24.pdf) | **87.28** | **86.01** | **76.05** |
| **Aug 2024** | +2.54% | [Link](https://www.tcmb.gov.tr/kurlar/202408/29082024.xml) | 2.47% | [TÜİK 53624](https://veriportali.tuik.gov.tr/tr/press/53624) | 3.03% | 3.47% | [?ENAG](https://tr.euronews.com/business/2024/09/03/tuik-agustos-ayi-enflasyonu-247-olurken-yillik-enflasyon-5197-olarak-gerceklesti) | **87.34** | **85.60** | **75.37** |
| **Sep 2024** | +0.58% | [Link](https://www.tcmb.gov.tr/kurlar/202409/30092024.xml) | 2.97% | [TÜİK 53618](https://veriportali.tuik.gov.tr/tr/press/53618) | 3.25% | 5.34% | [ENAG](https://web.archive.org/web/20241003095833/https://enagrup.org/bulten/24sep.pdf) | **85.31** | **83.39** | **71.97** |
| **Oct 2024** | +0.17% | [Link](https://www.tcmb.gov.tr/kurlar/202410/31102024.xml) | 2.88% | [TÜİK 53619](https://veriportali.tuik.gov.tr/tr/press/53619) | 3.25% | 5.57% | [ENAG](https://web.archive.org/web/20241104143837/https://enagrup.org/bulten/24oct.pdf) | **83.07** | **80.90** | **68.27** |
| **Nov 2024** | +1.17% | [Link](https://www.tcmb.gov.tr/kurlar/202411/29112024.xml) | 2.24% | [TÜİK 53620](https://veriportali.tuik.gov.tr/tr/press/53620) | 3.07% | 4.06% | [ENAG](https://web.archive.org/web/20250807163506/https://enagrup.org/bulten/24nov.pdf) | **82.20** | **79.41** | **66.38** |
| **Dec 2024** | +2.03% | [Link](https://www.tcmb.gov.tr/kurlar/202412/31122024.xml) | 1.03% | [TÜİK 53621](https://veriportali.tuik.gov.tr/tr/press/53621) | 1.67% | 2.34% | [ENAG](https://web.archive.org/web/20250228114607/https://enagrup.org/bulten/24dec.pdf) | **83.01** | **79.69** | **66.18** |
| **Jan 2025** | +1.37% | [Link](https://www.tcmb.gov.tr/kurlar/202501/31012025.xml) | 5.03% | [TÜİK 54176](https://veriportali.tuik.gov.tr/tr/press/54176) | 5.74% | 8.22% | [ENAG](https://web.archive.org/web/20250228133517/https://enagrup.org/bulten/jan25.pdf) | **80.12** | **76.40** | **61.99** |
| **Feb 2025** | +1.73% | [Link](https://www.tcmb.gov.tr/kurlar/202502/28022025.xml) | 2.27% | [TÜİK 54177](https://veriportali.tuik.gov.tr/tr/press/54177) | 2.54% | 3.37% | [ENAG](https://web.archive.org/web/20250520082029/https://www.enagrup.org/bulten/feb25.pdf) | **79.69** | **75.79** | **61.00** |
| **Mar 2025** | +3.81% | [Link](https://www.tcmb.gov.tr/kurlar/202503/28032025.xml) | 2.46% | [TÜİK 54178](https://veriportali.tuik.gov.tr/tr/press/54178) | 3.12% | 3.91% | [?ENAG](https://tr.euronews.com/2025/04/03/tuike-gore-mart-ayinda-yillik-enflasyon-yuzde-3810-enaga-gore-7520-kira-artis-orani-5126-o) | **80.74** | **76.30** | **60.94** |
| **Apr 2025** | +1.60% | [Link](https://www.tcmb.gov.tr/kurlar/202504/30042025.xml) | 3.00% | [TÜİK 54179](https://veriportali.tuik.gov.tr/tr/press/54179) | 4.39% | 4.46% | [?ENAG](https://tr.euronews.com/2025/05/05/nisan-ayinda-yillik-enflasyon-tuik-yuzde-3786-enag-7388-kira-artis-orani-4873) | **79.64** | **74.25** | **59.28** |
| **May 2025** | +1.81% | [Link](https://www.tcmb.gov.tr/kurlar/202505/30052025.xml) | 1.53% | [TÜİK 54180](https://veriportali.tuik.gov.tr/tr/press/54180) | 1.57% | 3.66% | [?ENAG](https://tr.euronews.com/business/2025/06/03/mayista-yillik-enflasyon-tuik-yuzde-3541-enag-ise-yuzde-7123-acikladi) | **79.86** | **74.43** | **58.22** |
| **Jun 2025** | +1.74% | [Link](https://www.tcmb.gov.tr/kurlar/202506/30062025.xml) | 1.37% | [TÜİK 54181](https://veriportali.tuik.gov.tr/tr/press/54181) | 1.77% | 3.05% | [?ENAG](https://tr.euronews.com/business/2025/07/03/haziranda-yillik-enflasyon-tuik-yuzde-3505-enag-ise-yuzde-6868-acikladi) | **80.15** | **74.40** | **57.48** |
| **Jul 2025** | +1.94% | [Link](https://www.tcmb.gov.tr/kurlar/202507/31072025.xml) | 2.06% | [TÜİK 54182](https://veriportali.tuik.gov.tr/tr/press/54182) | 2.62% | 3.75% | [?ENAG](https://tr.euronews.com/2025/08/04/temmuzda-yillik-enflasyon-tuik-yuzde-3352-enag-ise-yuzde-6515-acikladi) | **80.05** | **73.91** | **56.48** |
| **Aug 2025** | +1.06% | [Link](https://www.tcmb.gov.tr/kurlar/202508/29082025.xml) | 2.04% | [TÜİK 54183](https://veriportali.tuik.gov.tr/tr/press/54183) | 1.84% | 3.23% | [?ENAG](https://tr.euronews.com/2025/09/03/agustosta-yillik-enflasyon-tuik-yuzde-3295-enag-ise-yuzde-6549-acikladi) | **79.29** | **73.35** | **55.29** |
| **Sep 2025** | +1.37% | [Link](https://www.tcmb.gov.tr/kurlar/202509/30092025.xml) | 3.23% | [TÜİK 54184](https://veriportali.tuik.gov.tr/tr/press/54184) | 3.19% | 3.79% | [?ENAG](https://tr.euronews.com/business/2025/10/03/eylul-ayinda-yillik-enflasyon-tuik-yuzde-3329-enag-ise-yuzde-6323-acikladi) | **77.86** | **72.06** | **54.00** |
| **Oct 2025** | +0.93% | [Link](https://www.tcmb.gov.tr/kurlar/202510/31102025.xml) | 2.55% | [TÜİK 54185](https://veriportali.tuik.gov.tr/tr/press/54185) | 3.31% | 3.74% | [?ENAG](https://tr.euronews.com/business/2025/11/03/ekim-ayinda-yillik-enflasyon-tuik-yuzde-3287-enag-ise-yuzde-60-acikladi) | **76.63** | **70.40** | **52.54** |
| **Nov 2025** | +1.10% | [Link](https://www.tcmb.gov.tr/kurlar/202511/28112025.xml) | 0.87% | [TÜİK 54186](https://veriportali.tuik.gov.tr/tr/press/54186) | 1.19% | 2.13% | [?ENAG](https://tr.euronews.com/business/2025/12/03/kasim-ayinda-yillik-enflasyon-tuik-yuzde-3107-enag-ise-yuzde-5682-olarak-acikladi) | **76.81** | **70.34** | **52.01** |
| **Dec 2025** | +1.16% | [Link](https://www.tcmb.gov.tr/kurlar/202512/31122025.xml) | 0.89% | [TÜİK 58294](https://veriportali.tuik.gov.tr/tr/press/58294) | 1.23% | 2.11% | [?ENAG](https://tr.euronews.com/2026/01/05/2025-enflasyonu-tuik-yuzde-3089-enag-ise-yuzde-5614-acikladi) | **77.01** | **70.29** | **51.52** |
| **Jan 2026** | +1.16% | [Link](https://www.tcmb.gov.tr/kurlar/202601/30012026.xml) | 4.84% | [TÜİK 58293](https://veriportali.tuik.gov.tr/tr/press/58293) | 4.56% | 6.32% | [?ENAG](https://tr.euronews.com/2026/02/03/ocakta-yillik-enflasyon-tuik-yuzde-3065-enag-ise-yuzde-5342-acikladi) | **74.31** | **68.00** | **49.02** |

---

### Key Takeaway
**As of January 2026, purchasing power of a fixed USD salary has dropped to:**
* **74.31%** using TÜİK (government) — a ~26% loss
* **68.00%** using İTO (Istanbul chamber of commerce) — a ~32% loss
* **49.02%** using ENAG (independent academics) — a ~51% loss

The three sources consistently rank TÜİK < İTO < ENAG in 19 out of 25 months. The truth likely falls somewhere in the İTO–ENAG range, meaning a USD earner in Turkey has lost roughly one-third to one-half of their purchasing power in just two years.
