import pandas as pd
from pathlib import Path

# Paths
raw_dir = Path("data/raw")
processed_dir = Path("data/processed")
processed_dir.mkdir(parents=True, exist_ok=True)

INPUT_PATH = raw_dir / "sales.csv"
OUTPUT_PATH = processed_dir / "sales_cleaned.csv"

# Load data
df = pd.read_csv(INPUT_PATH)

# Basic cleaning
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Handle dates
if "Order_Date" in df.columns:
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

if "Ship_Date" in df.columns:
    df["Ship_Date"] = pd.to_datetime(df["Ship_Date"], errors="coerce")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.dropna(subset=["Sales", "Profit"])

# Save cleaned data
df.to_csv(OUTPUT_PATH, index=False)

print(f"Cleaned data saved successfully at:\n{OUTPUT_PATH}")
