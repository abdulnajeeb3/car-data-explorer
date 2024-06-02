import pandas as pd

def load_data(file_path):
    """
    Loads data from the specified CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: Loaded data as a pandas DataFrame.
    """
    return pd.read_csv(file_path)

def analyze_data(df):
    """
    Analyzes the DataFrame to generate summary statistics and identify trends.

    Parameters:
    df (DataFrame): The DataFrame to be analyzed.

    Returns:
    None. Prints summary statistics and trends.
    """
    summary = df.describe()  # Generate summary statistics
    print("Summary Statistics:\n", summary)
    
    avg_price_by_year = df.groupby('Year')['Price'].mean()
    print("\nAverage Price by Year:\n", avg_price_by_year)

def calculate_median(df):
    """
    Calculates the median values for the DataFrame.

    Parameters:
    df (DataFrame): The DataFrame for which to calculate median values.

    Returns:
    Series: Median values of the DataFrame.
    """
    median_values = df.median()
    print("\nMedian Values:\n", median_values)
    return median_values

def calculate_mode(df):
    """
    Calculates the mode values for the DataFrame.

    Parameters:
    df (DataFrame): The DataFrame for which to calculate mode values.

    Returns:
    DataFrame: Mode values of the DataFrame.
    """
    mode_values = df.mode().iloc[0]
    print("\nMode Values:\n", mode_values)
    return mode_values

def correlation_analysis(df):
    """
    Performs correlation analysis on the DataFrame.

    Parameters:
    df (DataFrame): The DataFrame for which to perform correlation analysis.

    Returns:
    DataFrame: Correlation matrix of the DataFrame.
    """
    correlation_matrix = df.corr()
    print("\nCorrelation Matrix:\n", correlation_matrix)
    return correlation_matrix

if __name__ == "__main__":
    df = load_data('data/cleaned_cars.csv')
    analyze_data(df)
    calculate_median(df)
    calculate_mode(df)
    correlation_analysis(df)
