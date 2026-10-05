import pandas as pd
import numpy as np

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [45000, 52000, 48000, 65000, 70000, 62000]
}

df = pd.DataFrame(data)

print("Monthly Sales:")
print(df)

# NumPy calculations
total = np.sum(df["Sales"])
average = np.mean(df["Sales"])
highest = np.max(df["Sales"])
lowest = np.min(df["Sales"])

print("\nTotal Sales:", total)
print("Average Sales:", average)
print("Highest Sales:", highest)
print("Lowest Sales:", lowest)

# Find best month
best_month = df.loc[df["Sales"].idxmax(), "Month"]

print("Best Sales Month:", best_month)