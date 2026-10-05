import pandas as pd
import numpy as np

# Create sales data
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet"],
    "Quantity": [5, 10, 7, 8, 15, 6],
    "Price": [50000, 20000, 30000, 50000, 20000, 30000]
}

df = pd.DataFrame(data)

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("Sales Data:")
print(df)

print("\nTotal Sales:", np.sum(df["Total_Sales"]))
print("Average Sales:", np.mean(df["Total_Sales"]))
print("Maximum Sales:", np.max(df["Total_Sales"]))
print("Minimum Sales:", np.min(df["Total_Sales"]))