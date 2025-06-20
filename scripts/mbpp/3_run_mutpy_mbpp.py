"""
This script runs mutation tests on a set of Python programs using MutPy.
It loads a JSON file with test names, loops through each test,
runs mutation testing, and saves reports and logs for each run.
"""

# IMPORTS
import os  # File and directory operations
import json  # JSON parsing
import subprocess
import sys

# PATHS
PROJECT_ROOT = r"C:\Users\skaspers\OneDrive - Capgemini\Documents\Prompted Testsuite Analysis"
input_json_path = "results/mbpp/filtered_tests_mbpp.json"
python_mutpy_path = ".venv38/Scripts/python.exe"
mutation_output_dir = 'results/mbpp/filtered_mutation_results'
logs_dir = os.path.join(mutation_output_dir, 'logs')
FILTERED_JSON_FILENAME = input_json_path
test_module_path = "datasets.mbpp.tests"
mbpp_programs_path = "datasets.mbpp.programs"
EXTRA_LOGS_ON = True

# GLOBAL VARIABLES
all_test_names_list = []
current_log_name = None
per_test_report_html_dir = None
yaml_report_file = None
test_name_index_value = None
program_module_name = None
module_test_name = None
file_for_json_read = None
current_json_content = None
TEST_JSON = None
json_load_error = None
result_from_subprocess = None
current_env_vars = None

# Create output directories if needed
if not os.path.exists(mutation_output_dir):
    print("Output directory does not exist, creating...")
    os.makedirs(mutation_output_dir)
if not os.path.exists(logs_dir):
    print("Logs directory does not exist, creating...")
    os.makedirs(logs_dir)

# Try to open JSON file with test names
if os.path.exists(FILTERED_JSON_FILENAME):
    print("JSON file found:", FILTERED_JSON_FILENAME)
    file_for_json_read = open(FILTERED_JSON_FILENAME, 'r')
else:
    print("JSON file not found:", FILTERED_JSON_FILENAME)
    file_for_json_read = None

if file_for_json_read is None:
    print("No JSON file found, stopping.")
    exit(1)

try:
    # Read the JSON content from file.
    current_json_content = file_for_json_read.read()
    TEST_JSON = json.loads(current_json_content)
    print("JSON loaded successfully, count:", len(TEST_JSON))
except Exception as json_load_error:
    print("ERROR reading JSON, exiting.", json_load_error)
    TEST_JSON = []
    file_for_json_read.close()
    exit(1)
file_for_json_read.close()

# Create list of test names from JSON
if isinstance(TEST_JSON, dict):
    all_test_names_list = list(TEST_JSON.keys())
elif isinstance(TEST_JSON, list):
    all_test_names_list = TEST_JSON
else:
    print("Unknown JSON format, stopping.")
    exit(1)

print("Created list of test names, count:", len(all_test_names_list))

# Find a working python interpreter path for mutpy
found_python_path = None
for q in ["python", "python3"]:
    if os.system(q + " --version > nul 2>&1") == 0:
        found_python_path = q
        print("Found python path:", q)
        break

# PATCH: if the configured venv interpreter does not exist, fall back to
# a working system interpreter that we just discovered (or 'python').
if not os.path.exists(python_mutpy_path):
    print("Configured interpreter", python_mutpy_path, "not found, using fallback.")
    python_mutpy_path = found_python_path or "python"
    print("Using interpreter for MutPy:", python_mutpy_path)

# GLOBAL FIX: disable hash-randomisation in all child processes to prevent
# _Py_HashRandomization_Init failures on Windows under heavy spawning.
# (Overgenomen uit origineel, behoud deze regel voor consistentie)
os.environ["PYTHONHASHSEED"] = "0"

# For each test name, prepare mutation testing, create necessary report directories,
# and run MutPy with the corresponding program and test modules.
for tn in all_test_names_list:
    try:
        try:
            # Try to extract index from test name
            test_name_index_value = int(tn.split('_')[1])
            print(f"\n=== Start test: {tn} (index {test_name_index_value}) ===")
        except (IndexError, ValueError):
            print(f"Error extracting index from test name: {tn}, skipping.")
            continue
        # Build program and test module names
        program_module_name = mbpp_programs_path + ".program_" + str(test_name_index_value).zfill(3)
        module_test_name = test_module_path + ".test_" + str(test_name_index_value).zfill(3)
        per_test_report_html_dir = os.path.join(
            mutation_output_dir, "program_" + str(test_name_index_value).zfill(3) + "_html"
        )
        yaml_report_file = os.path.join(
            mutation_output_dir, "program_" + str(test_name_index_value).zfill(3) + "_report.yaml"
        )
        # Create report directory if needed
        if not os.path.exists(per_test_report_html_dir):
            print("Create HTML directory for report:", per_test_report_html_dir)
            os.makedirs(per_test_report_html_dir)
        # Log file for current mutation run
        current_log_name = os.path.join(
            logs_dir, "program_" + str(test_name_index_value).zfill(3) + ".log"
        )

        # Command to run mutpy
        cmd = [
            python_mutpy_path, "-m", "mutpy.commandline",
            "--target", program_module_name,
            "--unit-test", module_test_name,
            "--runner", "unittest",
            "--report-html", per_test_report_html_dir,
            "--report", yaml_report_file,
            "--debug"
        ]
        print("Command:", " ".join(cmd))

        open_log = open(current_log_name, 'w')

        # Copy environment variables and set PYTHONPATH to PROJECT_ROOT
        current_env_vars = os.environ.copy()
        current_env_vars["PYTHONPATH"] = PROJECT_ROOT
        current_env_vars["PYTHONHASHSEED"] = "0"

        result_from_subprocess = subprocess.run(
            cmd,
            stdout=open_log,
            stderr=subprocess.STDOUT,
            env=current_env_vars,
            cwd=PROJECT_ROOT
        )
        open_log.flush()
        open_log.close()

        # Check that log file was created
        if not os.path.exists(current_log_name):
            print("Error: Log file NOT created:", current_log_name)
            continue
        # Check return code is int
        if not isinstance(result_from_subprocess.returncode, int):
            print("ERROR: returncode is not int.")

        with open(current_log_name, "r") as logfile:
            log_content = logfile.read()
            if "Mutation score" in log_content:
                print(f"Mutation succeeded for program_{test_name_index_value:03}.")
            else:
                print(f"Mutation failed for program_{test_name_index_value:03} (see log file).")
                if EXTRA_LOGS_ON:
                    print("---- log excerpt ----")
                    print(log_content[:500] if log_content else "(log empty)")
                    print("---------------------")

        if os.path.exists(yaml_report_file):
            print("YAML report created:", yaml_report_file)
        else:
            print("YAML report NOT found for", module_test_name)
        if os.path.isdir(per_test_report_html_dir) and os.listdir(per_test_report_html_dir):
            print("HTML report directory contains", len(os.listdir(per_test_report_html_dir)), "file(s).")
        else:
            print("HTML report directory is empty!")

    except Exception as error_in_loop:
        print(f"Error during test {tn}:", error_in_loop)

print("All mutation checks done! See:", mutation_output_dir)
print("SCRIPT PYTHON VERSION:", sys.executable, sys.version)
print("SCRIPT CWD:", os.getcwd())
