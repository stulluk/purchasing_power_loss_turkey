import csv
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
DATA_CSV = ROOT / "purchasing_power_data.csv"
CHARTS_DIR = ROOT / "charts"


def load_data():
    dates = []
    usdtry = []
    pp_tuik = []
    pp_ito = []
    pp_enag = []
    enag_mom = []

    with DATA_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dates.append(row["Month"])
            usdtry.append(float(row["TCMB ForexSelling"]))
            pp_tuik.append(float(row["PP (TUIK)"]))
            pp_ito.append(float(row["PP (ITO)"]))
            pp_enag.append(float(row["PP (ENAG)"]))
            raw_enag = (row.get("ENAG MoM %") or "").strip()
            enag_mom.append(float(raw_enag) if raw_enag else 0.0)

    return {
        "dates": dates,
        "usdtry": usdtry,
        "pp_tuik": pp_tuik,
        "pp_ito": pp_ito,
        "pp_enag": pp_enag,
        "enag_mom": enag_mom,
    }


def normalise_to_index(series):
    if not series:
        return []
    base = series[0]
    return [value / base * 100.0 for value in series]


def build_cost_of_living_index(enag_mom):
    """Build a simple cost-of-living index from ENAG MoM percentages."""
    index_values = []
    value = 100.0
    for pct in enag_mom:
        value *= 1.0 + pct / 100.0
        index_values.append(value)
    return index_values


def chart_purchasing_power_indices(data):
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    dates = data["dates"]
    pp_tuik = data["pp_tuik"]
    pp_ito = data["pp_ito"]
    pp_enag = data["pp_enag"]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, pp_tuik, label="PP (TÜİK)", color="#1f77b4", linewidth=2)
    plt.plot(dates, pp_ito, label="PP (İTO)", color="#ff7f0e", linewidth=2)
    plt.plot(dates, pp_enag, label="PP (ENAG)", color="#d62728", linewidth=2)
    plt.axhline(100, color="#888888", linestyle="--", linewidth=1, label="Dec 2023 baseline = 100")

    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Purchasing Power Index (Dec 2023 = 100)")
    plt.title("Purchasing Power of a Fixed USD Salary in Turkey (TÜİK, İTO, ENAG)")
    plt.grid(True, linestyle=":", alpha=0.4)
    plt.legend()
    plt.tight_layout()

    output_path = CHARTS_DIR / "purchasing-power-indices.png"
    plt.savefig(output_path, dpi=200)
    plt.close()
    return output_path


def chart_usdtry_vs_cost_of_living(data):
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    dates = data["dates"]
    usdtry = data["usdtry"]
    enag_mom = data["enag_mom"]

    usd_index = normalise_to_index(usdtry)
    lci_index = build_cost_of_living_index(enag_mom)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, usd_index, label="USD/TRY (Index, Dec 2023 = 100)", color="#2ca02c", linewidth=2)
    plt.plot(dates, lci_index, label="Cost of Living (ENAG-based Index)", color="#d62728", linewidth=2)

    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Index (Dec 2023 = 100)")
    plt.title("USD/TRY vs. ENAG Cost of Living Index")
    plt.grid(True, linestyle=":", alpha=0.4)
    plt.legend()
    plt.tight_layout()

    output_path = CHARTS_DIR / "usdtry-vs-enag-cost-of-living.png"
    plt.savefig(output_path, dpi=200)
    plt.close()
    return output_path


def chart_mercer_turkey_salary_increase():
    """Mercer Turkey: median full-year TL salary increase (all companies), same period as report."""
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    years = ["2023", "2024", "2025"]
    # Median full-year realised/planned increase (report section 7): 2023 ~75%, 2024 ~65%, 2025 ~40%
    pct = [75, 65, 40]
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(years, pct, color=["#1f77b4", "#ff7f0e", "#2ca02c"], edgecolor="black", linewidth=0.8)
    ax.set_ylabel("Median full-year salary increase (%)")
    ax.set_xlabel("Year")
    ax.set_title("Turkey (TL-paid): Mercer median full-year salary increase (all companies)")
    ax.set_ylim(0, max(pct) * 1.15)
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f"{int(b.get_height())}%", ha="center", fontsize=12)
    plt.tight_layout()
    output_path = CHARTS_DIR / "mercer_turkey_salary_increase_trend.png"
    plt.savefig(output_path, dpi=200)
    plt.close()
    return output_path


def main():
    data = load_data()
    chart1 = chart_purchasing_power_indices(data)
    chart2 = chart_usdtry_vs_cost_of_living(data)
    chart3 = chart_mercer_turkey_salary_increase()
    print(f"Saved charts to:\n- {chart1}\n- {chart2}\n- {chart3}")


if __name__ == "__main__":
    main()

