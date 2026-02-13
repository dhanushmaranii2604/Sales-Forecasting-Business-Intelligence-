import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
processed_dir = Path("data/processed")
input_path = processed_dir / "sales_cleaned.csv"
output_path = processed_dir / "sales_forecast.csv"

# Load cleaned data
df = pd.read_csv(input_path)

# Ensure date column is datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Monthly sales aggregation
monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order_Date"] = monthly_sales["Order_Date"].astype(str)

# Simple forecast (moving average)
window_size = 3
monthly_sales["Forecast"] = (
    monthly_sales["Sales"]
    .rolling(window=window_size)
    .mean()
)

# Save forecast data
monthly_sales.to_csv(output_path, index=False)

# Plot
plt.figure()
plt.plot(monthly_sales["Sales"], label="Actual Sales")
plt.plot(monthly_sales["Forecast"], linestyle="--", label="Forecast")
plt.legend()
plt.tight_layout()
plt.show()

print("=== 04_forecasting.py COMPLETED ===")
