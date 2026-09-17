import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_and_clean_data():
    """Generates the dataset using NumPy and handles null values."""
    np.random.seed(42)
    n = 250
    restaurants = ["Food Hub", "Spice Villa", "Urban Bites", "Tasty Corner", "Royal Kitchen"]
    
    df = pd.DataFrame({
        'restaurant_name': np.random.choice(restaurants, n),
        'order_value': np.random.uniform(100, 1000, n),
        'delivery_time_mins': np.random.normal(30, 10, n),
        'rating': np.random.uniform(1.0, 5.0, n),
        'distance_km': np.random.uniform(1, 15, n)
    })
    
    # Artificially inject nulls to fulfill the requirement to check/fill missing data
    null_idx1 = np.random.choice(df.index, size=10, replace=False)
    null_idx2 = np.random.choice(df.index, size=15, replace=False)
    df.loc[null_idx1, 'rating'] = np.nan
    df.loc[null_idx2, 'delivery_time_mins'] = np.nan

    # Check for and fill any null values in numeric columns with the median
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].median())
            
    return df

def summary_statistics(df):
    """Option 1: Uses NumPy statistical functions."""
    order_vals = df['order_value'].to_numpy()
    print("\n--- Summary Statistics (Powered by NumPy) ---")
    print(f"Max Order Value: Rs {np.max(order_vals):.2f}")
    print(f"Min Order Value: Rs {np.min(order_vals):.2f}")
    print(f"Mean Order Value: Rs {np.mean(order_vals):.2f}")
    print(f"Std Dev of Order Value: Rs {np.std(order_vals):.2f}")

def distribution_analysis(df):
    """Option 2: Uses Matplotlib subplots to save charts silently."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    axes[0].hist(df['delivery_time_mins'], bins=20, color='skyblue', edgecolor='black')
    axes[0].set_title('Delivery Time Distribution')
    axes[0].set_xlabel('Minutes')
    axes[0].set_ylabel('Frequency')

    axes[1].hist(df['order_value'], bins=20, color='lightgreen', edgecolor='black')
    axes[1].set_title('Order Value Distribution')
    axes[1].set_xlabel('Order Value (Rs)')
    axes[1].set_ylabel('Frequency')

    plt.tight_layout()
    # Save silently without plt.show()
    plt.savefig('distribution_analysis.png', dpi=150)
    plt.close()
    print("\n[Success] Distribution analysis saved as 'distribution_analysis.png' (150 DPI).")

def correlation_heatmap(df):
    """Option 3: Uses Seaborn to plot and save a correlation heatmap."""
    plt.figure(figsize=(8, 6))
    numeric_cols = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_cols.corr()
    
    sns.heatmap(corr_matrix, annot=True, cmap='viridis', fmt=".2f")
    plt.title('Numeric Features Correlation Heatmap')
    plt.tight_layout()
    
    plt.savefig('correlation_report.png', dpi=150)
    plt.close()
    print("\n[Success] Correlation heatmap saved as 'correlation_report.png' (150 DPI).")

def restaurant_performance(df):
    """Option 4: Uses Pandas groupby and aggregation."""
    perf = df.groupby('restaurant_name').agg({
        'order_value': 'mean',
        'delivery_time_mins': 'mean',
        'rating': 'mean'
    }).reset_index()
    
    # Format the numeric columns for cleaner console reading
    perf['order_value'] = perf['order_value'].round(2)
    perf['delivery_time_mins'] = perf['delivery_time_mins'].round(2)
    perf['rating'] = perf['rating'].round(2)
    
    print("\n--- Restaurant Performance Report (Powered by Pandas) ---")
    print(perf.to_string(index=False))

def print_exit_summary(df):
    """Calculates and prints the final plain-text summary report on exit."""
    print("\n" + "="*50)
    print("FINAL EDA SUMMARY REPORT")
    print("="*50)
    
    # 1. Top 3 restaurants by mean rating
    top_3 = df.groupby('restaurant_name')['rating'].mean().sort_values(ascending=False).head(3)
    print("\n Top 3 Restaurants by Mean Rating:")
    for rank, (name, rating) in enumerate(top_3.items(), 1):
        print(f"   {rank}. {name} (Rating: {rating:.2f})")

    # 2. Numeric column pair with the highest absolute Pearson correlation
    numeric_cols = df.select_dtypes(include=[np.number])
    corr = numeric_cols.corr().abs()
    np.fill_diagonal(corr.values, 0) # Remove self-correlation of 1.0
    highest_corr_pair = corr.unstack().idxmax()
    highest_corr_val = corr.unstack().max()
    print(f"\n Highest Correlation Pair:")
    print(f"   {highest_corr_pair[0]} & {highest_corr_pair[1]} (|r| = {highest_corr_val:.2f})")

    # 3. Overall mean and standard deviation of delivery time
    mean_time = df['delivery_time_mins'].mean()
    std_time = df['delivery_time_mins'].std()
    print(f"\n⏱  Overall Delivery Time Stats:")
    print(f"   Mean: {mean_time:.2f} mins")
    print(f"   Standard Deviation: {std_time:.2f} mins")
    print("="*50)

def main():
    print("Initializing Food Delivery Analytics Console...")
    df = generate_and_clean_data()
    print(f"Dataset generated, nulls imputed. Ready. (Shape: {df.shape})")

    while True:
        print("\n" + "-"*40)
        print("MAIN MENU")
        print("-"*40)
        print("1. Summary Statistics")
        print("2. Distribution Analysis")
        print("3. Correlation Heatmap")
        print("4. Restaurant Performance Report")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            summary_statistics(df)
        elif choice == '2':
            distribution_analysis(df)
        elif choice == '3':
            correlation_heatmap(df)
        elif choice == '4':
            restaurant_performance(df)
        elif choice == '5':
            print_exit_summary(df)
            print("\nExiting program. Have a great day!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()