import pandas as pd
import os

df = pd.read_csv("data/raw/sales.csv")

# Normalize column names (THIS FIXES THE ERROR)
df.columns = df.columns.str.strip().str.replace(" ", "_")

os.makedirs("data/processed", exist_ok=True)

# Profit by Category
profit_by_category = (
    df.groupby("Category")["Profit"]
    .sum()
    .reset_index()
)

profit_by_category.to_csv(
    "data/processed/profit_by_category.csv",
    index=False
)

# Loss-making Products
loss_products = (
    df.groupby("Product_Name")["Profit"]
    .sum()
    .reset_index()
)

loss_products = loss_products[loss_products["Profit"] < 0]

loss_products.to_csv(
    "data/processed/loss_products.csv",
    index=False
)

# Monthly Sales
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order_Date"] = monthly_sales["Order_Date"].astype(str)

monthly_sales.to_csv(
    "data/processed/monthly_sales.csv",
    index=False
)
print("EDA script executed successfully")
