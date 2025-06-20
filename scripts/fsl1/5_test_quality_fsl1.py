"""
This script reads filtered mutation result YAML files from a specific folder,
classifies each program based on its mutation score, and exports a summary to a CSV file.
It is intended for quick analysis of program test quality.
"""

# IMPORTS
import os  # File and directory operations
import yaml  # For reading YAML files.
import csv  # For CSV reading.

# PATHS
fsl1_input_folder = "results/fsl1/filtered_mutation_results"
print("Set input folder for YAML files:", fsl1_input_folder)
csv_path_output = "results/fsl1/classification_summary_fsl1.csv"
print("CSV output file will be saved as:", csv_path_output)

list_files = []
yaml_file_list = []
result_list = []
threshold = 80.0

print("Checking if input folder exists:", fsl1_input_folder)
if os.path.exists(fsl1_input_folder):
    folder_check_present = True
    print("Input folder present:", fsl1_input_folder)
else:
    print("Input folder not found:", fsl1_input_folder)
    print("ERROR: Input folder must exist or the script cannot continue.")
    assert os.path.exists(fsl1_input_folder)

# List files
print("Reading files from the input folder...")
for file_x in os.listdir(fsl1_input_folder):
    list_files.append(file_x)

print("Filtering YAML files ending with _report.yaml...")
for filename_tmp in list_files:
    if filename_tmp.endswith("_report.yaml"):
        yaml_file_list.append(filename_tmp)

# Process all YAML files and classify them by mutation score.
print("Start processing ALL YAML files with universal for-loop...")
file_index = 0
for y_file in yaml_file_list:
    file_index += 1
    print(f"\n=== Start processing file {file_index}: {y_file} ===")
    try:
        full_path = fsl1_input_folder + "/" + y_file
        program_id = y_file.split("_")[1]  # e.g., gets '003' from program_003_report.yaml
        print("ProgramID extracted from filename:", program_id)

        # Universal YAML loader to ignore strange python tags
        class YAMLIgnoreAll(yaml.SafeLoader):
            """
            YAML loader to ignore all python-like tags (for student YAML files).
            """
            pass

        def ignore_any(loader, tag_suffix, node):
            """
            Ignores any Python-specific YAML tag during loading.
            """
            return None

        YAMLIgnoreAll.add_multi_constructor("tag:yaml.org,2002:python/", ignore_any)

        with open(full_path, "r") as fd:
            y_data = yaml.load(fd, Loader=YAMLIgnoreAll)
        if y_data is None:
            print("WARNING: y_data is None after loading, set empty dict.")
            y_data = {}

        mutation_score = y_data.get("mutation_score", 0.0)
        print("Mutation score found:", mutation_score)

        classification_x = "Well tested" if mutation_score >= threshold else "Weakly tested"
        print("Classification for this file:", classification_x)

        result_dict = {
            "Program": "program_" + str(program_id),
            "Mutation Score": mutation_score,
            "Classification": classification_x
        }
        result_list.append(result_dict)
    except Exception as err_yaml:
        print("Error during processing of", y_file, ":", err_yaml)
        assert False

print("Finished processing YAML files.")
print("Number of program results in result_list:", len(result_list))

# Write result to CSV
print("Exporting result to CSV:", csv_path_output)
try:
    column_list = ["Program", "Mutation Score", "Classification"]
    extra_col_remark = False
    for rr in result_list:
        if "Remark" in rr:
            extra_col_remark = True
    if extra_col_remark:
        column_list.append("Remark")
    # B: Only open/write to the CSV file once per run
    with open(csv_path_output, "w", newline='', encoding="utf-8-sig") as cfile:
        writer = csv.DictWriter(cfile, fieldnames=column_list, delimiter=';')
        writer.writeheader()
        for rr in result_list:
            writer.writerow(rr)
    print("CSV saved at:", csv_path_output)
except Exception as err_export:
    print("Error exporting to CSV:", err_export)
    assert False