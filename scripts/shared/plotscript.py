"""
script: combineert, analyseert en visualiseert alle resultaten (CoT, FSL, ZSL, Pynguin).
Laadt de CSV's van alle vier methoden, merged deze tot één grote DataFrame,

"""

# IMPORTS
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy.stats import gaussian_kde

# === KLEURENMAP/PALETTE PER METHODE EN PER CLASSIFICATIE ===
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

# === PAD/LOCATIES PER CSV ===
base_dir = "results"
csv_files = {
    "CoT": os.path.join(base_dir, "cot", "appendix_metrics_table_cot.csv"),
    "FSL": os.path.join(base_dir, "fsl2", "appendix_metrics_table_fsl2.csv"),
    "ZSL": os.path.join(base_dir, "zsl2", "appendix_metrics_table_zsl2.csv"),
    "Pynguin": os.path.join(base_dir, "pynguin", "appendix_metrics_table_pynguin.csv"),
    "mbpp": os.path.join(base_dir, "mbpp", "appendix_metrics_table_mbpp.csv")
}
plots_dir = "results/comparison_plots"
if not os.path.exists(plots_dir):
    try:
        os.makedirs(plots_dir)
        print("Directory created:", plots_dir)
    except Exception as plot_folder_error:
        print("Could not create folder:", plots_dir, "\nError:", plot_folder_error)
else:
    print("Directory already exists:", plots_dir)

# INLEZEN & MERGEN VAN ALLE CSV's
dfs = []
for method, csv_path in csv_files.items():
    print(f"Trying to load CSV for method {method} from {csv_path} ...")
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path, sep=';')
            print(f"Loaded {len(df)} rows for method {method}")
            df['method'] = method
            # Verwijder ".py" uit programnaam als dat er nog in zit
            if 'Program' in df.columns:
                df['Program'] = df['Program'].astype(str).apply(lambda x: x.replace('.py',''))
            # Normalizeer kolomnamen/lege waarden (in jouw stijl!)
            for col in ['Mutation Score', 'Statement Coverage (%)', 'Assertion Count', 'Num Mutants', 'Test Time (s)', 'Test Suite Size']:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
            # Zet 'Detailed Classification' als hij niet bestaat
            if 'Detailed Classification' not in df.columns and 'Mutation Score' in df.columns:
                def detailed_split(mscore):
                    try:
                        if pd.isnull(mscore): return "Unknown"
                        if mscore == 0: return "Catastrophic"
                        if mscore >= 1 and mscore < 61: return "Partial"
                        if mscore >= 61 and mscore < 80: return "Near-miss"
                        if mscore >= 80: return "Well tested"
                        return "Unknown"
                    except: return "Unknown"
                df['Detailed Classification'] = df['Mutation Score'].apply(detailed_split)
            dfs.append(df)
        except Exception as read_err:
            print(f"Could not load/parse {csv_path}:", read_err)
    else:
        print("File not found:", csv_path)

if len(dfs)==0:
    print("No data loaded! Exiting.")
    exit()
else:
    print("Merging all dataframes into one (df_all) ...")
    df_all = pd.concat(dfs, ignore_index=True)
    print("All methods merged. Rows in df_all:", len(df_all))

# PLOT 1: Boxplot of Mutation Scores by Method (fixed median/outliers)
print("PLOT 1: Boxplot of Mutation Scores by Method (with corrected medians/outliers)")
plt.figure(figsize=(9,6))

if 'Mutation Score' not in df_all.columns or 'method' not in df_all.columns:
    print("Required columns missing.")
else:
    data_to_plot = []
    labels = []
    for method in csv_files.keys():
        subset = df_all[df_all['method']==method]['Mutation Score'].dropna().values
        data_to_plot.append(subset)
        labels.append(method)

    # Boxplot: expliciete instellingen
    box = plt.boxplot(data_to_plot, labels=labels, patch_artist=True,
                      showfliers=True,  # Belangrijk: toon ALLE outliers
                      boxprops=dict(edgecolor='black', linewidth=1.2),
                      medianprops=dict(color='red', linewidth=2),
                      whiskerprops=dict(color='black'),
                      capprops=dict(color='black'),
                      flierprops=dict(marker='o', markerfacecolor='black', markeredgecolor='black', markersize=5))

    # Handmatig kleuren per methode
    for i, patch in enumerate(box['boxes']):
        method = labels[i]
        patch.set_facecolor(method_color_map[method])
        patch.set_alpha(0.8)

    plt.ylabel("Mutation Score (%)")
    plt.xlabel("Method")
    plt.title("PLOT 1: Comparison of Mutation Scores by Method")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot1_boxplot.png"))
    plt.close()
    print("PLOT 1 saved as plot1_boxplot.png")

#  PLOT 2: Stacked Barplot of Test Classes per Method (with % annotation)
print("PLOT 2: Barplot of Test Classes per Method (stacked, with percentages)")
if 'Detailed Classification' not in df_all.columns or 'method' not in df_all.columns:
    print("Required columns not present.")
else:
    # Tellen per methode en klasse
    group_counts = df_all.groupby(['method','Detailed Classification']).size().unstack(fill_value=0)

    # Volgorde vastleggen
    class_order = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    if all([c in group_counts.columns for c in class_order]):
        group_counts = group_counts[class_order]

    # Totale programma’s per methode (voor %)
    total_per_method = group_counts.sum(axis=1)

    # Teksten voorbereiden (percentage op top van elke kleur)
    fig, ax = plt.subplots(figsize=(10,7))
    bottom = np.zeros(len(group_counts))
    for i, cls in enumerate(class_order):
        vals = group_counts[cls].values if cls in group_counts.columns else np.zeros(len(group_counts))
        b = ax.bar(group_counts.index, vals, bottom=bottom, label=cls, color=classification_color_map[cls])
        # Annotaties
        for j, val in enumerate(vals):
            if val > 0:
                percentage = (val / total_per_method.iloc[j]) * 100
                ax.text(j, bottom[j] + val/2, f"{percentage:.0f}%", ha='center', va='center', fontsize=9, color='black')
        bottom += vals

    ax.set_ylabel("Number of Programs")
    ax.set_xlabel("Method")
    ax.set_title("PLOT 2: Test Class Distribution per Method (with % labels)")
    ax.legend(title="Class")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot2_barplot.png"))
    plt.close()
    print("PLOT 2 saved as plot2_barplot.png")


# 3. Heatmap Strongly Tested (by Program × Method, with black grid lines)
print("PLOT 3: Heatmap Strongly Tested (by Program × Method, improved layout with black lines)")
if "Program" not in df_all.columns or "method" not in df_all.columns or "Detailed Classification" not in df_all.columns:
    print("Required columns missing.")
else:
    status_map = {"Well tested": 3, "Near-miss": 2, "Partial": 1, "Catastrophic": 0, "Unknown": np.nan}
    program_order = sorted(df_all['Program'].unique())
    method_order = ["CoT", "FSL", "ZSL", "Pynguin", "mbpp"]
    pivot = df_all.pivot_table(index="Program", columns="method", values="Detailed Classification", aggfunc='first').replace(status_map)
    pivot = pivot.reindex(index=program_order, columns=method_order)
    fig, ax = plt.subplots(figsize=(8, 13))
    # Custom pastel colors for better readability (same as other plots)
    from matplotlib.colors import ListedColormap, BoundaryNorm
    heat_colors = ["red", "orange", "yellow", "lightblue"]
    cmap = ListedColormap(heat_colors)
    norm = BoundaryNorm([-0.5,0.5,1.5,2.5,3.5], ncolors=4)
    im = ax.imshow(pivot, aspect='auto', cmap=cmap, norm=norm)
    # Draw black horizontal grid lines for each row
    for y in range(len(program_order)+1):
        ax.axhline(y-0.5, color='black', linewidth=0.3)
    # Draw vertical lines for method separation
    for x in range(len(method_order)+1):
        ax.axvline(x-0.5, color='black', linewidth=0.3)
    # Set ticks/labels
    ax.set_yticks(np.arange(len(program_order)))
    ax.set_yticklabels(program_order, fontsize=6)
    ax.set_xticks(np.arange(len(method_order)))
    ax.set_xticklabels(method_order, fontsize=10)
    ax.set_xlabel("Method")
    ax.set_ylabel("Program")
    # Custom legend
    legend_patches = [
        mpatches.Patch(color='lightblue', label='Well tested (3)'),
        mpatches.Patch(color='yellow', label='Near-miss (2)'),
        mpatches.Patch(color='orange', label='Partial (1)'),
        mpatches.Patch(color='red', label='Catastrophic (0)')
    ]
    ax.legend(handles=legend_patches, bbox_to_anchor=(1.03, 1), loc='upper left', fontsize=9)
    # Tight colorbar
    cbar = plt.colorbar(im, ax=ax, ticks=[0,1,2,3], shrink=0.5)
    cbar.ax.set_yticklabels(['Catastrophic', 'Partial', 'Near-miss', 'Well tested'])
    cbar.set_label("Test Class", rotation=270, labelpad=18)
    plt.title("Strongly Tested Status by Program and Method")
    plt.tight_layout(rect=[0, 0, 0.90, 1])  # leave space for legend
    plt.savefig(os.path.join(plots_dir, "plot3_heatmap.png"))
    plt.close()
    print("PLOT 3 saved as plot3_heatmap.png")

# 4. Boxplot of Statement Coverage by Method (methodekleuren)
print("PLOT 4: Boxplot of Statement Coverage by Method")
if 'Statement Coverage (%)' in df_all.columns and 'method' in df_all.columns:
    data_to_plot = [df_all[df_all['method']==m]['Statement Coverage (%)'].dropna().values for m in csv_files.keys()]
    plt.figure(figsize=(9,6))
    bp = plt.boxplot(data_to_plot, labels=csv_files.keys(), patch_artist=True,
                boxprops=dict(facecolor='white', edgecolor='black'),
                medianprops=dict(color='red'))
    # Kleur boxen juist
    for patch, method in zip(bp['boxes'], csv_files.keys()):
        patch.set_facecolor(method_color_map[method])
        patch.set_alpha(0.8)
    plt.ylabel("Statement Coverage (%)")
    plt.xlabel("Method")
    plt.title("Comparison of Statement Coverage by Method")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot4_boxplot.png"))
    plt.close()
    print("PLOT 4 saved as plot4_boxplot.png")
else:
    print("Required columns not present for statement coverage plot.")


# 5. Scatterplot: Mutation Score vs. Statement Coverage, by Method
print("PLOT 5: Scatterplot Mutation Score vs Statement Coverage by Method")
if 'Statement Coverage (%)' in df_all.columns and 'Mutation Score' in df_all.columns and 'method' in df_all.columns:
    plt.figure(figsize=(9,7))
    for m in csv_files.keys():
        sub = df_all[df_all['method']==m]
        plt.scatter(sub['Statement Coverage (%)'], sub['Mutation Score'],
                    color=method_color_map[m], label=m, alpha=0.75)
    plt.xlabel('Statement Coverage (%)')
    plt.ylabel('Mutation Score (%)')
    plt.title('Mutation Score vs. Statement Coverage by Method')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot5_scatter.png"))
    plt.close()
    print("PLOT 5 saved as plot5_scatter.png")
else:
    print("Required columns not present for scatterplot mutation vs coverage.")

# 6. Outlier Stripplot: Catastrophic and Partial Failures Across Methods
print("PLOT 6: Outlier Stripplot: Failures <80% Mutation Score")
if 'Mutation Score' in df_all.columns and 'method' in df_all.columns and 'Program' in df_all.columns:
    failures = df_all[df_all['Mutation Score'] < 80]
    plt.figure(figsize=(15,6))
    methods = list(csv_files.keys())
    for m in methods:
        sub = failures[failures['method']==m]
        plt.scatter(sub['Program'], sub['Mutation Score'], label=m, alpha=0.8, s=60, c=method_color_map[m])
    plt.xticks(rotation=90, fontsize=8)
    plt.ylabel('Mutation Score (%)')
    plt.xlabel('Program')
    plt.title('Catastrophic and Partial Failures Across Methods')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot6_stripplot.png"))
    plt.close()
    print("PLOT 6 saved as plot6_stripplot.png")
else:
    print("Required columns not present for outlier stripplot.")

# 7. Boxplot: Generation/Execution Time by Method
print("PLOT 7: Boxplot Generation/Execution Time by Method")
if 'Test Time (s)' in df_all.columns and 'method' in df_all.columns:
    plt.figure(figsize=(9,6))
    data_to_plot = [df_all[df_all['method']==m]['Test Time (s)'].dropna().values for m in csv_files.keys()]
    plt.boxplot(data_to_plot, labels=csv_files.keys(), patch_artist=True,
                boxprops=dict(facecolor='white', edgecolor='black'),
                medianprops=dict(color='red'))
    for patch, method in zip(plt.gca().artists, csv_files.keys()):
        patch.set_facecolor(method_color_map[method])
        patch.set_alpha(0.8)
    plt.ylabel("Test Time (s)")
    plt.xlabel("Method")
    plt.title("Test Execution Time by Method")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot7_boxplot.png"))
    plt.close()
    print("PLOT 7 saved as plot7_boxplot.png")
else:
    print("Required columns not present for test time boxplot.")

# 8. Scatterplot: Mutation Score vs. Assertion Count, by Method
print("PLOT 8: Scatterplot Mutation Score vs Assertion Count, by Method")
if 'Assertion Count' in df_all.columns and 'Mutation Score' in df_all.columns and 'method' in df_all.columns:
    plt.figure(figsize=(9,7))
    for m in csv_files.keys():
        sub = df_all[df_all['method']==m]
        plt.scatter(sub['Assertion Count'], sub['Mutation Score'],
                    color=method_color_map[m], label=m, alpha=0.75)
    plt.xlabel('Assertion Count')
    plt.ylabel('Mutation Score (%)')
    plt.title('Mutation Score vs. Assertion Count by Method')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot8_scatter.png"))
    plt.close()
    print("PLOT 8 saved as plot8_scatter.png")
else:
    print("Required columns not present for assertion count scatterplot.")

# 9. Spaghetti Plot: Mutation Scores Across Methods
print("PLOT 9: Program-by-Program Spaghetti Plot Across Methods")
if 'Program' in df_all.columns and 'method' in df_all.columns and 'Mutation Score' in df_all.columns:
    pivot = df_all.pivot(index='Program', columns='method', values='Mutation Score')
    plt.figure(figsize=(14,9))
    for idx, row in pivot.iterrows():
        plt.plot(pivot.columns, row.values, marker='o', alpha=0.6, linewidth=1)
    for m in csv_files.keys():
        plt.scatter([m]*len(pivot), pivot[m].values, color=method_color_map[m], label=m, s=30)
    plt.ylabel('Mutation Score (%)')
    plt.xlabel('Method')
    plt.title('Mutation Score per Program Across Methods')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot9_spaghetti.png"))
    plt.close()
    print("PLOT 9 saved as plot9_spaghetti.png")
else:
    print("Required columns not present for spaghetti plot.")

# 10. Stacked Histogram (True Counts) + KDE: Mutation Score Distribution
print("PLOT 10: Stacked Mutation Score Distribution by Method (+KDE, True Counts)")
if 'Mutation Score' in df_all.columns and 'method' in df_all.columns:
    plt.figure(figsize=(14,8))
    bins = np.arange(0, 110, 10)  # 0, 10, ..., 100
    method_palette = {
        "CoT": "lightblue",
        "FSL": "yellow",
        "ZSL": "orange",
        "Pynguin": "grey",
        "mbpp": "green"
    }
    # Compute hist for each method
    hist_counts = []
    for m in csv_files.keys():
        vals = df_all[df_all['method']==m]['Mutation Score'].dropna()
        counts, _ = np.histogram(vals, bins=bins)
        hist_counts.append(counts)
    # Stack bars (bottoms)
    bottoms = np.zeros(len(bins)-1)
    labels_drawn = set()
    for i, m in enumerate(csv_files.keys()):
        label = m if m not in labels_drawn else None
        plt.bar(bins[:-1], hist_counts[i], width=10, align='edge',
                bottom=bottoms, color=method_palette[m], edgecolor='black', label=label)
        # Numbers on bars
        for j, val in enumerate(hist_counts[i]):
            if val > 0:
                plt.text(bins[j]+5, bottoms[j]+val/2, str(val), ha='center', va='center', fontsize=9)
        bottoms += hist_counts[i]
        labels_drawn.add(m)
    # KDE overlay per method
    for m in csv_files.keys():
        vals = df_all[df_all['method']==m]['Mutation Score'].dropna()
        if len(vals) > 2:
            from scipy.stats import gaussian_kde
            kde = gaussian_kde(vals)
            xvals = np.linspace(0, 100, 200)
            plt.plot(xvals, kde(xvals)*len(vals)*10, color=method_palette[m], linewidth=2, alpha=0.8, label=f"{m} KDE")
    plt.xlabel("Mutation Score (%)")
    plt.ylabel("Number of Programs")
    plt.title("Stacked Mutation Score Distribution by Method (+KDE, True Counts)")
    handles, labels = plt.gca().get_legend_handles_labels()
    # Move KDE lines to the end of the legend
    new_handles, new_labels = [], []
    for m in csv_files.keys():
        new_handles.append(handles[labels.index(m)])
        new_labels.append(m)
    for m in csv_files.keys():
        label_kde = f"{m} KDE"
        if label_kde in labels:
            new_handles.append(handles[labels.index(label_kde)])
            new_labels.append(label_kde)
    plt.legend(new_handles, new_labels, loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot10_stackedbar.png"))
    plt.close()
    print("PLOT 10 saved as plot10_stackedbar.png")
else:
    print("Required columns not present for mutation score histogram.")

# 11. Barplot: Catastrophic Failures per Method
print("PLOT 11: Barplot Catastrophic Failures per Method (methodkleuren)")
if 'Mutation Score' in df_all.columns and 'method' in df_all.columns:
    catastrophic_counts = df_all[df_all['Mutation Score'] == 0].groupby('method').size().reindex(csv_files.keys(), fill_value=0)
    plt.figure(figsize=(8,5))
    bar_colors = [method_color_map[m] for m in catastrophic_counts.index]
    bars = plt.bar(catastrophic_counts.index, catastrophic_counts.values, color=bar_colors)
    for i, v in enumerate(catastrophic_counts.values):
        plt.text(i, v+0.3, str(v), ha='center', color='black', fontsize=12)
    plt.ylabel('Number of Catastrophic Failures (0%)')
    plt.xlabel('Method')
    plt.title('Catastrophic Failures by Method')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot11_barplot.png"))
    plt.close()
    print("PLOT 11 saved as plot11_barplot.png")
else:
    print("Required columns not present for catastrophic barplot.")


# 12. UpSet plot: Overlap “Well Tested” programs by Method
print("PLOT 12: UpSet Plot: Overlap of Well Tested Programs (4 methods)")
try:
    from upsetplot import UpSet, from_memberships
    well_sets = {}
    for m in csv_files.keys():
        well_sets[m] = set(df_all[(df_all['method']==m)&(df_all['Detailed Classification']=='Well tested')]['Program'])
    # Maak lijst memberships
    all_programs = set()
    for s in well_sets.values():
        all_programs |= s
    memberships = []
    for prog in all_programs:
        present = tuple(m for m in csv_files.keys() if prog in well_sets[m])
        memberships.append(present)
    # Build upset data
    upset_data = from_memberships(memberships)
    plt.figure(figsize=(11,7))
    UpSet(upset_data, subset_size='count', show_counts=True).plot()
    plt.suptitle("UpSet Plot: Overlap of Well Tested Programs by Method")
    plt.savefig(os.path.join(plots_dir, "plot12_upset.png"))
    plt.close()
    print("PLOT 12 saved as plot12_upset.png")
except ImportError:
    print("upsetplot not installed. Skipping UpSet plot.")

# 13. Correlation Heatmap per Method
print("PLOT 13: Correlation Heatmap per Method (manual, for each method)")
numeric_cols = ["Mutation Score", "Statement Coverage (%)", "Test Time (s)", "Assertion Count", "Num Mutants"]
for m in csv_files.keys():
    sub = df_all[df_all['method']==m][numeric_cols].copy()
    sub = sub.dropna(axis=0, how='any')
    if len(sub) < 2:
        print(f"Not enough data for method {m} to compute correlation matrix.")
        continue
    corr = sub.corr()
    fig, ax = plt.subplots(figsize=(7,6))
    cax = ax.matshow(corr, cmap='Blues', vmin=-1, vmax=1)
    plt.title(f"Correlation Heatmap ({m})", pad=25)
    plt.xticks(range(len(numeric_cols)), numeric_cols, rotation=45, ha='left', fontsize=9)
    plt.yticks(range(len(numeric_cols)), numeric_cols, fontsize=9)
    fig.colorbar(cax)
    # Annotate
    for i in range(len(numeric_cols)):
        for j in range(len(numeric_cols)):
            val = corr.iloc[i, j]
            ax.text(j, i, f"{val:.2f}", va='center', ha='center', color='black', fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, f"plot13_correlation{m}.png"))
    plt.close()
    print(f"PLOT 13 saved as plot13_correlation{m}.png")

# 14. Boxplot Assertion Density per Method
print("PLOT 14: Boxplot Assertion Density (assertions per test) per Method")
if "Assertion Count" in df_all.columns and "Test Suite Size" in df_all.columns:
    df_all["assertion_density"] = df_all["Assertion Count"] / df_all["Test Suite Size"].replace(0, np.nan)
    data_to_plot = [df_all[df_all['method']==m]['assertion_density'].dropna().values for m in csv_files.keys()]
    plt.figure(figsize=(9,6))
    bp = plt.boxplot(data_to_plot, labels=csv_files.keys(), patch_artist=True,
                boxprops=dict(facecolor='white', edgecolor='black'),
                medianprops=dict(color='red'))
    # Geef elke box de kleur van de methode (zoals in de andere plots)
    for patch, method in zip(bp['boxes'], csv_files.keys()):
        patch.set_facecolor(method_color_map[method])
        patch.set_alpha(0.85)
    plt.ylabel("Assertion Density (assertions per test)")
    plt.xlabel("Method")
    plt.title("Assertion Density by Method")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot14_boxplot_assertion.png"))
    plt.close()
    print("PLOT 14 saved as plot14_boxplot_assertion.png")
else:
    print("Required columns not present for assertion density boxplot.")


# 15. Efficiency Scatterplot: Mutation Score vs Kills per Second
print("PLOT 15: Efficiency Scatterplot: Mutation Score vs Kills per Second")
if "Num Mutants" in df_all.columns and "Test Time (s)" in df_all.columns and "Mutation Score" in df_all.columns and "method" in df_all.columns:
    plt.figure(figsize=(10,7))
    for m in csv_files.keys():
        sub = df_all[df_all['method']==m]
        x = sub["Num Mutants"] / sub["Test Time (s)"].replace(0, np.nan)
        y = sub["Mutation Score"]
        plt.scatter(x, y, label=m, color=method_color_map[m], alpha=0.7)
    plt.xlabel("Mutants per Second")
    plt.ylabel("Mutation Score (%)")
    plt.title("Efficiency: Mutation Score vs Mutants per Second")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot15_efficiency_scatter.png"))
    plt.close()
    print("PLOT 15 saved as plot15_efficiency_scatter.png")
else:
    print("Required columns not present for efficiency scatterplot.")

#  16. Boxplot Assertion Density (assertions per LoC) per Method
print("PLOT 16: Boxplot Assertion Density (assertions per LoC) per Method")
if "Assertion Count" in df_all.columns and "Statement Coverage (%)" in df_all.columns:
    df_all["assertion_density_loc"] = df_all["Assertion Count"] / df_all["Statement Coverage (%)"].replace(0, np.nan)
    data_to_plot = [df_all[df_all['method']==m]['assertion_density_loc'].dropna().values for m in csv_files.keys()]
    plt.figure(figsize=(9,6))
    bp = plt.boxplot(data_to_plot, labels=csv_files.keys(), patch_artist=True,
                     medianprops=dict(color='red'))
    method_palette = {
        "CoT": "lightblue",
        "FSL": "yellow",
        "ZSL": "orange",
        "Pynguin": "grey",
        "mbpp": 'green'
    }
    for patch, method in zip(bp['boxes'], csv_files.keys()):
        patch.set_facecolor(method_palette[method])
        patch.set_alpha(0.85)
    plt.ylabel("Assertion Density (assertions per LoC)")
    plt.xlabel("Method")
    plt.title("Assertion Density by Method (per LoC)")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot16_boxplot_loc.png"))
    plt.close()
    print("PLOT 16 saved as plot16_boxplot_loc.png")
else:
    print("Required columns not present for assertion density per LoC.")


# 17. Stacked Bar (Failure-Type Distribution per Method, normalized + % labels)
print("PLOT 17: Stacked Bar Failure-Type Distribution per Method (normalized)")
if "Detailed Classification" in df_all.columns:
    group_counts = df_all.groupby(['method','Detailed Classification']).size().unstack(fill_value=0)
    normed = group_counts.div(group_counts.sum(axis=1), axis=0)
    class_order = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    normed = normed[class_order] if all([c in normed.columns for c in class_order]) else normed
    bottom = np.zeros(len(normed))
    fig, ax = plt.subplots(figsize=(10,7))
    bars = []
    for i, cls in enumerate(class_order):
        vals = normed[cls].values if cls in normed.columns else np.zeros(len(normed))
        bar = ax.bar(normed.index, vals, bottom=bottom, label=cls, color=classification_color_map[cls])
        bars.append(bar)
        # Voeg % labels toe binnen elk segment
        for j, v in enumerate(vals):
            if v > 0.01:
                ax.text(j, bottom[j] + v/2, f"{v*100:.0f}%", ha='center', va='center', color='black', fontsize=11)
        bottom += vals
    ax.set_ylabel("Fraction of Programs")
    ax.set_xlabel("Method")
    ax.set_title("Normalized Failure-Type Distribution per Method")
    ax.legend(title="Class")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot17_stackedbar.png"))
    plt.close()
    print("PLOT 17 saved as plot17_stackedbar.png")
else:
    print("Detailed Classification column not found, skipping PLOT 17")


# 8. Scatterplot Generation Time vs Mutation Score by Method
print("PLOT 18: Scatterplot Generation Time vs Mutation Score by Method")
if "Test Time (s)" in df_all.columns and "Mutation Score" in df_all.columns and "method" in df_all.columns:
    plt.figure(figsize=(10,7))
    for m in csv_files.keys():
        sub = df_all[df_all['method']==m]
        plt.scatter(sub["Test Time (s)"], sub["Mutation Score"], label=m, color=method_color_map[m], alpha=0.7)
    plt.xlabel("Test Time (s)")
    plt.ylabel("Mutation Score (%)")
    plt.title("Test Time vs Mutation Score by Method")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot18_scatter.png"))
    plt.close()
    print("PLOT 18 saved as plot18_scatter.png")
else:
    print("Required columns not present for time vs mutation score scatterplot.")

# 19. Venn diagram: Well-Tested overlap (CoT, FSL, ZSL)
print("PLOT 19: Venn diagram – Well-Tested overlap (CoT, FSL, ZSL)")
try:
    from matplotlib_venn import venn3
    venn_methods = ["CoT", "FSL", "ZSL"]
    venn_sets = [set(df_all[(df_all["method"] == m) &
                            (df_all["Detailed Classification"] == "Well tested")]
                     ["Program"])
                 for m in venn_methods]

    plt.figure(figsize=(9, 9))
    v = venn3(venn_sets, set_labels=venn_methods)

    # colour the single-method circles
    venn_fill = [method_color_map[m] for m in venn_methods]
    for pid, col in zip(["100", "010", "001"], venn_fill):
        if v.get_patch_by_id(pid):
            v.get_patch_by_id(pid).set_color(col)
            v.get_patch_by_id(pid).set_alpha(0.7)

    plt.title("Overlap of Well-Tested Programs: CoT, FSL, ZSL")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir,
                 "plot19_venn.png"))
    plt.close()
    print("PLOT 19 saved as plot19_venn.png")
except ImportError:
    print("matplotlib-venn not installed → skipping PLOT 19.")


# 20. Stacked Histogram (Percentages) + KDE: Mutation-Score distribution
print("PLOT 20: Stacked Mutation-Score distribution by Method (+KDE, %)")

if {"Mutation Score", "method"}.issubset(df_all.columns):
    plt.figure(figsize=(14, 8))

    bins = np.arange(0, 110, 10)                       # 0,10,…,100
    bottoms = np.zeros(len(bins) - 1)
    labels_drawn = set()
    palette20 = {"CoT": "lightblue", "FSL": "yellow",
                 "ZSL": "orange",   "Pynguin": "grey",
                 "mbpp": "green"}

    # stacked bars (%)
    for m in csv_files.keys():
        vals = df_all[df_all["method"] == m]["Mutation Score"].dropna()
        counts, _ = np.histogram(vals, bins=bins)
        heights = counts / len(vals) * 100              # convert to %

        label = m if m not in labels_drawn else None
        plt.bar(bins[:-1], heights, width=10, align="edge",
                bottom=bottoms, color=palette20[m],
                edgecolor="black", label=label)

        # % labels inside bars
        for j, h in enumerate(heights):
            if h > 0:
                plt.text(bins[j] + 5, bottoms[j] + h / 2,
                         f"{h:.0f}%", ha="center", va="center", fontsize=9)
        bottoms += heights
        labels_drawn.add(m)

    # KDE overlays
    for m in csv_files.keys():
        vals = df_all[df_all["method"] == m]["Mutation Score"].dropna()
        if len(vals) > 2:
            kde = gaussian_kde(vals)
            xs = np.linspace(0, 100, 200)
            scale = 10 * 100                           # bin-width ×100
            plt.plot(xs, kde(xs) * scale, lw=2, alpha=.8,
                     color=palette20[m], label=f"{m} KDE")

    # cosmetics
    plt.xlabel("Mutation Score (%)")
    plt.ylabel("Percentage of Programs")
    plt.title("Stacked Mutation-Score Distribution by Method (+KDE, %)")
    # reorder legend → bars first, KDE lines second
    h, l = plt.gca().get_legend_handles_labels()
    ordered_h, ordered_l = [], []
    for m in csv_files.keys():
        ordered_h.append(h[l.index(m)])
        ordered_l.append(m)
    for m in csv_files.keys():
        lk = f"{m} KDE"
        if lk in l:
            ordered_h.append(h[l.index(lk)])
            ordered_l.append(lk)
    plt.legend(ordered_h, ordered_l, loc="upper left")

    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir,
                 "plot20_stackedbar.png"))
    plt.close()
    print("PLOT 20 saved as plot20_stackedbar.png")
else:
    print("Required columns missing → skipping PLOT 20.")


# 21. Violin Plot: Mutation-Score by Test-Class
print("PLOT 21: Violin plot – Mutation-Score by Test Class")

if {"Detailed Classification", "Mutation Score"}.issubset(df_all.columns):
    class_order  = ["Well tested", "Near-miss", "Partial", "Catastrophic"]
    color_order  = [classification_color_map[c] for c in class_order]
    data         = [df_all[df_all["Detailed Classification"] == c]
                    ["Mutation Score"].dropna().values for c in class_order]

    plt.figure(figsize=(10, 6))
    parts = plt.violinplot(data, positions=range(1, 5), widths=0.7,
                           showmedians=True, showextrema=True)

    # colour each violin
    for i, body in enumerate(parts['bodies']):
        body.set_facecolor(color_order[i])
        body.set_edgecolor("black")
        body.set_alpha(0.8)
    if 'cmedians' in parts:            # white median lines
        parts['cmedians'].set_color("white")
        parts['cmedians'].set_linewidth(2)

    plt.xticks(range(1, 5), class_order)
    plt.ylabel("Mutation Score (%)")
    plt.xlabel("Test Class")
    plt.title("Mutation-Score Distribution by Test Class (All Methods)")
    legend_elems = [mpatches.Patch(color=color_order[i], label=class_order[i])
                    for i in range(4)]
    plt.legend(handles=legend_elems, loc="best")

    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir,
                 "plot21_violinplot.png"))
    plt.close()
    print("PLOT 21 saved as plot21_violinplot.png")
else:
    print("Required columns missing → skipping PLOT 21.")

# 22. Barplot – number of programs per method
print("PLOT 22: Barplot – number of programs per method")

if "method" in df_all.columns:
    # One row per program ⇒ row-count gives total test-suites
    prog_counts = (df_all.groupby("method")
                         .size()
                         .reindex(csv_files.keys(), fill_value=0))

    plt.figure(figsize=(8, 6))
    bar_cols = [method_color_map[m] for m in prog_counts.index]
    bars = plt.bar(prog_counts.index, prog_counts.values, color=bar_cols)

    # annotate bar heights
    for idx, val in enumerate(prog_counts.values):
        plt.text(idx, val + 0.5, f"{val}", ha="center", va="bottom", fontsize=11)

    plt.ylabel("Number of Programs (Test Suites)")
    plt.xlabel("Method")
    plt.title("Total Programs Processed per Method")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "plot22_barplot.png"))
    plt.close()
    print("PLOT 22 saved as plot22_barplotpng")
else:
    print("'method' column not found → skipping PLOT 22.")


print("All comparison plots saved in folder:", plots_dir)
