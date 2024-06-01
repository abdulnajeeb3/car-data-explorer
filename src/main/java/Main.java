public class Main {

    public static void main(String[] args) {
        String rawData = "data/cars.csv";
        String cleanedData = "data/cleaned_cars.csv";

        DataCleaning.cleanData(rawData, cleanedData);
        DataAnalysis.analyzeData(cleanedData);
        DataVisualization.visualizeData(cleanedData);
    }
}
