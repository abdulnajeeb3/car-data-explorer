import pandas as pd

def analyze_data(input_file):
    df = pd.read_csv(input_file)
    
    # Summary statistics
    summary = df.describe()
    print("Summary Statistics:")
    print(summary)
    
    # Trend analysis (example: average price by year)
    avg_price_by_year = df.groupby('Year')['Price'].mean()
    print("\nAverage Price by Year:")
    print(avg_price_by_year)

if __name__ == "__main__":
    analyze_data('data/cleaned_cars.csv')
