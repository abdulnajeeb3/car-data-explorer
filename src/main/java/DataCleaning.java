import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class DataCleaning {

    public static void cleanData(String inputFile, String outputFile) {
        try (CSVReader reader = new CSVReader(new FileReader(inputFile));
             CSVWriter writer = new CSVWriter(new FileWriter(outputFile))) {

            List<String[]> allData = reader.readAll();
            List<String[]> cleanedData = new ArrayList<>();

            for (String[] row : allData) {
                boolean valid = true;
                for (String value : row) {
                    if (value == null || value.trim().isEmpty()) {
                        valid = false;
                        break;
                    }
                }
                if (valid) {
                    cleanedData.add(row);
                }
            }

            writer.writeAll(cleanedData);
            System.out.println("Cleaned data saved to " + outputFile);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
