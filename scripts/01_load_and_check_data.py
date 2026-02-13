import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# File path
FILE_PATH = BASE_DIR / "data" / "processed" / "sales_cleaned.csv"

# Load data
df = pd.read_csv(FILE_PATH)

# Ensure date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Basic checks
print("Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# Monthly sales aggregation
monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"]
    .sum()
)

# Plot
plt.figure()
monthly_sales.plot(title="Monthly Sales Trend")
plt.xlabel("Order Date")
plt.ylabel("Sales")
plt.tight_layout()

# SAVE graph (important)
output_image = BASE_DIR / "data" / "processed" / "monthly_sales_trend.png"
plt.savefig(output_image)
#plt.show()

print("Graph saved at:", output_image)
print("=== 01_load_and_check_data.py COMPLETED ===")
