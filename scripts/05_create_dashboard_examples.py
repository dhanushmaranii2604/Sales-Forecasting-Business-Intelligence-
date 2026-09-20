"""Generate two lightweight SVG dashboard examples from processed project data.

Run from the repository root after the cleaning, EDA, and forecasting scripts:
    python scripts/05_create_dashboard_examples.py
"""
from pathlib import Path
import html
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
OUTPUT = ROOT / "dashbords"


def money(value: float) -> str:
    return f"${value:,.1f}K"


def write_overview() -> None:
    monthly = pd.read_csv(PROCESSED / "monthly_sales.csv")
    categories = pd.read_csv(PROCESSED / "profit_by_category.csv")
    total_sales = monthly["Sales"].sum()
    top_month = monthly.loc[monthly["Sales"].idxmax()]
    top_category = categories.loc[categories["Profit"].idxmax()]
    # The SVGs are intentionally self-contained so GitHub can preview them directly.
    # Keep the checked-in examples readable and update the headline values from data.
    source = (OUTPUT / "dashboard_overview.svg").read_text(encoding="utf-8")
    source = source.replace("$286.4K</text>", f"{html.escape(money(total_sales / 1000))}</text>", 1)
    source = source.replace("Nov 2017</text>", f"{html.escape(str(top_month['Order_Date']))}</text>", 1)
    source = source.replace("$118.4K sales", f"{money(float(top_month['Sales']) / 1000)} sales", 1)
    source = source.replace("Technology</text>", f"{html.escape(str(top_category['Category']))}</text>", 1)
    source = source.replace("$145.5K profit", f"{money(float(top_category['Profit']) / 1000)} profit", 1)
    (OUTPUT / "dashboard_overview.svg").write_text(source, encoding="utf-8")


def write_forecast() -> None:
    forecast = pd.read_csv(PROCESSED / "sales_forecast.csv")
    actual = forecast.iloc[-1]
    latest_forecast = float(forecast["Forecast"].dropna().iloc[-1])
    source = (OUTPUT / "dashboard_forecast.svg").read_text(encoding="utf-8")
    source = source.replace("$83.8K</text>", f"{money(float(actual['Sales']) / 1000)}</text>", 1)
    source = source.replace("$93.4K</text>", f"{money(latest_forecast / 1000)}</text>", 1)
    (OUTPUT / "dashboard_forecast.svg").write_text(source, encoding="utf-8")


if __name__ == "__main__":
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_overview()
    write_forecast()
    print("Dashboard examples generated in dashbords/")
