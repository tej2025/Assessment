import pandas as pd
import numpy as np

# --- 1. DATASET SETUP ---
np.random.seed(42)

restaurants = ["Food Hub", "Spice Villa", "Urban Bites", "Tasty Corner", "Royal Kitchen"]
cities = ["Ahmedabad", "Surat", "Vadodara"]
cuisines = ["Indian", "Chinese", "Fast Food"]

df = pd.DataFrame({
    "restaurant_name": np.random.choice(restaurants, 40),
    "city": np.random.choice(cities, 40),
    "order_value": np.random.randint(200, 1000, 40),
    "delivery_time_mins": np.random.randint(25, 40, 40),
    "rating": np.round(np.random.uniform(3.5, 5.0, 40), 1),
    "cuisine_type": np.random.choice(cuisines, 40)
})

# --- 2. GROUPING & AGGREGATION ---
# Use a single method chain for groupby and agg
grouped_df = df.groupby('restaurant_name').agg({
    'order_value': 'mean',
    'delivery_time_mins': 'mean',
    'rating': 'mean'
})

# --- 3. FILTERING ---
# Retain restaurants with mean rating > 4.0 and mean delivery time < 35 mins
filtered_df = grouped_df[
    (grouped_df['rating'] > 4.0) & 
    (grouped_df['delivery_time_mins'] < 35.0)
]

# --- 4. SORTING & OUTPUT ---
# Sort by mean order value descending and reset index
final_df = filtered_df.sort_values(by='order_value', ascending=False).reset_index()

# Print the complete result with column headers
print("--- Ranked Restaurant Summary ---")
print(final_df)