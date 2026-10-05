import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [45000, 52000, 48000, 65000, 70000, 62000]

plt.figure(figsize=(9, 5))

plt.plot(
    months,
    sales,
    marker="o",
    markersize=8,
    linewidth=2.5,
    color="green"
)

for month, sale in zip(months, sales):
    plt.text(
        month,
        sale + 1500,
        f"${sale:,}",
        ha="center",
        fontsize=9
    )

plt.title("Monthly Sales Trend", fontsize=16, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Sales ($)")

plt.grid(True, linestyle="--", alpha=0.5)
plt.ylim(40000, 75000)

plt.tight_layout()

plt.savefig("sales_chart.png")