"""
Project: Cars Dataset 2025 - Automotive Performance & Pricing Analysis
Course: Data Visualization using Python
"""

import re
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns

# ==========================================================
# 0. DATA LOADING & PREPROCESSING (RUNS ONCE)
# ==========================================================
file_path = r"C:\Users\user\Downloads\Cars Datasets 2025.csv"
df = pd.read_csv(file_path, encoding="latin1")


def get_number(val):
  if pd.isna(val):
    return None
  clean = str(val).replace("$", "").replace(",", "").split("-")[0]
  match = re.search(r"\d+\.?\d*", clean)
  return float(match.group()) if match else None


# Convert alphanumeric strings to numbers
df["price"] = df["Cars Prices"].apply(get_number)
df["hp"] = df["HorsePower"].apply(get_number)
df["speed"] = df["Total Speed"].apply(get_number)
df["acceleration"] = df["Performance(0 - 100 )KM/H"].apply(get_number)
df["seats"] = df["Seats"].apply(get_number)

# Standardize primary fuel categories
df["fuel"] = df["Fuel Types"].replace({
    "plug in hyrbrid": "Hybrid",
    "Plug-in Hybrid": "Hybrid",
    "Petrol/Hybrid": "Hybrid",
    "Petrol, Hybrid": "Hybrid",
    "Hybrid (Petrol)": "Hybrid",
    "Hybrid/Petrol": "Hybrid",
    "Petrol (Hybrid)": "Hybrid",
    "Diesel Hybrid": "Hybrid",
    "Petrol/Diesel": "Petrol",
    "Diesel/Petrol": "Diesel",
    "Petrol, Diesel": "Petrol",
})

# Reusable subset for fuel-based plots
main_fuels = df[df["fuel"].isin(["Petrol", "Diesel", "Hybrid", "Electric"])]

print("Data loaded and cleaned successfully. Rendering charts...")

# ==========================================================
# A. MATPLOTLIB PLOTS (GRAPHS 1 TO 5)
# ==========================================================

# GRAPH 1: Bar Chart
print("Displaying Graph 1: Close window to continue...")
top_10 = df["Company Names"].value_counts().head(10)
plt.figure(figsize=(8, 4.5))
plt.bar(top_10.index, top_10.values, color="skyblue", edgecolor="black")
plt.title(
    "Top 10 Car Manufacturers by Model Count", fontsize=12, fontweight="bold"
)
plt.xlabel("Company")
plt.ylabel("Number of Models")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# GRAPH 2: Histogram
print("Displaying Graph 2: Close window to continue...")
plt.figure(figsize=(8, 4.5))
plt.hist(df["hp"].dropna(), bins=15, color="orange", edgecolor="black")
plt.title("Distribution of Vehicle Horsepower", fontsize=12, fontweight="bold")
plt.xlabel("Horsepower (hp)")
plt.ylabel("Count of Vehicles")
plt.tight_layout()
plt.show()

# GRAPH 3: Scatter Plot
print("Displaying Graph 3: Close window to continue...")
plt.figure(figsize=(8, 4.5))
plt.scatter(df["hp"], df["speed"], color="blue", alpha=0.5)
plt.title("Horsepower vs Total Speed", fontsize=12, fontweight="bold")
plt.xlabel("Horsepower (hp)")
plt.ylabel("Total Speed (km/h)")
plt.tight_layout()
plt.show()

# GRAPH 4: Pie Chart
print("Displaying Graph 4: Close window to continue...")
fuel_counts = main_fuels["fuel"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(
    fuel_counts.values,
    labels=fuel_counts.index,
    autopct="%1.1f%%",
    startangle=90,
)
plt.title("Proportion of Major Fuel Types", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.show()

# GRAPH 5: Line Chart
print("Displaying Graph 5: Close window to continue...")
seats_df = df[df["seats"].isin([2, 4, 5, 7])]
avg_price = seats_df.groupby("seats")["price"].mean()
plt.figure(figsize=(8, 4.5))
plt.plot(avg_price.index.astype(str), avg_price.values, marker="o", color="red")
plt.title(
    "Average Price Across Seating Capacities", fontsize=12, fontweight="bold"
)
plt.xlabel("Number of Seats")
plt.ylabel("Average Price (USD $)")
plt.tight_layout()
plt.show()

# ==========================================================
# B. SEABORN PLOTS (GRAPHS 6 TO 10)
# ==========================================================

# GRAPH 6: Strip Plot
print("Displaying Graph 6: Close window to continue...")
plt.figure(figsize=(8, 4.5))
sns.stripplot(data=main_fuels, x="fuel", y="price", jitter=True)
plt.ylim(0, main_fuels["price"].quantile(0.95))
plt.title("Price Spread Across Fuel Types", fontsize=12, fontweight="bold")
plt.xlabel("Fuel Type")
plt.ylabel("Price (USD $)")
plt.tight_layout()
plt.show()

# GRAPH 7: Box Plot
print("Displaying Graph 7: Close window to continue...")
plt.figure(figsize=(8, 4.5))
sns.boxplot(
    data=main_fuels,
    x="fuel",
    y="hp",
    hue="fuel",
    palette="Set2",
    showfliers=False,
)
plt.title("Horsepower by Fuel Type", fontsize=12, fontweight="bold")
plt.xlabel("Fuel Type")
plt.ylabel("Horsepower (hp)")
plt.tight_layout()
plt.show()

# GRAPH 8: Violin Plot
print("Displaying Graph 8: Close window to continue...")
sample_engines = df[df["Engines"].isin(["I4", "V6", "V8"])]
plt.figure(figsize=(8, 4.5))
sns.violinplot(data=sample_engines, x="Engines", y="speed", cut=0)
plt.title(
    "Speed Distribution Across Engine Types", fontsize=12, fontweight="bold"
)
plt.xlabel("Engine Type")
plt.ylabel("Total Speed (km/h)")
plt.tight_layout()
plt.show()

# GRAPH 9: Heatmap
print("Displaying Graph 9: Close window to continue...")
cols = ["hp", "speed", "acceleration", "seats", "price"]
corr = df[cols].corr()
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Heatmap", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.show()

# GRAPH 10: Swarm Plot
print("Displaying Graph 10: Close window to continue...")
top_3 = df[df["Company Names"].isin(["Porsche", "Volkswagen", "Nissan"])]
plt.figure(figsize=(8, 4.5))
sns.swarmplot(data=top_3, x="Company Names", y="hp", size=2.5)
plt.title("Horsepower by Top 3 Companies", fontsize=12, fontweight="bold")
plt.xlabel("Company")
plt.ylabel("Horsepower (hp)")
plt.tight_layout()
plt.show()
# ==========================================================
# C. PLOTLY PLOTS (GRAPHS 11 TO 15)
# (Opens interactive charts in your web browser)
# ==========================================================
print("Opening Plotly charts in your default browser...")

# GRAPH 11: Interactive Bar Chart
avg_price_fuel = (
    main_fuels.groupby("fuel", as_index=False)["price"].mean().round(2)
)
fig11 = px.bar(
    avg_price_fuel,
    x="fuel",
    y="price",
    color="fuel",
    title="Average Price by Fuel Type",
    labels={"fuel": "Fuel Type", "price": "Average Price (USD $)"},
)
fig11.show()

# GRAPH 12: Interactive Bubble Chart
clean_df = df.dropna(subset=["hp", "speed", "price", "fuel"]).head(200)
fig12 = px.scatter(
    clean_df,
    x="hp",
    y="speed",
    size="price",
    color="fuel",
    hover_name="Cars Names",
    title="Horsepower vs Speed (Bubble Size = Price)",
    labels={"hp": "Horsepower (hp)", "speed": "Total Speed (km/h)"},
)
fig12.show()

# GRAPH 13: Interactive Scatter Plot
acc_df = df.dropna(subset=["acceleration", "price", "fuel"])
fig13 = px.scatter(
    acc_df,
    x="acceleration",
    y="price",
    color="fuel",
    hover_name="Cars Names",
    title="Acceleration vs Price",
    labels={
        "acceleration": "0-100 KM/H Time (seconds)",
        "price": "Price (USD $)",
    },
)
fig13.show()

# GRAPH 14: Interactive Box Plot
top_brands = df[
    df["Company Names"].isin(
        ["Nissan", "Volkswagen", "Porsche", "Mazda", "Ford"]
    )
]
fig14 = px.box(
    top_brands,
    x="Company Names",
    y="price",
    color="Company Names",
    title="Price Distribution Across Top Companies",
    labels={"Company Names": "Manufacturer", "price": "Price (USD $)"},
)
fig14.show()

# GRAPH 15: Interactive Bar Chart
fastest = (
    df[["Cars Names", "Company Names", "speed", "price"]]
    .dropna()
    .sort_values(by="speed", ascending=False)
    .head(10)
)
fig15 = px.bar(
    fastest,
    x="Cars Names",
    y="speed",
    color="Company Names",
    title="Top 10 Fastest Cars",
    labels={"Cars Names": "Car Model", "speed": "Top Speed (km/h)"},
)
fig15.show()

print("All 15 plots executed successfully!")
