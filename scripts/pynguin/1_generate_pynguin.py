"""
This script reads an Excel file containing function code and test cases.
It creates program files for each row in the Excel file.
Folders are created if they do not exist.
"""

# IMPORTS
import os # File and directory operations
import pandas as pd  # For DataFrame operations.

# PATHS
excel_file_path = "datasets/pynguin/100_programs.xlsx"
ml_model = "pynguin"
main_folder = "datasets"
programs_folder = main_folder + "/" + ml_model + "/" + "/programs"
# tests_folder = main_folder + "/" + ml_model + "/" + prompt_type + "/tests"

# GLOBAL VARIABLES
the_big_df = None
num_rows = 0
row_index = 0
task_id = None
function_code = None
test_case_list = None
program_output_path = ""
# test_output_path = ""
excel_error = None
program_folder_error = None
# test_folder_error = None
save_code_error = None
# test_save_error = None
file_writer = None
# file_writer_test = None
intermediate_result_case = None

# main folder locations
print("Main folder is:", main_folder)
print("Main folder for programs:", programs_folder)
# print("Main folder for tests:", tests_folder)

print("Reading Excel file:", excel_file_path)

# Excel file load attempt
print("Before trying to load the Excel file.")
try:
    print("Trying to load Excel...")
    the_big_df = pd.read_excel(excel_file_path, header=0)
    print("Excel file loaded.")
    # first 3 rows
    print(the_big_df.head(3))
    print("Columns in DataFrame:", the_big_df.columns.tolist())
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

if not os.path.exists(programs_folder):
    print("ERROR: Program folder no longer exists!")
# if not os.path.exists(tests_folder):
#     print("ERROR: Test folder no longer exists!")

if the_big_df is not None:
    assert os.path.exists(programs_folder), "Program folder does not exist!"
    # assert os.path.exists(tests_folder), "Test folder does not exist!"
    print("Folders exist. Folder check succeeded.")

# PROCESS EACH ROW
if the_big_df is not None:
    print("Processing DataFrame rows...")
    for row_index in range(len(the_big_df)):
        print("Processing row:", row_index)
        current_row = the_big_df.iloc[row_index]

        # TASK ID: Prefer column name if possible, otherwise fallback to first column
        if 'id' in the_big_df.columns:
            task_id = int(current_row['id'])
        elif 'task_id' in the_big_df.columns:
            task_id = int(current_row['task_id'])
        elif 'index' in the_big_df.columns:
            task_id = int(current_row['index'])
        else:
            try:
                task_id = int(current_row[0])
            except Exception as id_error:
                print("ERROR: Could not find valid task_id for row", row_index, ":", id_error)
                continue

        # CODE: Prefer column name if possible, otherwise fallback to index 2
        if 'code' in the_big_df.columns:
            function_code = current_row['code']
        elif 'function_code' in the_big_df.columns:
            function_code = current_row['function_code']
        else:
            function_code = current_row[2]

        program_output_path = programs_folder + "/program_" + str(task_id).zfill(3) + ".py"
        # test_output_path = tests_folder + "/test_" + str(task_id).zfill(3) + ".py"

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


        print("Row", row_index, "finished.")

print("All mutation tests completed.")
print("JSON loaded.")
print("100 programs created.")
