"""
This script processes YAML report files, summarizes mutation testing results, writes a CSV summary, and creates a bar plot.
It creates output directories if needed, reads and checks YAML files, and saves results for each program.
"""

# IMPORTS
import os  # File and directory operations
import json  # JSON parsing
import csv  # CSV output
import matplotlib.pyplot as plt  # For plotting
import yaml

# PATHS
out_dir_zsl = "results/zsl/filtered_mutation_results"
result_csv_path = os.path.join(out_dir_zsl, "mutation_summary_zsl.csv")
debug_log_file = os.path.join(out_dir_zsl, "report_debug_log.txt")

# GLOBAL VARIABLES
n_report_files_xyz = 0
all_data_reports = []
list_report_files = []

# OUTPUT DIR CHECK & CREATION
# Create output dir if it doesn't exist
if not os.path.exists(out_dir_zsl):
    os.makedirs(out_dir_zsl, exist_ok=True)
    print("Output directory created:", out_dir_zsl)
else:
    print("Output directory already exists:", out_dir_zsl)

# YAML FILE READER
def read_yaml_file(yaml_file_path):
    """
    Read a YAML file and return a dictionary.
    Returns None if there is an error.
    """
    try:
        with open(yaml_file_path, "r", encoding="utf-8") as ff:
            result_dict = yaml.unsafe_load(ff)
        return result_dict
    except Exception as error:
        print("Error reading YAML:", yaml_file_path)
        print("Error message:", error)
        return None

# WRITE DEBUG LOG & FIND REPORTS
# create debug log file
with open(debug_log_file, 'w', encoding='utf-8') as log_file:
    print("Debug log file opened.")
    # Search for report files
    for random_report_file in os.listdir(out_dir_zsl):
        # Only look for files that match
        if random_report_file.startswith("program_") and random_report_file.endswith("_report.yaml"):
            list_report_files.append(os.path.join(out_dir_zsl, random_report_file))
    n_report_files_xyz = len(list_report_files)
    print("Number of report files found:", n_report_files_xyz)
    if n_report_files_xyz == 0:
        print("WARNING: No report files found!")
    for ind_var in range(n_report_files_xyz):
        report_path = list_report_files[ind_var]
        base_name = os.path.basename(report_path)
        program_name = "program_" + base_name.split("_")[1]
        program_number = base_name.split("_")[1]
        log_file.write("\n=== " + base_name + " ===\n")
        try:
            report_dict = read_yaml_file(report_path)
        except Exception as error:
            print("Problem reading YAML:", report_path)
            print("Error message:", error)
            log_file.write("YAML read error: " + str(error) + "\n")
            report_dict = None
            continue
        if not isinstance(report_dict, dict):
            log_file.write("Wrong data type: " + str(type(report_dict)) + "\n")
            continue
        mutations_list = report_dict.get("mutations", [])
        if isinstance(mutations_list, str):
            try:
                mutations_list = json.loads(mutations_list)
            except Exception:
                mutations_list = []
        if not isinstance(mutations_list, list):
            log_file.write("mutations not a list\n")
            continue
        total_mutations = 0
        n_killed = 0
        n_survived = 0
        n_timeouts = 0
        for mutation in mutations_list:
            total_mutations += 1
            if isinstance(mutation, dict):
                if mutation.get("status") == "killed":
                    n_killed += 1
                if mutation.get("status") == "survived":
                    n_survived += 1
                if mutation.get("status") == "timeout":
                    n_timeouts += 1

        try:
            if total_mutations > 0:
                if "mutation_score" in report_dict:
                    mutation_score = report_dict.get("mutation_score")
                else:
                    mutation_score = round((n_killed / total_mutations) * 100, 2)
            else:
                mutation_score = 0.0
        except Exception as error:
            print("Problem with mutation_score!", error)
            mutation_score = 0.0
        result_dict = {}
        result_dict["Program"] = program_name
        result_dict["Total"] = total_mutations
        result_dict["Killed"] = n_killed
        result_dict["Survived"] = n_survived
        result_dict["Timeout"] = n_timeouts
        result_dict["Mutation Score (%)"] = round(mutation_score, 2)
        all_data_reports.append(result_dict)
        assert isinstance(all_data_reports[-1], dict)
    log_file.write("\nAll processed.\n")
    print("All reports processed.")

# CHECK IF DATA EXISTS
if len(all_data_reports) == 0:
    print("No results found (see log).")
    print("Script stops: no data.")
    exit(1)
else:
    print("Data found. Continue processing...")

# CSV OUTPUT
try:
    print("Saving results to CSV...")
    column_names = ["Program", "Total", "Killed", "Survived", "Timeout", "Mutation Score (%)"]
    all_data_reports_sorted = sorted(all_data_reports, key=lambda xx: xx["Program"])
    # write the result CSV
    with open(result_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=column_names, delimiter=';')
        writer.writeheader()
        for row in all_data_reports_sorted:
            writer.writerow(row)
    print("Summary saved as:", result_csv_path)
    assert len(all_data_reports_sorted) > -1
except Exception as error:
    print("Error writing CSV:", error)

print("Script finished. Results processed:", len(all_data_reports))