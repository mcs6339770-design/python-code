import matplotlib.pyplot as plt

# Runtime input
n = int(input("Enter number of expense categories: "))

categories = []
expenses = []

for i in range(n):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    categories.append(category)
    expenses.append(amount)

# Create dashboard
plt.figure(figsize=(12, 4))

# 1. Line Chart
plt.subplot(1, 3, 1)
plt.plot(categories, expenses, marker="o")
plt.title("Expense Trend")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)

# 2. Bar Chart
plt.subplot(1, 3, 2)
plt.bar(categories, expenses)
plt.title("Expense Comparison")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)

# 3. Pie Chart
plt.subplot(1, 3, 3)
plt.pie(expenses, labels=categories, autopct="%1.1f%%")
plt.title("Expense Distribution")

plt.tight_layout()
plt.show()