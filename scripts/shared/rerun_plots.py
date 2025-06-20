"""
script met aggregatie: vergelijkt GEMIDDELDE en STANDAARDDEVIATIE per methode (3 reruns per LLM-methode), vergeleken met baselines.
Barplots tonen mean ± std (errorbar) voor mutation score, coverage, asserts en suite size.
Alle plots in map 'plot_aggr'.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# KLEUREN EN PADEN
method_color_map = {
    "CoT": 'lightblue',
    "FSL": 'yellow',
    "ZSL": 'orange',
    "Pynguin": 'grey',
    "mbpp": 'green'
}
classification_color_map = {
    "Well tested": 'lightblue',
    "Near-miss": 'yellow',
    "Partial": 'orange',
    "Catastrophic": 'red',
    "Unknown": 'grey'
}

base_dir = "results"
rerun_csv_paths = {
    "CoT": [
        os.path.join(base_dir, "cot1", "appendix_metrics_table_cot1.csv"),
        os.path.join(base_dir, "cot2", "appendix_metrics_table_cot2.csv"),
        os.path.join(base_dir, "cot", "appendix_metrics_table_cot.csv")
    ],
    "FSL": [
        os.path.join(base_dir, "fsl1", "appendix_metrics_table_fsl1.csv"),
        os.path.join(base_dir, "fsl2", "appendix_metrics_table_fsl2.csv"),
        os.path.join(base_dir, "fsl", "appendix_metrics_table_fsl.csv")
    ],
    "ZSL": [
        os.path.join(base_dir, "zsl1", "appendix_metrics_table_zsl1.csv"),
        os.path.join(base_dir, "zsl2", "appendix_metrics_table_zsl2.csv"),
        os.path.join(base_dir, "zsl", "appendix_metrics_table_zsl.csv")
    ],
    "Pynguin": [
        os.path.join(base_dir, "pynguin", "appendix_metrics_table_pynguin.csv")
    ],
    "mbpp": [
        os.path.join(base_dir, "mbpp", "appendix_metrics_table_mbpp.csv")
    ]
}
plots_dir = "results/plot_aggr"
if not os.path.exists(plots_dir):
    try:
        os.makedirs(plots_dir)
        print("Directory created:", plots_dir)
    except Exception as plot_folder_error:
        print("Could not create folder:", plots_dir, "\nError:", plot_folder_error)
else:
    print("Directory already exists:", plots_dir)

# DATA INLEZEN EN GEMIDDELDES/STDS BEREKENEN
summary_dict = {}
for method, csv_list in rerun_csv_paths.items():
    coverages, mutscores, asserts, suitesizes, filtered = [], [], [], [], []
    for path in csv_list:
        if os.path.exists(path):
            try:
                df = pd.read_csv(path, sep=';')
                df = df.dropna(subset=['Mutation Score', 'Statement Coverage (%)', 'Assertion Count', 'Test Suite Size'])
                filtered.append(len(df))
                coverages.append(df['Statement Coverage (%)'].mean())
                mutscores.append(df['Mutation Score'].mean())
                asserts.append(df['Assertion Count'].mean())
                suitesizes.append(df['Test Suite Size'].mean())
            except Exception as e:
                print("Error loading or parsing:", path, e)
        else:
            print("File not found:", path)
    summary_dict[method] = {
        "mean_filtered_tests": np.mean(filtered) if filtered else np.nan,
        "std_filtered_tests": np.std(filtered, ddof=1) if len(filtered) > 1 else np.nan,
        "mean_coverage": np.mean(coverages) if coverages else np.nan,
        "std_coverage": np.std(coverages, ddof=1) if len(coverages) > 1 else np.nan,
        "mean_mutscore": np.mean(mutscores) if mutscores else np.nan,
        "std_mutscore": np.std(mutscores, ddof=1) if len(mutscores) > 1 else np.nan,
        "mean_asserts": np.mean(asserts) if asserts else np.nan,
        "std_asserts": np.std(asserts, ddof=1) if len(asserts) > 1 else np.nan,
        "mean_suite_size": np.mean(suitesizes) if suitesizes else np.nan,
        "std_suite_size": np.std(suitesizes, ddof=1) if len(suitesizes) > 1 else np.nan
    }

methods = list(summary_dict.keys())
plot_df = pd.DataFrame({
    "Method": methods,
    "Survivors": [summary_dict[m]["mean_filtered_tests"] for m in methods],
    "Survivors_std": [summary_dict[m]["std_filtered_tests"] for m in methods],
    "Coverage": [summary_dict[m]["mean_coverage"] for m in methods],
    "Coverage_std": [summary_dict[m]["std_coverage"] for m in methods],
    "Mutation Score": [summary_dict[m]["mean_mutscore"] for m in methods],
    "Mutation Score_std": [summary_dict[m]["std_mutscore"] for m in methods],
    "Asserts": [summary_dict[m]["mean_asserts"] for m in methods],
    "Asserts_std": [summary_dict[m]["std_asserts"] for m in methods],
    "Suite Size": [summary_dict[m]["mean_suite_size"] for m in methods],
    "Suite Size_std": [summary_dict[m]["std_suite_size"] for m in methods]
})

# GEMIDDELDE MUTATION SCORE (met errorbars std)
plt.figure(figsize=(8,6))
plt.bar(plot_df["Method"], plot_df["Mutation Score"], yerr=plot_df["Mutation Score_std"],
        color=[method_color_map[m] for m in plot_df["Method"]], capsize=7)
plt.ylabel("Mutation Score (%)")
plt.xlabel("Method")
plt.title("Mean Mutation Score per Method (errorbars: std over reruns)")
for idx, val in enumerate(plot_df["Mutation Score"]):
    plt.text(idx, val+1, f"{val:.1f}%", ha='center', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "barplot_mutscore.png"))
plt.close()

# COVERAGE
plt.figure(figsize=(8,6))
plt.bar(plot_df["Method"], plot_df["Coverage"], yerr=plot_df["Coverage_std"],
        color=[method_color_map[m] for m in plot_df["Method"]], capsize=7)
plt.ylabel("Statement Coverage (%)")
plt.xlabel("Method")
plt.title("Mean Statement Coverage per Method (errorbars: std)")
for idx, val in enumerate(plot_df["Coverage"]):
    plt.text(idx, val+1, f"{val:.1f}%", ha='center', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "barplot_coverage.png"))
plt.close()

# ASSERTS
plt.figure(figsize=(8,6))
plt.bar(plot_df["Method"], plot_df["Asserts"], yerr=plot_df["Asserts_std"],
        color=[method_color_map[m] for m in plot_df["Method"]], capsize=7)
plt.ylabel("Assertions per Suite")
plt.xlabel("Method")
plt.title("Mean Number of Assertions per Method (errorbars: std)")
for idx, val in enumerate(plot_df["Asserts"]):
    plt.text(idx, val+0.5, f"{val:.2f}", ha='center', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "barplot_asserts.png"))
plt.close()

# SUITE SIZE
plt.figure(figsize=(8,6))
plt.bar(plot_df["Method"], plot_df["Suite Size"], yerr=plot_df["Suite Size_std"],
        color=[method_color_map[m] for m in plot_df["Method"]], capsize=7)
plt.ylabel("Test Suite Size")
plt.xlabel("Method")
plt.title("Mean Suite Size per Method (errorbars: std)")
for idx, val in enumerate(plot_df["Suite Size"]):
    plt.text(idx, val+0.5, f"{val:.2f}", ha='center', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "barplot_suitesize.png"))
plt.close()

# ASSERTION DENSITY (per suite)
assertion_density = plot_df["Asserts"] / plot_df["Suite Size"]
plt.figure(figsize=(8,6))
plt.bar(plot_df["Method"], assertion_density, color=[method_color_map[m] for m in plot_df["Method"]])
plt.ylabel("Assertion Density (assertions per test)")
plt.xlabel("Method")
plt.title("Mean Assertion Density per Method")
for idx, val in enumerate(assertion_density):
    plt.text(idx, val+0.02, f"{val:.2f}", ha='center', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "barplot_assertion_density.png"))
plt.close()

# ASSERTION DENSITY (per coverage)
assertion_density_loc = plot_df["Asserts"] / plot_df["Coverage"].replace(0, np.nan)
plt.figure(figsize=(8,6))
plt.bar(plot_df["Method"], assertion_density_loc, color=[method_color_map[m] for m in plot_df["Method"]])
plt.ylabel("Assertion Density (assertions per % coverage)")
plt.xlabel("Method")
plt.title("Mean Assertion Density per LoC by Method")
for idx, val in enumerate(assertion_density_loc):
    plt.text(idx, val+0.02, f"{val:.2f}", ha='center', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "barplot_assertion_loc.png"))
plt.close()

# AANTAL SURVIVORS
plt.figure(figsize=(8,6))
plt.bar(plot_df["Method"], plot_df["Survivors"], yerr=plot_df["Survivors_std"],
        color=[method_color_map[m] for m in plot_df["Method"]], capsize=7)
plt.ylabel("Filtered Test Suites")
plt.xlabel("Method")
plt.title("Mean Number of Survivors per Method (errorbars: std)")
for idx, val in enumerate(plot_df["Survivors"]):
    plt.text(idx, val+0.5, f"{val:.0f}", ha='center', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "barplot_survivors.png"))
plt.close()



# Plot B: Scatterplot van mean mutation score vs mean coverage per methode
method_metrics = {}
for method in methods:
    method_metrics[method] = {
        "Mutation Score": summary_dict[method]["mean_mutscore"],
        "Statement Coverage (%)": summary_dict[method]["mean_coverage"],
        "Assertion Count": summary_dict[method]["mean_asserts"],
        "Suite Size": summary_dict[method]["mean_suite_size"],
        "Assertion SD": summary_dict[method]["std_asserts"]
    }

plt.figure(figsize=(10,8))
for m in method_metrics:
    x = method_metrics[m]["Mutation Score"]
    y = method_metrics[m]["Statement Coverage (%)"]
    s = method_metrics[m]["Assertion Count"]*2  # marker size
    plt.scatter(x, y, s=s, color=method_color_map[m], label=f"{m} (asserts: {method_metrics[m]['Assertion Count']:.1f})", alpha=0.8, edgecolor="black")
    plt.text(x+0.5, y, m, fontsize=11, weight="bold", color=method_color_map[m])
plt.xlabel("Mean Mutation Score (%)")
plt.ylabel("Mean Statement Coverage (%)")
plt.title("Mean Mutation Score vs Coverage per Method (marker size: mean # asserts)")
plt.legend(title="Method + mean # asserts", loc="lower right")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, "plotB_scatter.png"))
plt.close()
print("PLOT B saved as plotB_scatter.png")


print("Alle aggregated comparison plots saved in folder:", plots_dir)
