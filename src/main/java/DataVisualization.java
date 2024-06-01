import com.opencsv.CSVReader;
import org.knowm.xchart.CategoryChart;
import org.knowm.xchart.CategoryChartBuilder;
import org.knowm.xchart.XChartPanel;
import org.knowm.xchart.style.Styler;

import javax.swing.*;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DataVisualization {

    public static void visualizeData(String inputFile) {
        try (CSVReader reader = new CSVReader(new FileReader(inputFile))) {

            List<String[]> allData = reader.readAll();
            Map<String, Double> priceByYear = new HashMap<>();

            for (String[] row : allData) {
                String year = row[1];
                double price = Double.parseDouble(row[2]);

                priceByYear.merge(year, price, Double::sum);
            }

            CategoryChart chart = new CategoryChartBuilder().width(800).height(600).title("Average Price by Year").xAxisTitle("Year").yAxisTitle("Price").build();

            chart.getStyler().setLegendPosition(Styler.LegendPosition.InsideNW);
            chart.getStyler().setHasAnnotations(true);

            chart.addSeries("Price", priceByYear.keySet(), priceByYear.values());

            SwingUtilities.invokeLater(() -> {
                JFrame frame = new JFrame("XChart Example");
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.add(new XChartPanel<>(chart));
                frame.pack();
                frame.setVisible(true);
            });

            System.out.println("Visualizations generated.");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
