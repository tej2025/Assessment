import numpy as np

# Generate 25 random delivery distances
np.random.seed(42)
distances = np.random.uniform(1.0,15.0,25)

# Calculate delivery fee
fees = 20+(5*distances)

# orders where fee is greater than ₹60
mask = fees>60

print("Orders with fee greater than ₹60:")
print("Distance:", distances[mask])
print("Fee:", fees[mask])

# Statistics
print("\nStatistics:")
print("Minimum fee:", min(fees))
print("Maximum fee:", max(fees))
print("Mean fee:",np.mean(fees))
print("Standard deviation:", np.std(fees))