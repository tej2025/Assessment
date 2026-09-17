import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

df = pd.DataFrame({
    "order_value": np.random.uniform(100, 800, 200),
    "distance_km": np.random.uniform(1, 20, 200),
    "delivery_time_mins": np.random.normal(30, 8, 200),
    "rating": np.random.uniform(1, 5, 200),
    "discount_pct": np.random.uniform(0, 30, 200),
    "cuisine_type": np.random.choice(
        ["Indian", "Chinese", "Fast Food"], 200
    )
})

# Pairplot
sns.pairplot(df, hue="cuisine_type")
plt.savefig("food_delivery_pairplot.png", dpi=200)
plt.close()

# Correlation matrix
numeric_df = df.select_dtypes(include=np.number)
corr_matrix = numeric_df.corr()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Food Delivery Pearson Correlation Heatmap")
plt.tight_layout()
plt.savefig("food_delivery_correlation_heatmap.png", dpi=200)
plt.close()

print("Pairplot and correlation heatmap created successfully.")