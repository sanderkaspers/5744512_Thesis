"""
This script analyzes and visualizes mutation testing results from 3 reruns of the 'cot' experiment.
It loads data from three CSVs ('appendix_metrics_table_cotF.csv', 'appendix_metrics_table_cot1.csv', 'appendix_metrics_table_cot2.csv')
and generates main/appendix visuals using the *mean per program* (over all present runs).

"""

# IMPORTS
import os
import pandas as pd  # For DataFrame operations.
import matplotlib.pyplot as plt  # For plots.
import matplotlib.patches as mpatches
import numpy as np
from scipy.stats import gaussian_kde
import random

# PATHS
base_dir = "results"
cot_plots_path = os.path.join(base_dir, 'plots_cot')
metrics_tables_csvs = [
    os.path.join(base_dir, "cot1", "appendix_metrics_table_cot1.csv"),
    os.path.join(base_dir, "cot2", "appendix_metrics_table_cot2.csv"),
    os.path.join(base_dir, "cot", "appendix_metrics_table_cot.csv")
]

# GLOBAL VARIABLES
random.seed(3)
png_ext = ".png"
classification_color_map = {
    "Well tested": 'lightblue',
    "Near-miss": 'yellow',
    "Partial": 'orange',
    "Catastrophic": 'red'
}
pie_colors = ['lightblue', 'yellow', 'orange', 'red']

# CREATE DIRECTORY FOR PLOTS
if not os.path.exists(cot_plots_path):
    try:
        os.makedirs(cot_plots_path)
        print("Directory created:", cot_plots_path)
    except Exception as plot_folder_error:
        print("Could not create folder:", cot_plots_path, "\nError:", plot_folder_error)
else:
    print("Directory already exists:", cot_plots_path)

# DATA LOAD
print("Loading all metrics table CSVs (no YAML/JSON)...")
dfs = []
for csv in metrics_tables_csvs:
    try:
        df = pd.read_csv(csv, sep=';')
        df["Source"] = os.path.basename(csv)
        dfs.append(df)
        print("CSV loaded successfully:", csv)
    except Exception as errcsv:
        print("Error reading CSV:", csv)
        print(errcsv)
        continue

if len(dfs) == 0:
    print("No data loaded! Exiting script.")
    exit()

# Concatenate all runs, standardize columns
all_data = pd.concat(dfs, ignore_index=True)
if "Program" in all_data.columns:
    all_data["Program"] = all_data["Program"].astype(str).apply(lambda x: x.replace(".py", ""))
else:
    print("No 'Program' column found in merged data.")

# Ensure numeric columns
for colname in ["Mutation Score", "Num Mutants", "Assertion Count", "Statement Coverage (%)", "Test Time (s)", "Test Suite Size"]:
    if colname in all_data.columns:
        try:
            all_data[colname] = pd.to_numeric(all_data[colname], errors='coerce')
        except Exception as errcast:
            print("Could not cast column to numeric:", colname, errcast)

# Add 'Test Suite Size' from fallback cols if missing
if "Test Suite Size" not in all_data.columns:
    for fallback in ["Suite Size", "Test Count"]:
        if fallback in all_data.columns:
            all_data["Test Suite Size"] = all_data[fallback]
            print(f"Test Suite Size set from {fallback}")
            break
    else:
        all_data["Test Suite Size"] = np.nan

# AGGREGATE MEANS PER PROGRAM
# Group by Program, compute means for all relevant metrics
agg_data = all_data.groupby("Program", as_index=False).agg({
    "Mutation Score": "mean",
    "Statement Coverage (%)": "mean",
    "Assertion Count": "mean",
    "Test Time (s)": "mean",
    "Test Suite Size": "mean"
})

# Split class assignment
def detailed_split(mscore):
    try:
        if pd.isnull(mscore):
            return "Unknown"
        if mscore == 0:
            return "Catastrophic"
        if mscore >= 1 and mscore < 61:
            return "Partial"
        if mscore >= 61 and mscore < 80:
            return "Near-miss"
        if mscore >= 80:
            return "Well tested"
        return "Unknown"
    except:
        return "Unknown"

agg_data["Detailed Classification"] = agg_data["Mutation Score"].apply(detailed_split)

# MAIN PLOTS (plots 1, 2, 4, 7, 8, 10, 12, 14)

print("Generating selected plots for aggregated rerun analysis...")

# PLOT 1: Pie Chart - Distribution of Classification Labels
print("PLOT 1: Pie Chart - Distribution of Classification Labels (3-run aggregated means)")
if "Detailed Classification" in agg_data.columns:
    class_order = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    color_map = classification_color_map
    class_counter = agg_data["Detailed Classification"].value_counts().to_dict()
    values = [class_counter.get(c, 0) for c in class_order]
    pie_colors = [color_map[c] for c in class_order]
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=class_order, autopct="%1.1f%%", startangle=140, colors=pie_colors)
    legend_handles = [mpatches.Patch(color=color_map[cat], label=cat) for cat in class_order]
    plt.legend(handles=legend_handles, loc='best')
    plt.title("PLOT 1: Distribution of Classification Labels (mean per program, 3 runs)")
    plt.tight_layout()
    plt.savefig(os.path.join(cot_plots_path, "plot1_pie_mean.png"))
    plt.close()
    print("Pie plot saved as plot1_pie_mean.png")
else:
    print("Detailed Classification column not found.")

# PLOT 2: Boxplot of Mutation Scores
print("PLOT 2: Boxplot of Mean Mutation Scores (per program, aggregated 3 runs)")
if "Mutation Score" in agg_data.columns:
    mut_hist_list2 = agg_data["Mutation Score"].dropna().tolist()
    plt.figure(figsize=(8, 6))
    plt.boxplot(
        mut_hist_list2,
        vert=True,
        widths=0.35,
        patch_artist=True,
        boxprops=dict(facecolor='lightblue', edgecolor='black', linewidth=1),
        medianprops=dict(color='yellow', linewidth=1.5),
        whiskerprops=dict(color='black', linewidth=1),
        capprops=dict(color='black', linewidth=1),
        flierprops=dict(
            markerfacecolor='yellow', marker='o', markersize=5,
            linestyle='none', markeredgecolor='black'
        ),
        whis=1.5
    )
    plt.title("PLOT 2: Boxplot of Mean Mutation Scores (3-run mean per program)")
    plt.ylabel("Mean Mutation Score (%)")
    plt.tight_layout()
    plt.savefig(os.path.join(cot_plots_path, "plot2_boxplot_mean.png"))
    plt.close()
    print("Boxplot done (plot2_boxplot_mean.png)")

# PLOT 4: Enhanced Classification Barplot
print("PLOT 4: Enhanced Classification Barplot (class split, mean per program, aggregated 3 runs)")
plt.figure(figsize=(12, 7))
if "Detailed Classification" in agg_data.columns:
    cat_order = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    color_map = classification_color_map
    counts = []
    for cat in cat_order:
        cnt = sum(agg_data["Detailed Classification"] == cat)
        counts.append(cnt)
    colors = [color_map[cat] for cat in cat_order]
    bars = plt.bar(cat_order, counts, color=colors)
    for i, val in enumerate(counts):
        plt.text(i, val + 0.25, f'n={val}', ha='center', fontsize=12)
    legend_handles = [mpatches.Patch(color=color_map[cat], label=cat) for cat in cat_order]
    plt.legend(handles=legend_handles, loc='upper right')
else:
    print("Detailed Classification column not found for barplot.")
plt.ylabel("Number of Programs")
plt.xlabel("Test Classification")
plt.title("PLOT 4: Distribution per Test Classification (mean per program, 3 runs)")
plt.tight_layout()
plt.savefig(os.path.join(cot_plots_path, "plot4_barplot_mean.png"))
plt.close()
print("PLOT 4 saved as plot4_classification_barplot_mean.png")

# PLOT 7: Scatterplot Mutation Score vs Statement Coverage
print("PLOT 7: Scatterplot Mean Mutation Score vs Mean Statement Coverage (per program, aggregated 3 runs)")
plt.figure(figsize=(10, 7))
if "Statement Coverage (%)" in agg_data.columns and "Mutation Score" in agg_data.columns:
    xvals = agg_data["Statement Coverage (%)"]
    yvals = agg_data["Mutation Score"]
    class_col = agg_data["Detailed Classification"] if "Detailed Classification" in agg_data.columns else None
    color_map = classification_color_map
    scatter_colors = [color_map.get(str(v), "grey") for v in class_col]
    plt.scatter(xvals, yvals, c=scatter_colors, alpha=0.8)
    if len(xvals.dropna()) > 2:
        m, b = np.polyfit(xvals.dropna(), yvals.dropna(), 1)
        plt.plot(xvals, m * xvals + b, color='grey', linestyle='dashed')
        corr = np.corrcoef(xvals.dropna(), yvals.dropna())[0, 1]
        plt.title(f"PLOT 7: Mean Mutation Score vs Mean Statement Coverage (Pearson R={corr:.2f})")
    else:
        plt.title("PLOT 7: Mean Mutation Score vs Mean Statement Coverage (3 runs, mean per program)")
    plt.xlabel("Mean Statement Coverage (%)")
    plt.ylabel("Mean Mutation Score (%)")
    legend_elements = [mpatches.Patch(color=color_map[cat], label=cat) for cat in color_map]
    plt.legend(handles=legend_elements)
    plt.tight_layout()
    plt.savefig(os.path.join(cot_plots_path, "plot7_mean_mutscore_vs_mean_coverage.png"))
    plt.close()
    print("PLOT 7 saved as plot7_mean_mutscore_vs_mean_coverage.png")

# PLOT 8: Scatterplot Mutation Score vs Assertion Count
print("PLOT 8: Scatterplot Mean Mutation Score vs Mean Assertion Count (per program, aggregated 3 runs)")
plt.figure(figsize=(10, 7))
if "Assertion Count" in agg_data.columns and "Mutation Score" in agg_data.columns:
    xvals = agg_data["Assertion Count"]
    yvals = agg_data["Mutation Score"]
    class_col = agg_data["Detailed Classification"] if "Detailed Classification" in agg_data.columns else None
    color_map = classification_color_map
    scatter_colors = [color_map.get(str(v), "grey") for v in class_col]
    plt.scatter(xvals, yvals, c=scatter_colors, alpha=0.8)
    plt.xlabel("Mean Assertion Count")
    plt.ylabel("Mean Mutation Score (%)")
    plt.title("PLOT 8: Mean Mutation Score vs Mean Assertion Count (per program, 3 runs)")
    legend_elements = [mpatches.Patch(color=color_map[cat], label=cat) for cat in color_map]
    plt.legend(handles=legend_elements)
    plt.tight_layout()
    plt.savefig(os.path.join(cot_plots_path, "plot8_mean_mutscore_vs_mean_assertioncount.png"))
    plt.close()
    print("PLOT 8 saved as plot8_mean_mutscore_vs_mean_assertioncount.png")

# PLOT 10: Scatterplot Mutation Score vs Test Suite Size
print("PLOT 10: Scatterplot Mean Mutation Score vs Mean Test Suite Size (per program, aggregated 3 runs)")
plt.figure(figsize=(10, 7))
if "Test Suite Size" in agg_data.columns and "Mutation Score" in agg_data.columns:
    xvals = agg_data["Test Suite Size"]
    yvals = agg_data["Mutation Score"]
    class_col = agg_data["Detailed Classification"] if "Detailed Classification" in agg_data.columns else None
    color_map = classification_color_map
    scatter_colors = [color_map.get(str(v), "grey") for v in class_col]
    plt.scatter(xvals, yvals, c=scatter_colors, alpha=0.8)
    plt.xlabel("Mean Test Suite Size")
    plt.ylabel("Mean Mutation Score (%)")
    plt.title("PLOT 10: Mean Mutation Score vs Mean Test Suite Size (per program, 3 runs)")
    legend_elements = [mpatches.Patch(color=color_map[cat], label=cat) for cat in color_map]
    plt.legend(handles=legend_elements)
    plt.tight_layout()
    plt.savefig(os.path.join(cot_plots_path, "plot10_mean_mutscore_vs_mean_suitesize.png"))
    plt.close()
    print("PLOT 10 saved as plot10_mean_mutscore_vs_mean_suitesize.png")

# PLOT 12: Boxplot Mean Assertion Count by Class
print("PLOT 12: Boxplot Mean Assertion Count by Class (aggregated, mean per program, 3 runs)")
plt.figure(figsize=(8, 7))
if "Assertion Count" in agg_data.columns and "Detailed Classification" in agg_data.columns:
    classes = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    data = []
    for c in classes:
        data.append(agg_data[agg_data["Detailed Classification"]==c]["Assertion Count"].dropna())
    plt.boxplot(
        data,
        labels=classes,
        patch_artist=True,
        boxprops=dict(facecolor='yellow', edgecolor='black'),
        medianprops=dict(color='orange')
    )
    plt.ylabel("Mean Assertion Count")
    plt.title("PLOT 12: Mean Assertion Count by Test Class (per program, 3 runs)")
    plt.tight_layout()
    plt.savefig(os.path.join(cot_plots_path, "plot12_mean_assertioncount.png"))
    plt.close()
    print("PLOT 12 saved as plot12_mean_assertioncount.png")
else:
    print("Required columns for Plot 12 not found.")

# PLOT 14: Boxplot Mean Total Time by Class
print("PLOT 14: Boxplot Mean Total Time by Test Class (aggregated, mean per program, 3 runs)")
plt.figure(figsize=(8, 7))
if "Test Time (s)" in agg_data.columns and "Detailed Classification" in agg_data.columns:
    classes = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    data = []
    for c in classes:
        data.append(agg_data[agg_data["Detailed Classification"]==c]["Test Time (s)"].dropna())
    plt.boxplot(
        data,
        labels=classes,
        patch_artist=True,
        boxprops=dict(facecolor='grey', edgecolor='black'),
        medianprops=dict(color='black')
    )
    plt.ylabel("Mean Test Time (s)")
    plt.title("PLOT 14: Mean Total Time by Test Class (per program, 3 runs)")
    plt.tight_layout()
    plt.savefig(os.path.join(cot_plots_path, "plot14_mean_totaltime.png"))
    plt.close()
    print("PLOT 14 saved as plot14_mean_totaltime.png")
else:
    print("Required columns for Plot 14 not found.")

print("All selected plots saved in folder:", cot_plots_path)


