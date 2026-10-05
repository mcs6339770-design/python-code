import pandas as pd
import numpy as np

# Sales data
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet"],
    "Quantity": [5, 10, 7, 8, 15, 6],
    "Price": [50000, 20000, 30000, 50000, 20000, 30000]
}

# Create DataFrame
df = pd.DataFrame(data)

print("First 5 Records:")
print(df.head())

# Calculate Total Sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Statistical Analysis
print("\nTotal Sales:", np.sum(df["Total_Sales"]))
print("Average Sales:", np.mean(df["Total_Sales"]))
print("Highest Sale:", np.max(df["Total_Sales"]))

# Product-wise Sales
product_sales = df.groupby("Product")["Total_Sales"].sum()

print("\nProduct-wise Sales:")
print(product_sales)