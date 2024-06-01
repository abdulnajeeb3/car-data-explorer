from data_cleaning import clean_data
from data_analysis import analyze_data
from data_visualization import visualize_data

def main():
    raw_data = 'data/cars.csv'
    cleaned_data = 'data/cleaned_cars.csv'
    
    clean_data(raw_data, cleaned_data)
    analyze_data(cleaned_data)
    visualize_data(cleaned_data)

if __name__ == "__main__":
    main()
