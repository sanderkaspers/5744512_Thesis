"""
This script combines, analyzes, and visualizes mutation testing results from the 'fsl' experiment.
It loads, cleans, and merges data from CSV, YAML, and JSON sources, computes key metrics,
and generates all required appendix and main text visuals in one run.
"""

# IMPORTS
import os
import yaml  # For reading YAML files.
import pandas as pd  # For DataFrame operations.
import matplotlib.pyplot as plt  # For plots.
import matplotlib.patches as mpatches
import csv  # For CSV reading/writing.
import numpy as np
from scipy.stats import gaussian_kde
import random
import json
import re

# CUSTOM YAML LOADER: Ignore Python object/module tags
class IgnorePyModuleLoader(yaml.SafeLoader):
    pass

def ignore_python_module_constructor(loader, suffix, node):
    # Just return None for any python/module or other python tags
    return None

# Ignore all known and unknown python-related YAML tags
IgnorePyModuleLoader.add_multi_constructor(
    'tag:yaml.org,2002:python/module:', lambda loader, suffix, node: None
)
IgnorePyModuleLoader.add_multi_constructor('tag:yaml.org,2002:python/', ignore_python_module_constructor)
IgnorePyModuleLoader.add_multi_constructor('!', lambda loader, suffix, node: None)
# END CUSTOM LOADER

# PATHS
fsl_result_path = "results/fsl"
yaml_folder_fsl = os.path.join(fsl_result_path, 'filtered_mutation_results')
csv_file_fsl = os.path.join(fsl_result_path, 'classification_summary_fsl.csv')
fsl_plots_path = os.path.join(fsl_result_path, 'plots')
metrics_table_csv = os.path.join('results', 'fsl', 'appendix_metrics_table_fsl.csv')
coverage_json = os.path.join('results', 'fsl', 'coverage_per_test_fsl.json')

# GLOBAL VARIABLES
random.seed(3)
png_ext = ".png"
classification_color_map = {
    "Well tested": 'lightblue',
    "Weakly tested": 'yellow'
}
pie_colors = ['lightblue', 'yellow']

# CREATE DIRECTORY FOR PLOTS
if not os.path.exists(fsl_plots_path):
    try:
        os.makedirs(fsl_plots_path)
        print("Directory created:", fsl_plots_path)
    except Exception as plot_folder_error:
        print("Could not create folder:", fsl_plots_path, "\nError:", plot_folder_error)
else:
    print("Directory already exists:", fsl_plots_path)

# METRIC GATHERING BLOCK

# LOAD classification_summary_fsl.csv as df_classification
print("Trying to load classification data (df_classification)…")
try:
    df_classification = pd.read_csv(csv_file_fsl, sep=';')
    print("Classification CSV found & loaded (df_classification).")
    print("Number of rows in classification file:", len(df_classification))
except Exception as classification_load_error:
    print("Could not load classification CSV:", classification_load_error)
    df_classification = None

# PATCH/FIX: filter on valid Program-names
if df_classification is not None:
    # Remove all rows with missing/None/NaN/empty Program
    old_count = len(df_classification)
    df_classification = df_classification[
        df_classification['Program'].notnull() &
        (df_classification['Program'].astype(str).str.lower() != "none") &
        (df_classification['Program'].astype(str).str.strip() != "")
    ]
    print(f"After filtering: {len(df_classification)} valid programs (from {old_count})")


# LOAD coverage_per_test_fsl.json
print("Loading statement coverage JSON…")
coverage_dict = {}
if os.path.exists(coverage_json):
    try:
        with open(coverage_json, "r", encoding="utf-8") as f_cov:
            coverage_dict = json.load(f_cov)
        print("coverage_per_test_fsl.json loaded. Keys:", len(coverage_dict))
    except Exception as err_covjson:
        print("Could not load coverage JSON:", err_covjson)
        coverage_dict = {}
else:
    print("coverage_per_test_fsl.json not found. Continuing without coverage.")

def get_coverage(program_name, coverage_dict):
    """
    Looks up coverage % for a given program.
    """
    # remove .py if present
    # Ensure the key matches what's in coverage_dict (add .py if not present)
    if str(program_name).endswith('.py'):
        key = str(program_name)
    else:
        key = str(program_name) + '.py'
    try:
        if key in coverage_dict:
            return float(coverage_dict[key])
    except Exception as e:
        print("Error getting coverage for", key, e)
    return np.nan

results_list = []
if df_classification is not None:
    print("Iterating through classification data for metrics gathering.")
    for idx, row in df_classification.iterrows():
        program_name = row.get('Program', None)
        mutation_score = row.get('Mutation Score', np.nan)
        classification_label = row.get('Classification', "")
        yaml_path = os.path.join(yaml_folder_fsl, str(program_name) + "_report.yaml")
        # Default metrics
        ymetrics = {
            "Test Time (s)": np.nan,
            "Number of Tests": np.nan,
            "Num Mutants": np.nan,
            "Assertion Count": np.nan
        }
        # Try YAML with custom loader!
        if os.path.exists(yaml_path):
            print("YAML found for", program_name)
            try:
                with open(yaml_path, "r", encoding="utf-8") as f_yaml:
                    ydata = yaml.load(f_yaml, Loader=IgnorePyModuleLoader)
                if ydata is None:
                    ydata = {}
                ymetrics["Test Time (s)"] = ydata.get("total_time", np.nan)
                ymetrics["Number of Tests"] = ydata.get("number_of_tests", np.nan)
                mutant_list = ydata.get("mutations", [])
                ymetrics["Num Mutants"] = len(mutant_list)
                # Count assertions (mutants with exception_traceback)
                ymetrics["Assertion Count"] = 0
                for mutant in mutant_list:
                    if isinstance(mutant, dict) and mutant.get("exception_traceback"):
                        ymetrics["Assertion Count"] += 1
            except Exception as yaml_parse_error:
                print("YAML parse error for", yaml_path, ":", yaml_parse_error)
        else:
            print("No YAML found for", program_name)
        # Try coverage JSON
        statement_coverage = get_coverage(program_name, coverage_dict)
        # Compose row
        tmp_dict = {
            "Program": program_name,
            "Mutation Score": mutation_score,
            "Classification": classification_label,
            "Test Time (s)": ymetrics["Test Time (s)"],
            "Test Suite Size": ymetrics["Number of Tests"],
            "Num Mutants": ymetrics["Num Mutants"],
            "Assertion Count": ymetrics["Assertion Count"],
            "Statement Coverage (%)": statement_coverage
        }
        results_list.append(tmp_dict)
    print("Metric gathering done for", len(results_list), "programs.")
else:
    print("df_classification is None; skipping metrics gathering.")

# SAVE METRICS TO CSV
print("Saving enriched metrics to", metrics_table_csv)
try:
    df_metrics = pd.DataFrame(results_list)
    df_metrics.to_csv(metrics_table_csv, index=False, sep=';')
    print("Enriched CSV written to:", metrics_table_csv)
except Exception as save_error:
    print("Could not save enriched CSV:", save_error)

# DATA LOAD FOR PLOTTING
print("Loading appendix metrics table (main CSV, enriched) ...")
try:
    merged_result_data = pd.read_csv(metrics_table_csv, sep=';')
    print("appendix_metrics_table_fsl.csv loaded successfully:", metrics_table_csv)
except Exception as errcsv:
    print("Error reading appendix_metrics_table_fsl.csv:", metrics_table_csv)
    print(errcsv)
    merged_result_data = pd.DataFrame()

# Stripping .py from Program col for safety
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
if "Mutation Score" in merged_result_data.columns:
    merged_result_data["Detailed Classification"] = merged_result_data["Mutation Score"].apply(detailed_split)
    print("Detailed classification assigned.")
else:
    merged_result_data["Detailed Classification"] = "Unknown"
    print("No Mutation Score col for split class.")

# Old fallback for base class
if "Classification" not in merged_result_data.columns:
    merged_result_data["Classification"] = merged_result_data["Detailed Classification"].replace(
        {"Well tested": "Well tested", "Near-miss": "Weakly tested", "Partial": "Weakly tested", "Catastrophic": "Weakly tested"}
    )

# APPENDIX PLOTS
"""
print("Generating appendix plots...")

## PLOT 2: Pie Chart - Distribution of Classification Labels (4-way split)
print("PLOT 2: Pie Chart - Distribution of Classification Labels (4-way split, main text)")
if "Detailed Classification" in merged_result_data.columns:
    class_order = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    color_map = {"Well tested": "lightblue", "Near-miss": "yellow", "Partial": "orange", "Catastrophic": "red"}
    class_counter = merged_result_data["Detailed Classification"].value_counts().to_dict()
    values = [class_counter.get(c, 0) for c in class_order]
    pie_colors = [color_map[c] for c in class_order]
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=class_order, autopct="%1.1f%%", startangle=140, colors=pie_colors)
    legend_handles = [mpatches.Patch(color=color_map[cat], label=cat) for cat in class_order]
    plt.legend(handles=legend_handles, loc='best')
    plt.title("PLOT 2: Distribution of Classification Labels (4-way split, fsl)")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl_plots_path, "plot2_pie_fsl.png"))
    plt.close()
    print("Pie plot saved as plot2_pie_fsl.png")
else:
    print("Detailed Classification column not found.")

# Plot 3: Boxplot mutation scores (appendix)
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
    plt.title(f"APPENDIX PLOT 3: Boxplot of Mutation Scores")
    plt.ylabel("Mutation Score (%)")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl_plots_path, "plot3_boxplot_fsl.png"))
    plt.close()
    print("Boxplot done (plot3_boxplot_fsl.png)")

# Plot 4: Histogram mutation scores (appendix)
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
    plt.title(f"APPENDIX PLOT 4: Distribution of Mutation Scores")
    plt.xlabel("Mutation Score (%)")
    plt.ylabel("Number of Programs")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl_plots_path, "plot4_histogram_fsl.png"))
    plt.close()
    print("Histogram done and saved as plot4_histogram_fsl.png")

# MAIN PLOTS
print("Generating main result plots 5–15 using enriched dataframe...")

# PLOT 5: Enhanced Classification Barplot (split catastrophic, partial, near-miss, well tested)
print("PLOT 5: Enhanced Classification Barplot (multi-class breakdown, main text)")
plt.figure(figsize=(12, 7))
if "Detailed Classification" in merged_result_data.columns:
    cat_order = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    color_map = {"Well tested": "lightblue", "Near-miss": "yellow", "Partial": "orange", "Catastrophic": "red"}
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
plt.title("PLOT 5: Distribution per Test Classification (Split, fsl)")
plt.tight_layout()
plt.savefig(os.path.join(fsl_plots_path, "plot5_enhanced_barplot_fsl.png"))
plt.close()
print("PLOT 5 saved as plot5_enhanced_barplot_fsl.png")

# PLOT 6: Enhanced Mutation Score Barplot per Program (with mutant/assertion counts)
print("PLOT 6: Enhanced Mutation Score Barplot per Program (main text)")
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
plt.title("PLOT 6: Mutation Score per Program (Split/Annotated, fsl)")
plt.tight_layout()
plt.savefig(os.path.join(fsl_plots_path, "plot6_enhanced_mutscore_fsl.png"))
plt.close()
print("PLOT 6 saved as plot6_enhanced_mutscore_fsl.png")

# PLOT 7: Outlier Barplot (Reden 0%-balken, Label)
print("PLOT 7: Outlier Barplot (split, main text)")
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
plt.title("PLOT 7: Outlier Mutation Scores with Failure Causes (fsl)")
plt.tight_layout()
plt.savefig(os.path.join(fsl_plots_path, "plot7_outlier_fsl.png"))
plt.close()
print("PLOT 7 saved as plot7_outlier_fsl.png")

# PLOT 8: Scatterplot Mutation Score vs Statement Coverage
print("PLOT 8: Scatterplot Mutation Score vs Statement Coverage")
plt.figure(figsize=(10, 7))
if "Statement Coverage (%)" in merged_result_data.columns:
    xvals = merged_result_data["Statement Coverage (%)"]
    yvals = merged_result_data["Mutation Score"]
    class_col = merged_result_data["Detailed Classification"] if "Detailed Classification" in merged_result_data.columns else merged_result_data["Classification"]
    color_map = {"Well tested": "lightblue", "Near-miss": "yellow", "Partial": "orange", "Catastrophic": "red"}
    scatter_colors = [color_map.get(str(v), "grey") for v in class_col]
    plt.scatter(xvals, yvals, c=scatter_colors, alpha=0.8)
    if len(xvals.dropna()) > 2:
        m, b = np.polyfit(xvals.dropna(), yvals.dropna(), 1)
        plt.plot(xvals, m * xvals + b, color='grey', linestyle='dashed')
        corr = np.corrcoef(xvals.dropna(), yvals.dropna())[0, 1]
        plt.title(f"PLOT 8: Mutation Score vs Statement Coverage (Pearson R={corr:.2f})")
    else:
        plt.title("PLOT 8: Mutation Score vs Statement Coverage (fsl)")
    plt.xlabel("Statement Coverage (%)")
    plt.ylabel("Mutation Score (%)")
    legend_elements = [mpatches.Patch(color=color_map[cat], label=cat) for cat in color_map]
    plt.legend(handles=legend_elements)
    plt.tight_layout()
    plt.savefig(os.path.join(fsl_plots_path, "plot8_mutscore_vs_coverage_fsl.png"))
    plt.close()
    print("PLOT 8 saved as plot8_mutscore_vs_coverage_fsl.png")

# PLOT 9: Scatterplot Mutation Score vs Assertion Count
print("PLOT 9: Scatterplot Mutation Score vs Assertion Count")
plt.figure(figsize=(10, 7))
if "Assertion Count" in merged_result_data.columns:
    xvals = merged_result_data["Assertion Count"]
    yvals = merged_result_data["Mutation Score"]
    class_col = merged_result_data["Detailed Classification"] if "Detailed Classification" in merged_result_data.columns else merged_result_data["Classification"]
    color_map = {"Well tested": "lightblue", "Near-miss": "yellow", "Partial": "orange", "Catastrophic": "red"}
    scatter_colors = [color_map.get(str(v), "grey") for v in class_col]
    plt.scatter(xvals, yvals, c=scatter_colors, alpha=0.8)
    for i in range(len(xvals)):
        if pd.notnull(xvals.iloc[i]) and xvals.iloc[i] < 20 and yvals.iloc[i] < 80:
            plt.text(xvals.iloc[i], yvals.iloc[i], merged_result_data["Program"].iloc[i], fontsize=6)
    plt.xlabel("Assertion Count")
    plt.ylabel("Mutation Score (%)")
    plt.title("PLOT 9: Mutation Score vs Assertion Count (fsl)")
    legend_elements = [mpatches.Patch(color=color_map[cat], label=cat) for cat in color_map]
    plt.legend(handles=legend_elements)
    plt.tight_layout()
    plt.savefig(os.path.join(fsl_plots_path, "plot9_mutscore_vs_assertioncount_fsl.png"))
    plt.close()
    print("PLOT 9 saved as plot9_mutscore_vs_assertioncount_fsl.png")

# PLOT 10: Boxplot Mutant Count by Class
print("PLOT 10: Boxplot Mutant Count by Class")
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
    plt.title("PLOT 10: Mutant Count by Test Class (fsl)")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl_plots_path, "plot10_mutant_count_fsl.png"))
    plt.close()
    print("PLOT 10 saved as plot10_mutant_count_fsl.png")

# PLOT 11: Scatterplot Mutation Score vs Test Suite Size
print("PLOT 11: Scatterplot Mutation Score vs Test Suite Size")
plt.figure(figsize=(10, 7))
if "Test Suite Size" in merged_result_data.columns:
    xvals = merged_result_data["Test Suite Size"]
    yvals = merged_result_data["Mutation Score"]
    class_col = merged_result_data["Detailed Classification"] if "Detailed Classification" in merged_result_data.columns else merged_result_data["Classification"]
    color_map = {"Well tested": "lightblue", "Near-miss": "yellow", "Partial": "orange", "Catastrophic": "red"}
    scatter_colors = [color_map.get(str(v), "grey") for v in class_col]
    plt.scatter(xvals, yvals, c=scatter_colors, alpha=0.8)
    for i in range(len(xvals)):
        if (not np.isnan(xvals.iloc[i])) and (xvals.iloc[i] < 5) and (yvals.iloc[i] < 80):
            plt.text(xvals.iloc[i], yvals.iloc[i], merged_result_data["Program"].iloc[i], fontsize=6)
    plt.xlabel("Test Suite Size")
    plt.ylabel("Mutation Score (%)")
    plt.title("PLOT 11: Mutation Score vs Test Suite Size (fsl)")
    legend_elements = [mpatches.Patch(color=color_map[cat], label=cat) for cat in color_map]
    plt.legend(handles=legend_elements)
    plt.tight_layout()
    plt.savefig(os.path.join(fsl_plots_path, "plot11_mutscore_vs_suitesize_fsl.png"))
    plt.close()
    print("PLOT 11 saved as plot11_mutscore_vs_suitesize_fsl.png")

# PLOT 12: Parallel Coordinates Plot
print("PLOT 12: Parallel Coordinates Plot")
from pandas.plotting import parallel_coordinates
plt.figure(figsize=(14, 8))
key_metrics = ["Mutation Score", "Statement Coverage (%)", "Assertion Count", "Num Mutants", "Test Suite Size"]
for metric in key_metrics:
    if metric not in merged_result_data.columns:
        merged_result_data[metric] = np.nan
subset = merged_result_data.dropna(subset=["Detailed Classification"])
try:
    parallel_coordinates(subset[["Detailed Classification"] + key_metrics], class_column="Detailed Classification", color=['lightblue', 'yellow', 'orange', 'red'])
    plt.title("PLOT 12: Parallel Coordinates of Key Metrics by Class (fsl)")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl_plots_path, "plot12_parallel_coordinates_fsl.png"))
    plt.close()
    print("PLOT 12 saved as plot12_parallel_coordinates_fsl.png")
except Exception as e:
    print("Parallel coordinates failed:", e)

# PLOT 13: Boxplot Assertion Count by Class
print("PLOT 13: Boxplot Assertion Count by Class")
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
    plt.title("PLOT 13: Assertion Count by Test Class (fsl)")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl_plots_path, "plot13_assertioncount_fsl.png"))
    plt.close()
    print("PLOT 13 saved as plot13_assertioncount_fsl.png")

# PLOT 14: Violin Plot/Density Overlay for Mutation Score by Class
print("PLOT 14: Violin Plot/Density Overlay for Mutation Score by Class")
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
        plt.title("PLOT 14: Violin Plot of Mutation Score by Class (fsl, matplotlib)")
        # Legend
        import matplotlib.patches as mpatches
        legend_elements = [mpatches.Patch(color=color_map[i], label=class_order[i]) for i in range(len(class_order))]
        plt.legend(handles=legend_elements, loc='best')
        plt.tight_layout()
        plt.savefig(os.path.join(fsl_plots_path, "plot14_violinplot_fsl.png"))
        plt.close()
        print("PLOT 14 saved as plot14_violinplot_fsl.png")
    except Exception as err:
        print("Matplotlib violinplot failed:", err)
else:
    print("PLOT 14 skipped: columns missing.")

# PLOT 15: Boxplot of Total Time by Test Class
print("PLOT 15: Boxplot of Total Time by Test Class")
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
    plt.title("PLOT 15: Total Time by Test Class (fsl)")
    plt.tight_layout()
    plt.savefig(os.path.join(fsl_plots_path, "plot15_totaltime_fsl.png"))
    plt.close()
    print("PLOT 15 saved as plot15_totaltime_fsl.png")

print("All plots (appendix and main text) saved in folder:", fsl_plots_path)
"""