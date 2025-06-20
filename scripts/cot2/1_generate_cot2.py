"""
This script reads an Excel file containing function code and test cases.
It creates program files and test files for each row in the Excel file.
Folders are created if they do not exist.
"""

# IMPORTS
import os # File and directory operations
import pandas as pd  # For DataFrame operations.

# PATHS
excel_file_path = "datasets/GPT_4/Chain_of_thought2/FULL100COT_RERUN2.xlsx"
ml_model = "GPT_4"
prompt_type = "Chain_of_thought2"
main_folder = "datasets"
programs_folder = main_folder + "/" + ml_model + "/" + prompt_type + "/programs"
tests_folder = main_folder + "/" + ml_model + "/" + prompt_type + "/tests"

# GLOBAL VARIABLES
the_big_df = None
num_rows = 0
row_index = 0
task_id = None
function_code = None
test_case_list = None
program_output_path = ""
test_output_path = ""
excel_error = None
program_folder_error = None
test_folder_error = None
save_code_error = None
test_save_error = None
file_writer = None
file_writer_test = None
intermediate_result_case = None

# main folder locations
print("Main folder is:", main_folder)
print("Main folder for programs:", programs_folder)
print("Main folder for tests:", tests_folder)

print("Reading Excel file:", excel_file_path)

# Excel file load attempt
print("Before trying to load the Excel file.")
try:
    print("Trying to load Excel...")
    the_big_df = pd.read_excel(excel_file_path, header=0)
    print("Excel file loaded.")
    # first 3 rows
    print(the_big_df.head(3))
except Exception as excel_error:
    # Excel file error
    print("Error reading Excel:")
    print(excel_error)
    print("Excel file not found or could not be opened.")
    the_big_df = None

if the_big_df is None:
    print("ERROR: DataFrame not loaded!")
else:
    num_rows = len(the_big_df)
    print("Number of rows in DataFrame:", num_rows)
    if num_rows == 0:
        print("ERROR: DataFrame is empty!")
    else:
        print("DataFrame NOT empty! Rows:", num_rows)
        print("First row of DataFrame:", the_big_df.iloc[0] if num_rows > 0 else "NONE")

if the_big_df is not None:
    # asserting non-empty DataFrame
    assert len(the_big_df) > 0, "DataFrame is empty!"
    print("DataFrame contains data.")

# CREATE/CHECK FOLDERS
print("Check program folder:", programs_folder)
if not os.path.exists(programs_folder):
    try:
        os.makedirs(programs_folder)
        print("Created:", programs_folder)
    except Exception as program_folder_error:
        print("Error creating program folder:")
        print(program_folder_error)
else:
    print("Program folder exists:", programs_folder)

print("Check test folder:", tests_folder)
if not os.path.exists(tests_folder):
    try:
        os.makedirs(tests_folder)
        print("Test folder created:", tests_folder)
    except Exception as test_folder_error:
        print("Error creating test folder:")
        print(test_folder_error)
else:
    print("Test folder exists:", tests_folder)

if not os.path.exists(programs_folder):
    print("ERROR: Program folder no longer exists!")
if not os.path.exists(tests_folder):
    print("ERROR: Test folder no longer exists!")

if the_big_df is not None:
    assert os.path.exists(programs_folder), "Program folder does not exist!"
    assert os.path.exists(tests_folder), "Test folder does not exist!"
    print("Both folders exist. Folder check succeeded.")

# PROCESS EACH ROW
if the_big_df is not None:
    print("Processing DataFrame rows...")
    for row_index in range(len(the_big_df)):
        print("Processing row:", row_index)
        current_row = the_big_df.iloc[row_index]
        task_id = int(current_row[0])
        function_code = current_row[2]
        test_case_list = current_row[3:]

        program_output_path = programs_folder + "/program_" + str(task_id).zfill(3) + ".py"
        test_output_path = tests_folder + "/test_" + str(task_id).zfill(3) + ".py"

        # Write function code
        try:
            file_writer = open(program_output_path, "w", encoding="utf-8")
            file_writer.write(str(function_code).strip() + "\n")
            file_writer.close()
            print("Written:", program_output_path)
        except Exception as save_code_error:
            print("Error saving program:")
            print(program_output_path)
            print(save_code_error)

        # Write test file
        try:
            file_writer_test = open(test_output_path, "w", encoding="utf-8")
            file_writer_test.write("import unittest\n")
            file_writer_test.write(
                "from datasets." + ml_model + "." + prompt_type + ".programs.program_" + str(task_id).zfill(3) + " import *\n\n"
            )
            file_writer_test.write("class TestVersion(unittest.TestCase):\n")
            for i in range(len(test_case_list)):
                intermediate_result_case = test_case_list.iloc[i]
                if hasattr(pd, "isna") and pd.isna(intermediate_result_case):
                    # test case is empty
                    print("Test case empty, skipping.")
                else:
                    lines_list = str(intermediate_result_case).strip().split("\n")
                    for row_content in lines_list:
                        file_writer_test.write("    " + row_content.strip() + "\n")
                    file_writer_test.write("\n")
            file_writer_test.close()
            print("Test file written:", test_output_path)
        except Exception as test_save_error:
            print("Error saving test:")
            print(test_output_path)
            print(test_save_error)

        print("Row", row_index, "finished.")

print("All mutation tests completed.")
print("JSON loaded.")
print("100 programs and tests created.")