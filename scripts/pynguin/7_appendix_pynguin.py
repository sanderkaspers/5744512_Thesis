"""
This script loads mutation testing results and manual comments, processes metrics per program,
and saves a summary table as CSV. It checks for missing files and cleans YAML input for parsing.
"""

# IMPORTS
import os    # For checking if files exist.
import pandas as pd   # For reading CSV and using dataframes.
import re     # Regex for cleaning up YAML files with Python tags.
import yaml  # For parsing test results in YAML format.
import json   # For loading manual comments.

# PATHS
classification_csv_path = 'results/pynguin/classification_summary_pynguin.csv'  # Path to classification csv file.
filtered_mutation_dir = 'results/pynguin/filtered_mutation_results' # Directory with all mutation YAML files.
manual_comments_file = 'data/manual_comments_pynguin.json'   # JSON file for manual comments.
metrics_table_csv = 'results/pynguin/appendix_metrics_table_pynguin.csv' # Output CSV for all gathered metrics.

# GLOBAL VARIABLES
df_classification = None   # DataFrame for classification data.
manual_comments = {}  # Dictionary for manual comments.
manual_comments_exists = False  # Indicates if the manual comments JSON exists.
results_list = []  # List of result dicts for each program.
test_time = None  # Test time per program (from YAML)
num_tests = None     # Number of tests (from YAML)
num_mutants = None   # Number of mutants in the YAML file
num_asserts = None    # Number of asserts/tracebacks, None until calculated
tmp_dict = None # Temporary dict for each program
yaml_path = ""      # Path to the YAML file per program
yaml_text = ""   # Cleaned YAML file as string
yaml_dict = None  # Dictionary after parsing YAML
program_name = ""   # Name of the program (from CSV), set in each loop
mutation_score = None    # Mutation score from CSV
classification_label = ""  # Classification label from CSV
manual_comment = ""    # Manual comment, default empty unless found
yaml_file_exists = False  # Indicates if the YAML file exists
mutant_list = []   # All mutants in a list per YAML file
save_success = False    # Indicates if saving CSV succeeded

def check_if_classification_file_exists():
    """
    Checks if the classification CSV file exists, and stops the script if not found.
    """

    print("Checking if classification file exists...")
    assert os.path.exists(classification_csv_path)
    print("Classification file found.")

# DATA LOADING
print("Trying to load classification data (df_classification)…")
try:
    df_classification = pd.read_csv(classification_csv_path)  # Load CSV as pandas DataFrame.
    print("Classification CSV found & loaded (df_classification).")
    print("Number of rows in classification file:", len(df_classification))
except Exception as classification_load_error:
    print("Could not load classification CSV:", classification_load_error)
    print("Note: df_classification remains empty (None).")

# Check if manual comments file exists.
print("Checking if manual comments file exists…")
manual_comments_exists = os.path.exists(manual_comments_file)
if manual_comments_exists:
    print("Manual comments file found, attempting to load.")
    try:
        with open(manual_comments_file, "r", encoding="utf-8") as json_file:
            manual_comments = json.load(json_file)
        print("Manual comments JSON loaded successfully (manual_comments).")
        print("Number of manual comments loaded:", len(manual_comments))
    except Exception as manual_comments_load_error:
        print("Could not load manual comments JSON:", manual_comments_load_error)
        print("manual_comments remains empty.")
else:
    print("Note: manual comments JSON missing (not a problem, continue).")
    print("manual_comments remains empty.")

# YAML CLEANING FUNCTION
def clean_yaml(yaml_filepath):
    """
    Cleans the given YAML file by removing Python-specific tags, so the file can be read safely.
    Returns the cleaned text as a string. Returns an empty string if reading fails.
    """
    print("clean_yaml started for file:", yaml_filepath)
    lines_out = []
    try:
        with open(yaml_filepath, "r", encoding="utf-8") as f:
            for line in f.readlines():
                clean_line = re.sub(r'!!python/\S+:', '', line)  # Remove Python tag
                lines_out.append(clean_line)
    except Exception as yaml_clean_error:
        print("Could not read YAML (clean_yaml):", yaml_filepath)
        print("Error:", yaml_clean_error)
        return ""
    return "".join(lines_out)

# GATHERING METRICS
print("Preparing to gather metrics.")
results_list = []  # Reset for safety

if df_classification is not None:
    print("Starting to iterate through classification data (df_classification).")
    length_df = len(df_classification)     # Number of programs in classification CSV
    print("Number of rows in df_classification:", length_df)
    i_counter = 0    # Initialize counter (int), start at 0.

    while i_counter < length_df:
        print("Processing row", i_counter,  "– Program:", df_classification.loc[i_counter, 'Program'])
        program_name = df_classification.loc[i_counter, 'Program']    # Program name (string)
        mutation_score = df_classification.loc[i_counter, 'Mutation Score']  # Mutation score (float)
        classification_label = df_classification.loc[i_counter, 'Classification']  # Classification label (string)
        manual_comment = manual_comments.get(program_name, "")

        yaml_path = filtered_mutation_dir + "/" + str(program_name) + "_report.yaml" # Build YAML path

        # Make a dict for this row
        tmp_dict = {
            "Program": program_name,
            "Mutation Score": mutation_score,
            "Classification": classification_label,
            "Test Time (s)": None,
            "Number of Tests": None,
            "Number of Mutants": None,
            "Estimated Asserts": None,
            "Manual Comment": manual_comment
        }

        yaml_file_exists = os.path.exists(yaml_path)
        if yaml_file_exists:
            print("YAML file found, attempting to read and process.")
            try:
                yaml_text = clean_yaml(yaml_path)  # Clean YAML as string
                yaml_dict = yaml.safe_load(yaml_text)  # Parse to dict
                test_time = yaml_dict.get("total_time")
                num_tests = yaml_dict.get("number_of_tests")
                mutant_list = yaml_dict.get("mutations", [])
                num_mutants = len(mutant_list)

                # Count asserts (mutants with exception_traceback)
                num_asserts = 0
                for mutant in mutant_list:
                    if mutant.get("exception_traceback"):
                        num_asserts += 1

                # Set values in dict
                tmp_dict["Test Time (s)"] = test_time
                tmp_dict["Number of Tests"] = num_tests
                tmp_dict["Number of Mutants"] = num_mutants
                tmp_dict["Estimated Asserts"] = num_asserts
                print("All values set in tmp_dict.")
            except Exception as yaml_parse_error:
                print("YAML PARSE ERROR:", yaml_parse_error)
        else:
            print("YAML file missing, skipping:", yaml_path)

        results_list.append(tmp_dict)
        i_counter += 1

else:
    print("df_classification is None; the classification file is not loaded. No metrics gathered.")

# SAVE OUTPUT TO CSV
print("Saving all data to CSV… (may take a moment)")
try:
    df_output = pd.DataFrame(results_list)
    df_output.to_csv(metrics_table_csv, index=False, sep=';')
    print("CSV written to:", metrics_table_csv)
    save_success = True
except Exception as save_error:
    print("Could not save CSV:", save_error)
    save_success = False