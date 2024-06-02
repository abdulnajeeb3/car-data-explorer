import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    
    # Box plot of prices by car brand
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Brand', y='Price', data=df)
    plt.xticks(rotation=90)
    plt.title('Car Prices by Brand')
    plt.xlabel('Brand')
    plt.ylabel('Price')
    plt.savefig('output/price_by_brand.png')
    plt.close()
    
    # Bar chart of the number of cars by fuel type
    plt.figure(figsize=(10, 6))
    df['Fuel_Type'].value_counts().plot(kind='bar')
    plt.title('Number of Cars by Fuel Type')
    plt.xlabel('Fuel Type')
    plt.ylabel('Number of Cars')
    plt.savefig('output/cars_by_fuel_type.png')
    plt.close()
    
    # Pie chart of the proportion of cars by transmission type
    plt.figure(figsize=(8, 8))
    df['Transmission'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title('Proportion of Cars by Transmission Type')
    plt.ylabel('')
    plt.savefig('output/cars_by_transmission_type.png')
    plt.close()
    
    # Heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.savefig('output/correlation_matrix.png')
    plt.close()
    
    print("Visualizations saved to output/")

def heatmap():
    print("Awesome function heatmap")
