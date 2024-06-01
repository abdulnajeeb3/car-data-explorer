import com.opencsv.CSVReader;

import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DataAnalysis {

    public static void analyzeData(String inputFile) {
        try (CSVReader reader = new CSVReader(new FileReader(inputFile))) {

            List<String[]> allData = reader.readAll();
            Map<String, Double> priceByYear = new HashMap<>();

            double totalPrice = 0;
            int count = 0;

            for (String[] row : allData) {
                String year = row[1];
                double price = Double.parseDouble(row[2]);

                priceByYear.merge(year, price, Double::sum);

                totalPrice += price;
                count++;
            }

            double averagePrice = totalPrice / count;

            System.out.println("Summary Statistics:");
            System.out.println("Average Price: " + averagePrice);

            System.out.println("\nAverage Price by Year:");
            for (Map.Entry<String, Double> entry : priceByYear.entrySet()) {
                System.out.println(entry.getKey() + ": " + entry.getValue() / count);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
