import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

months = np.arange(1, 13)

# Generate monthly data
orders = np.random.randint(1000, 5001, 12)
avg_order_value = np.random.uniform(200, 400, 12)
revenue = orders * avg_order_value
delivery_time = np.random.normal(28, 4, 12)

fig, axes = plt.subplots(3, 1, figsize=(10, 12))

# Subplot 1: Line chart for total orders
axes[0].plot(months, orders, marker='o', linestyle='-', color='blue')

# Annotate each data point with its value just above the marker
for i in range(len(months)):
    axes[0].annotate(str(orders[i]), 
                     (months[i], orders[i]), 
                     textcoords="offset points", 
                     xytext=(0, 10), # Shifts the text 10 points vertically
                     ha='center')    # Centers the text over the marker

# Adding titles and labels for good measure
axes[0].set_title("Monthly Total Orders")
axes[0].set_xlabel("Month (1-12)")
axes[0].set_ylabel("Number of Orders")

bar_colors = ['green' if value > 800000 else 'red' for value in revenue]

axes[1].bar(months, revenue, color=bar_colors)
axes[1].axhline(800000, linestyle='--')

axes[1].set_title("Monthly Revenue")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Revenue (₹)")

# Subplot 3: Histogram of delivery times
delivery_times_500 = np.random.normal(
    np.mean(delivery_time),
    np.std(delivery_time),
    500
)

axes[2].hist(delivery_times_500, bins=15)

mean_delivery = np.mean(delivery_times_500)

axes[2].axvline(mean_delivery, linestyle='--', label='Mean')
axes[2].set_title("Delivery Time Distribution")
axes[2].set_xlabel("Delivery Time (minutes)")
axes[2].set_ylabel("Frequency")
axes[2].legend()

plt.suptitle("Food Delivery Monthly Dashboard")
plt.tight_layout()
plt.savefig("food_delivery_dashboard.png", dpi=150)
plt.show()