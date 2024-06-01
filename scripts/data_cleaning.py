
### Scripts

#### `data_cleaning.py`
```python
import pandas as pd

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    
    # Drop rows with missing values
    df.dropna(inplace=True)
    
    # Convert data types
    df['Year'] = df['Year'].astype(int)
    df['Price'] = df['Price'].astype(float)
    df['Mileage'] = df['Mileage'].astype(float)
    
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_data('data/cars.csv', 'data/cleaned_cars.csv')
