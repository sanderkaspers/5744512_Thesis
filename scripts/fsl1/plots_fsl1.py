"""
This script analyzes and visualizes mutation testing results from the 'fsl1' experiment.
It loads ALL data from one CSV ('appendix_metrics_table_fsl1F.csv') and generates all required appendix and main text visuals in one run.
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
fsl1_result_path = "results/fsl1"
fsl1_plots_path = os.path.join(fsl1_result_path, 'plotss')
metrics_table_csv = os.path.join(fsl1_result_path, "appendix_metrics_table_fsl1.csv")

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
if not os.path.exists(fsl1_plots_path):
    try:
        os.makedirs(fsl1_plots_path)
        print("Directory created:", fsl1_plots_path)
    except Exception as plot_folder_error:
        print("Could not create folder:", fsl1_plots_path, "\nError:", plot_folder_error)
else:
    print("Directory already exists:", fsl1_plots_path)

# DATA LOAD
print("Loading metrics table CSV only (no YAML/JSON)...")
try:
    merged_result_data = pd.read_csv(metrics_table_csv, sep=';')
    print("CSV loaded successfully:", metrics_table_csv)
except Exception as errcsv:
    print("Error reading CSV:", metrics_table_csv)
    print(errcsv)
    merged_result_data = pd.DataFrame()

# Strip .py from Program col for safety
if "Program" in merged_result_data.columns:
    merged_result_data["Program"] = merged_result_data["Program"].astype(str)
    merged_result_data["Program"] = merged_result_data["Program"].apply(lambda x: x.replace(".py", ""))
else:
    print("No 'Program' column in merged_result_data.")

# Ensure numeric cols
for colname in ["Mutation Score", "Num Mutants", "Assertion Count", "Statement Coverage (%)", "Test Time (s)", "Test Suite Size"]:
    if colname in merged_result_data.columns:
        try:
            merged_result_data[colname] = pd.to_numeric(merged_result_data[colname], errors='coerce')
        except Exception as errcast:
            print("Could not cast column to numeric:", colname, errcast)

# Add 'Test Suite Size' from fallback cols if missing
if "Test Suite Size" not in merged_result_data.columns:
    for fallback in ["Suite Size", "Test Count"]:
        if fallback in merged_result_data.columns:
            merged_result_data["Test Suite Size"] = merged_result_data[fallback]
            print(f"Test Suite Size set from {fallback}")
            break
    else:
        merged_result_data["Test Suite Size"] = np.nan

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
if "Detailed Classification" not in merged_result_data.columns and "Mutation Score" in merged_result_data.columns:
    merged_result_data["Detailed Classification"] = merged_result_data["Mutation Score"].apply(detailed_split)
    print("Detailed classification assigned (computed).")
elif "Detailed Classification" in merged_result_data.columns:
    print("Detailed Classification found in CSV.")
else:
    merged_result_data["Detailed Classification"] = "Unknown"
    print("No Detailed Classification or Mutation Score col; using 'Unknown'.")

# Old fallback for base class
if "Classification" not in merged_result_data.columns:
    merged_result_data["Classification"] = merged_result_data["Detailed Classification"].replace(
        {"Well tested": "Well tested", "Near-miss": "Weakly tested", "Partial": "Weakly tested", "Catastrophic": "Weakly tested"}
    )

# APPENDIX & MAIN PLOTS
print("Generating all plots 1–14...")

# PLOT 1
print("PLOT 1: Pie Chart - Distribution of Classification Labels (4-way split, main text)")
if "Detailed Classification" in merged_result_data.columns:
    class_order = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    color_map = classification_color_map
    class_counter = merged_result_data["Detailed Classification"].value_counts().to_dict()
    values = [class_counter.get(c, 0) for c in class_order]
    pie_colors = [color_map[c] for c in class_order]
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=class_order, autopct="%1.1f%%", startangle=140, colors=pie_colors)
    legend_handles = [mpatches.Patch(color=color_map[cat], label=cat) for cat in class_order]
    plt.legend(handles=legend_handles, loc='best')
    plt.title("PLOT 1: Distribution of Classification Labels (4-way split, fsl1)")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl1_plots_path, "plot1_pie_fsl1.png"))
    plt.close()
    print("Pie plot saved as plot1_pie_fsl1.png")
else:
    print("Detailed Classification column not found.")

# PLOT 2
print("PLOT 2: Boxplot of Mutation Scores (fsl1)")
if "Mutation Score" in merged_result_data.columns:
    mut_hist_list2 = []
    for row in merged_result_data["Mutation Score"]:
        try:
            mut_hist_list2.append(float(row))
        except Exception:
            pass
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
    plt.title(f"PLOT 2: Boxplot of Mutation Scores (fsl1)")
    plt.ylabel("Mutation Score (%)")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl1_plots_path, "plot2_boxplot_fsl1.png"))
    plt.close()
    print("Boxplot done (plot2_boxplot_fsl1.png)")

# PLOT 3
print("PLOT 3: Histogram of Mutation Scores (fsl1)")
if "Mutation Score" in merged_result_data.columns:
    mut_hist_list = []
    for item in merged_result_data["Mutation Score"]:
        try:
            mut_hist_list.append(float(item))
        except Exception:
            pass
    plt.figure(figsize=(10, 6))
    plt.hist(mut_hist_list, bins=10, color="lightblue", edgecolor="black", alpha=0.85)
    kde = gaussian_kde(mut_hist_list)
    x_vals = np.linspace(min(mut_hist_list), max(mut_hist_list), 200)
    hist_vals, bin_edges = np.histogram(mut_hist_list, bins=10)
    bin_width = bin_edges[1] - bin_edges[0]
    scale = len(mut_hist_list) * bin_width
    plt.plot(x_vals, kde(x_vals) * scale, color='yellow', linewidth=2)
    plt.title(f"PLOT 3: Histogram of Mutation Scores (fsl1)")
    plt.xlabel("Mutation Score (%)")
    plt.ylabel("Number of Programs")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl1_plots_path, "plot3_histogram_fsl1.png"))
    plt.close()
    print("Histogram done (plot3_histogram_fsl1.png)")

# PLOT 4
print("PLOT 4: Enhanced Classification Barplot (split catastrophic, partial, near-miss, well tested)")
plt.figure(figsize=(12, 7))
if "Detailed Classification" in merged_result_data.columns:
    cat_order = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    color_map = classification_color_map
    counts = []
    for cat in cat_order:
        cnt = sum(merged_result_data["Detailed Classification"] == cat)
        counts.append(cnt)
    colors = [color_map[cat] for cat in cat_order]
    bars = plt.bar(cat_order, counts, color=colors)
    for i, val in enumerate(counts):
        plt.text(i, val + 0.25, f'n={val}', ha='center', fontsize=12)
    legend_handles = [mpatches.Patch(color=color_map[cat], label=cat) for cat in cat_order]
    plt.legend(handles=legend_handles, loc='upper right')
else:
    base_classes = merged_result_data["Classification"].value_counts()
    plt.bar(base_classes.index, base_classes.values, color=['lightblue','yellow'])
    for i, val in enumerate(base_classes.values):
        plt.text(i, val + 0.2, str(val), ha='center', fontsize=12)
plt.ylabel("Number of Programs")
plt.xlabel("Test Classification")
plt.title("PLOT 4: Distribution per Test Classification (Split, fsl1)")
plt.tight_layout()
plt.savefig(os.path.join(fsl1_plots_path, "plot4_enhanced_barplot_fsl1.png"))
plt.close()
print("PLOT 4 saved as plot4_enhanced_barplot_fsl1.png")

# PLOT 5
print("PLOT 5: Enhanced Mutation Score Barplot per Program (with mutant/assertion counts)")
plt.figure(figsize=(15, 7))
if "Mutation Score" in merged_result_data.columns:
    sorted_df = merged_result_data.sort_values("Mutation Score", ascending=False)
    x_labels = sorted_df["Program"].tolist()
    y_values = sorted_df["Mutation Score"].tolist()
    mutant_counts = sorted_df["Num Mutants"].tolist() if "Num Mutants" in sorted_df.columns else [None]*len(y_values)
    assertion_counts = sorted_df["Assertion Count"].tolist() if "Assertion Count" in sorted_df.columns else [None]*len(y_values)
    bar_colors = []
    for i, v in enumerate(y_values):
        if v == 0:
            bar_colors.append("red")
        elif v < 61:
            bar_colors.append("orange")
        elif v < 80:
            bar_colors.append("yellow")
        else:
            bar_colors.append("lightblue")
    bars = plt.bar(x_labels, y_values, color=bar_colors)
    for idx, bar in enumerate(bars):
        txt = f"{y_values[idx]:.0f}%"
        m = mutant_counts[idx]
        a = assertion_counts[idx]
        if m is not None and not np.isnan(m):
            txt += f"\nM:{int(m)}"
        if a is not None and not np.isnan(a):
            txt += f"\nA:{int(a)}"
        if y_values[idx] == 0:
            plt.text(idx, 2, "Catastrophic", ha='center', va='bottom', fontsize=7, color='red')
        plt.text(idx, bar.get_height() + 2, txt, ha='center', va='bottom', fontsize=7)
    plt.xticks(rotation=90, fontsize=8)
    legend_elements = [
        mpatches.Patch(color="lightblue", label="Well tested"),
        mpatches.Patch(color="yellow", label="Near-miss"),
        mpatches.Patch(color="orange", label="Partial"),
        mpatches.Patch(color="red", label="Catastrophic")
    ]
    plt.legend(handles=legend_elements)
plt.ylabel("Mutation Score (%)")
plt.xlabel("Program")
plt.title("PLOT 5: Mutation Score per Program (Split/Annotated, fsl1)")
plt.tight_layout()
plt.savefig(os.path.join(fsl1_plots_path, "plot5_enhanced_mutscore_fsl1.png"))
plt.close()
print("PLOT 5 saved as plot5_enhanced_mutscore_fsl1.png")

# PLOT 6
print("PLOT 6: Outlier Barplot (Reden 0%-balken, Label)")
plt.figure(figsize=(14, 6))
outlier_rows = merged_result_data[
    (merged_result_data["Detailed Classification"] == "Catastrophic") |
    (merged_result_data["Detailed Classification"] == "Partial") |
    (merged_result_data["Detailed Classification"] == "Near-miss")
]
if not outlier_rows.empty:
    out_x = outlier_rows["Program"].tolist()
    out_y = outlier_rows["Mutation Score"].tolist()
    out_cov = outlier_rows["Statement Coverage (%)"].tolist() if "Statement Coverage (%)" in outlier_rows.columns else [None]*len(out_y)
    bar_colors = []
    labels = []
    for i, val in enumerate(out_y):
        if val == 0:
            bar_colors.append("red")
        elif val < 61:
            bar_colors.append("orange")
        elif val < 80:
            bar_colors.append("yellow")
        else:
            bar_colors.append("lightblue")
        # Label: reason
        if out_cov[i] is not None and not np.isnan(out_cov[i]):
            if out_cov[i] >= 80:
                labels.append("Assertion Failure")
            elif out_cov[i] < 80:
                labels.append("Coverage Failure")
            else:
                labels.append("Unknown")
        else:
            labels.append("Unknown")
    plt.bar(out_x, out_y, color=bar_colors)
    for idx, v in enumerate(out_y):
        plt.text(idx, v + 1, labels[idx], ha='center', va='bottom', fontsize=8)
    plt.xticks(rotation=45, fontsize=8)
    legend_elements = [
        mpatches.Patch(color="yellow", label="Near-miss"),
        mpatches.Patch(color="orange", label="Partial"),
        mpatches.Patch(color="red", label="Catastrophic")
    ]
    plt.legend(handles=legend_elements)
plt.ylabel("Mutation Score (%)")
plt.title("PLOT 6: Outlier Mutation Scores with Failure Causes (fsl1)")
plt.tight_layout()
plt.savefig(os.path.join(fsl1_plots_path, "plot6_outlier_fsl1.png"))
plt.close()
print("PLOT 6 saved as plot6_outlier_fsl1.png")

# PLOT 7
print("PLOT 7: Scatterplot Mutation Score vs Statement Coverage")
plt.figure(figsize=(10, 7))
if "Statement Coverage (%)" in merged_result_data.columns:
    xvals = merged_result_data["Statement Coverage (%)"]
    yvals = merged_result_data["Mutation Score"]
    class_col = merged_result_data["Detailed Classification"] if "Detailed Classification" in merged_result_data.columns else merged_result_data["Classification"]
    color_map = classification_color_map
    scatter_colors = [color_map.get(str(v), "grey") for v in class_col]
    plt.scatter(xvals, yvals, c=scatter_colors, alpha=0.8)
    if len(xvals.dropna()) > 2:
        m, b = np.polyfit(xvals.dropna(), yvals.dropna(), 1)
        plt.plot(xvals, m * xvals + b, color='grey', linestyle='dashed')
        corr = np.corrcoef(xvals.dropna(), yvals.dropna())[0, 1]
        plt.title(f"PLOT 7: Mutation Score vs Statement Coverage (Pearson R={corr:.2f})")
    else:
        plt.title("PLOT 7: Mutation Score vs Statement Coverage (fsl1)")
    plt.xlabel("Statement Coverage (%)")
    plt.ylabel("Mutation Score (%)")
    legend_elements = [mpatches.Patch(color=color_map[cat], label=cat) for cat in color_map]
    plt.legend(handles=legend_elements)
    plt.tight_layout()
    plt.savefig(os.path.join(fsl1_plots_path, "plot7_mutscore_vs_coverage_fsl1.png"))
    plt.close()
    print("PLOT 7 saved as plot7_mutscore_vs_coverage_fsl1.png")

# PLOT 8
print("PLOT 8: Scatterplot Mutation Score vs Assertion Count")
plt.figure(figsize=(10, 7))
if "Assertion Count" in merged_result_data.columns:
    xvals = merged_result_data["Assertion Count"]
    yvals = merged_result_data["Mutation Score"]
    class_col = merged_result_data["Detailed Classification"] if "Detailed Classification" in merged_result_data.columns else merged_result_data["Classification"]
    color_map = classification_color_map
    scatter_colors = [color_map.get(str(v), "grey") for v in class_col]
    plt.scatter(xvals, yvals, c=scatter_colors, alpha=0.8)
    for i in range(len(xvals)):
        # label "difficult" programs with low assertion count and low score
        if pd.notnull(xvals.iloc[i]) and xvals.iloc[i] < 20 and yvals.iloc[i] < 80:
            plt.text(xvals.iloc[i], yvals.iloc[i], merged_result_data["Program"].iloc[i], fontsize=6)
    plt.xlabel("Assertion Count")
    plt.ylabel("Mutation Score (%)")
    plt.title("PLOT 8: Mutation Score vs Assertion Count (fsl1)")
    legend_elements = [mpatches.Patch(color=color_map[cat], label=cat) for cat in color_map]
    plt.legend(handles=legend_elements)
    plt.tight_layout()
    plt.savefig(os.path.join(fsl1_plots_path, "plot8_mutscore_vs_assertioncount_fsl1.png"))
    plt.close()
    print("PLOT 8 saved as plot8_mutscore_vs_assertioncount_fsl1.png")

# PLOT 9
print("PLOT 9: Boxplot Mutant Count by Class")
plt.figure(figsize=(8, 7))
if "Num Mutants" in merged_result_data.columns:
    classes = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    color_map = ["lightblue", "yellow", "orange", "red"]
    data = []
    for c in classes:
        data.append(merged_result_data[merged_result_data["Detailed Classification"]==c]["Num Mutants"].dropna())
    plt.boxplot(data, labels=classes, patch_artist=True,
        boxprops=dict(facecolor='lightblue', edgecolor='black'),
        medianprops=dict(color='yellow'))
    plt.ylabel("Number of Mutants")
    plt.title("PLOT 9: Mutant Count by Test Class (fsl1)")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl1_plots_path, "plot9_mutant_count_fsl1.png"))
    plt.close()
    print("PLOT 9 saved as plot9_mutant_count_fsl1.png")

# PLOT 10
print("PLOT 10: Scatterplot Mutation Score vs Test Suite Size")
plt.figure(figsize=(10, 7))
if "Test Suite Size" in merged_result_data.columns:
    xvals = merged_result_data["Test Suite Size"]
    yvals = merged_result_data["Mutation Score"]
    class_col = merged_result_data["Detailed Classification"] if "Detailed Classification" in merged_result_data.columns else merged_result_data["Classification"]
    color_map = classification_color_map
    scatter_colors = [color_map.get(str(v), "grey") for v in class_col]
    plt.scatter(xvals, yvals, c=scatter_colors, alpha=0.8)
    for i in range(len(xvals)):
        if (not np.isnan(xvals.iloc[i])) and (xvals.iloc[i] < 5) and (yvals.iloc[i] < 80):
            plt.text(xvals.iloc[i], yvals.iloc[i], merged_result_data["Program"].iloc[i], fontsize=6)
    plt.xlabel("Test Suite Size")
    plt.ylabel("Mutation Score (%)")
    plt.title("PLOT 10: Mutation Score vs Test Suite Size (fsl1)")
    legend_elements = [mpatches.Patch(color=color_map[cat], label=cat) for cat in color_map]
    plt.legend(handles=legend_elements)
    plt.tight_layout()
    plt.savefig(os.path.join(fsl1_plots_path, "plot10_mutscore_vs_suitesize_fsl1.png"))
    plt.close()
    print("PLOT 10 saved as plot10_mutscore_vs_suitesize_fsl1.png")

# PLOT 11
print("PLOT 11: Parallel Coordinates Plot")
from pandas.plotting import parallel_coordinates
plt.figure(figsize=(14, 8))
key_metrics = ["Mutation Score", "Statement Coverage (%)", "Assertion Count", "Num Mutants", "Test Suite Size"]
for metric in key_metrics:
    if metric not in merged_result_data.columns:
        merged_result_data[metric] = np.nan
subset = merged_result_data.dropna(subset=["Detailed Classification"])
try:
    parallel_coordinates(subset[["Detailed Classification"] + key_metrics], class_column="Detailed Classification", color=['lightblue', 'yellow', 'orange', 'red'])
    plt.title("PLOT 11: Parallel Coordinates of Key Metrics by Class (fsl1)")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl1_plots_path, "plot11_parallel_coordinates_fsl1.png"))
    plt.close()
    print("PLOT 11 saved as plot11_parallel_coordinates_fsl1.png")
except Exception as e:
    print("Parallel coordinates failed:", e)

# PLOT 12
print("PLOT 12: Boxplot Assertion Count by Class")
plt.figure(figsize=(8, 7))
if "Assertion Count" in merged_result_data.columns:
    classes = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    data = []
    for c in classes:
        data.append(merged_result_data[merged_result_data["Detailed Classification"]==c]["Assertion Count"].dropna())
    plt.boxplot(data, labels=classes, patch_artist=True,
        boxprops=dict(facecolor='yellow', edgecolor='black'),
        medianprops=dict(color='orange'))
    plt.ylabel("Assertion Count")
    plt.title("PLOT 12: Assertion Count by Test Class (fsl1)")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl1_plots_path, "plot12_assertioncount_fsl1.png"))
    plt.close()
    print("PLOT 12 saved as plot12_assertioncount_fsl1.png")

# PLOT 13
print("PLOT 13: Violin Plot/Density Overlay for Mutation Score by Class")
plt.figure(figsize=(8, 7))
if "Mutation Score" in merged_result_data.columns and "Detailed Classification" in merged_result_data.columns:
    try:
        # Define order and colors
        class_order = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
        color_map = ["lightblue", "yellow", "orange", "red"]
        # Prepare data as lists for each class
        data = []
        for cname in class_order:
            # All mutation scores for this class (remove NaN)
            vals = merged_result_data[merged_result_data["Detailed Classification"] == cname]["Mutation Score"].dropna().tolist()
            data.append(vals)
        # Matplotlib violinplot
        parts = plt.violinplot(data, positions=range(1, len(class_order)+1), widths=0.7, showmedians=True, showmeans=False, showextrema=True)
        # Color the violins manually
        for i, pc in enumerate(parts['bodies']):
            pc.set_facecolor(color_map[i])
            pc.set_edgecolor('black')
            pc.set_alpha(0.8)
        if 'cmedians' in parts:
            parts['cmedians'].set_color('white')
            parts['cmedians'].set_linewidth(2)
        # Set x-ticks and labels
        plt.xticks(range(1, len(class_order)+1), class_order)
        plt.ylabel("Mutation Score")
        plt.xlabel("Detailed Classification")
        plt.title("PLOT 13: Violin Plot of Mutation Score by Class (fsl1, matplotlib)")
        # Legend
        legend_elements = [mpatches.Patch(color=color_map[i], label=class_order[i]) for i in range(len(class_order))]
        plt.legend(handles=legend_elements, loc='best')
        plt.tight_layout()
        plt.savefig(os.path.join(fsl1_plots_path, "plot13_violinplot_fsl1.png"))
        plt.close()
        print("PLOT 13 saved as plot13_violinplot_fsl1.png")
    except Exception as err:
        print("Matplotlib violinplot failed:", err)
else:
    print("PLOT 13 skipped: columns missing.")

# PLOT 14
print("PLOT 14: Boxplot of Total Time by Test Class")
plt.figure(figsize=(8, 7))
if "Test Time (s)" in merged_result_data.columns:
    classes = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    data = []
    for c in classes:
        data.append(merged_result_data[merged_result_data["Detailed Classification"]==c]["Test Time (s)"].dropna())
    plt.boxplot(data, labels=classes, patch_artist=True,
        boxprops=dict(facecolor='grey', edgecolor='black'),
        medianprops=dict(color='black'))
    plt.ylabel("Total Time (s)")
    plt.title("PLOT 14: Total Time by Test Class (fsl1)")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl1_plots_path, "plot14_totaltime_fsl1.png"))
    plt.close()
    print("PLOT 14 saved as plot14_totaltime_fsl1.png")

print("All 14 plots saved in folder:", fsl1_plots_path)
