import pandas as pd
import numpy as np

data = {
    "Customer": ["A", "B", "C", "D", "E"],
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
    "Quantity": [2, 5, 3, 4, 6],
    "Price": [50000, 20000, 30000, 50000, 20000]
}

df = pd.DataFrame(data)

# Calculate sales
df["Sales"] = df["Quantity"] * df["Price"]

print("Customer Sales Data:")
print(df)

# Customer with highest sales
highest_customer = df.loc[df["Sales"].idxmax(), "Customer"]

print("\nTotal Sales:", np.sum(df["Sales"]))
print("Average Sales:", np.mean(df["Sales"]))
print("Highest Sales:", np.max(df["Sales"]))
print("Top Customer:", highest_customer)

# Product summary
summary = df.groupby("Product")["Sales"].sum()

print("\nProduct-wise Sales:")
print(summary)