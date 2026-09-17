import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Dataset Generation ---
np.random.seed(7)
num_rows = 200

df = pd.DataFrame({
    'order_value': np.random.uniform(100, 800, num_rows),
    'distance_km': np.random.uniform(1, 20, num_rows),
    'delivery_time_mins': np.random.normal(30, 8, num_rows),
    'rating': np.random.uniform(1.0, 5.0, num_rows),
    'discount_pct': np.random.uniform(0, 30, num_rows)
})

# --- 2. Introduce & Impute Null Values ---
# Calculate 5% of rows (10 rows out of 200)
null_count = int(0.05 * num_rows)

# Randomly select indices for nulls using np.random.choice
null_idx_time = np.random.choice(df.index, size=null_count, replace=False)
null_idx_rating = np.random.choice(df.index, size=null_count, replace=False)

# Apply NaNs to the selected indices
df.loc[null_idx_time, 'delivery_time_mins'] = np.nan
df.loc[null_idx_rating, 'rating'] = np.nan

# Fill NaNs with the respective column medians
df['delivery_time_mins'] = df['delivery_time_mins'].fillna(df['delivery_time_mins'].median())
df['rating'] = df['rating'].fillna(df['rating'].median())

# --- 3. Feature Engineering & Categorization ---
# Add derived column for delivery speed (km/h)
df['delivery_speed_kmph'] = df['distance_km'] / (df['delivery_time_mins'] / 60)

# Classify into 3 equal-frequency bins using qcut
# qcut bins from lowest to highest, so labels map to lowest speeds up to highest speeds
df['speed_band'] = pd.qcut(df['delivery_speed_kmph'], q=3, labels=['slow', 'Normal', 'Fast'])

# --- 4. Seaborn Visualizations ---
# 4a. Correlation Heatmap
plt.figure(figsize=(10, 8))
numeric_cols = df.select_dtypes(include=[np.number])
corr_matrix = numeric_cols.corr(method='pearson')

# Plot heatmap with annotations and a diverging color palette (coolwarm)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Pearson Correlation Heatmap")
plt.tight_layout()

# Save at DPI >= 150
plt.savefig('correlation_heatmap.png', dpi=150)
plt.close() # Close to prevent overlap with the next plot

# 4b. Pairplot
# Select specific columns + speed_band for hue
cols_to_plot = ['order_value', 'distance_km', 'delivery_time_mins', 'rating', 'speed_band']

# Create pairplot colored by speed_band
pairplot_fig = sns.pairplot(df[cols_to_plot], hue='speed_band', palette='viridis')

# Save the pairplot figure at DPI >= 150
pairplot_fig.savefig('pairplot.png', dpi=150)
plt.close()

print("Task 4 Execution Complete: Dataset generated, cleaned, and charts saved.")