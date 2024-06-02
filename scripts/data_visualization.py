import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(input_file):
    df = pd.read_csv(input_file)
    
    # Histogram of car prices
    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=30, edgecolor='k')
    plt.title('Distribution of Car Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.savefig('output/price_distribution.png')
    plt.close()
    
    # Scatter plot of price vs mileage
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Mileage'], df['Price'], alpha=0.5)
    plt.title('Price vs Mileage')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.savefig('output/price_vs_mileage.png')
    plt.close()
    
    # Line chart of average price by year
    avg_price_by_year = df.groupby('Year')['Price'].mean()
    plt.figure(figsize=(10, 6))
    avg_price_by_year.plot(kind='line')
    plt.title('Average Price by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Price')
    plt.savefig('output/avg_price_by_year.png')
    plt.close()
    
    print("Visualizations saved to output/")

if __name__ == "__main__":
    visualize_data('data/cleaned_cars.csv')
