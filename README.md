# Cars Dataset 2025: Automotive Performance & Pricing Analysis

An exploratory data analysis (EDA) and visualization project examining **1,218 global automobile models** across 11 technical and pricing attributes using **Pandas, Matplotlib, Seaborn, and Plotly**.

## Dataset Overview
- **Source:** Kaggle (`Cars Datasets 2025`)
- **Size:** 1,218 vehicle records × 11 features
- **Key Attributes:** Manufacturer, Model Name, Engine Architecture, Displacement/Battery Capacity, Horsepower (`hp`), Top Speed (`km/h`), `0–100 km/h` Acceleration (`sec`), Price (`USD`), Fuel Type, Seating Capacity, and Torque (`Nm`).

## Visualizations Implemented (15 Charts)
- **Matplotlib (5 Static Charts):** Top 10 manufacturers by model count, horsepower frequency histogram, horsepower vs. top speed scatter plot, fuel type market share pie chart, and average price by seating capacity.
- **Seaborn (5 Statistical Plots):** Price spread strip plot by fuel type, horsepower boxplot across fuel types, top speed violin plot by engine configuration (`I4`, `V6`, `V8`), numerical correlation heatmap, and swarm plot comparing top 3 manufacturers.
- **Plotly (5 Interactive Web Charts):** Hover-enabled average fuel price bar chart, 4D bubble chart (Power × Speed × Price × Fuel), acceleration vs. price scatter plot, manufacturer price dispersion boxplot, and top 10 fastest cars ranking.

## Key Insights
- **Power & Speed Correlation:** Horsepower and top speed show a strong positive linear relationship, whereas horsepower and `0–100 km/h` sprint times exhibit a strong inverse correlation.
- **Right-Skewed Pricing:** Mass-market commuter vehicles cluster in accessible price brackets, while two-seater halo sports cars and hypercars create an extended upper price tail.
- **Fuel Segment Dynamics:** Petrol models dominate overall catalog volume (>70%), while Hybrid and Electric drivetrains command higher median baseline prices.

## How to Run
1. Clone this repository and navigate to the project folder.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
3. Run the analysis script (ensure Cars Datasets 2025.csv is in the same directory):
   ```bash
   python cars_analysis.py
