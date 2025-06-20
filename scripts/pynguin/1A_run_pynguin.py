"""
This script runs Pynguin to generate tests for all program files in the programs folder.
It collects all program_xxx.py files, runs Pynguin on each, and saves logs and test files in the tests folder.
Folders are created if they do not exist.
"""

# IMPORTS
import pathlib  # For file paths and folders
import subprocess  # For running Pynguin as a subprocess
import os  # For environment variables and directory operations
import sys  # For printing errors
import shutil  # For copying files

# PATHS AND CONFIGURATION
program_folder = pathlib.Path("datasets/pynguin/programs")
tests_folder = pathlib.Path("datasets/pynguin/tests")
pynguin_bin = "pynguin"  # Path to pynguin executable
# sys.path.insert(0, os.path.abspath("datasets/pynguin/programs"))  # Not needed if using absolute imports

# ENVIRONMENT VARIABLES
os.environ["PYNGUIN_DANGER_AWARE"] = "YES"
os.environ["PYNGUIN_DISABLE_RICH"] = "1"

# Ensure tests folder exists
if not tests_folder.exists():
    try:
        tests_folder.mkdir(parents=True, exist_ok=True)
        print("Created tests folder:", tests_folder)
    except Exception as folder_error:
        print("Error creating tests folder:")
        print(folder_error)
else:
    print("Tests folder exists:", tests_folder)

print("Program folder is:", program_folder)
print("Tests folder is:", tests_folder)
print("Collecting program files in:", program_folder)

# Gather all program_*.py files
py_files = sorted(program_folder.glob("program_*.py"))
print("Number of program files found:", len(py_files))

if len(py_files) == 0:
    print("No program files found. Exiting.")
    sys.exit(0)
else:
    print("Program files to process:", [p.name for p in py_files])

# Process each program file
for idx, py_file in enumerate(py_files, 1):
    program_name = py_file.stem  # e.g., 'program_008'
    try:
        code_id = int(program_name.split('_')[1])
    except Exception as code_id_error:
        print("Error parsing code id for file:", py_file)
        print(code_id_error)
        continue

    print("({:03d}/{:03d}) Running Pynguin on:".format(idx, len(py_files)), program_name)

    # Clean up any previous test or failing files for this code id
    for suffix in ["", "_failing"]:
        old_test = tests_folder / f"test_program_{str(code_id).zfill(3)}{suffix}.py"
        if old_test.exists():
            try:
                old_test.unlink()
                print("Removed leftover file:", old_test)
            except Exception as cleanup_error:
                print("Error removing leftover test:", old_test)
                print(cleanup_error)

    cmd = [
        pynguin_bin,
        "--project-path", str(program_folder.resolve()),
        "--module-name", program_name,
        "--output-path", str(tests_folder.resolve()),
        "--maximum-iterations", "10000",
        "--seed", "3",
    ]
    print("Running command:", " ".join(cmd))
    try:
        result = subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            env=os.environ,
        )
        print("Pynguin run completed for:", program_name)
    except Exception as pynguin_error:
        print("Error running Pynguin on:", program_name)
        print(pynguin_error)
        continue

    # Write log (if non-empty)
    log_file = tests_folder / ("pynguin_" + program_name + ".log")
    try:
        if result.stdout.strip():
            log_file.write_text(result.stdout, encoding="utf-8")
            print("Log written to:", log_file)
        else:
            if log_file.exists():
                log_file.unlink()
            print("Log was empty for:", program_name)
    except Exception as log_error:
        print("Error writing log for:", program_name)
        print(log_error)

    # Handle generated test file(s)
    generated = tests_folder / ("test_" + program_name + ".py")
    dest = tests_folder / ("test_" + str(code_id).zfill(3) + ".py")
    failing = tests_folder / ("test_" + program_name + "_failing.py")

    # Move and rename the test file (if it exists)
    if generated.exists():
        if dest.exists():
            try:
                dest.unlink()
                print("Existing dest file removed:", dest)
            except Exception as unlink_error:
                print("Error removing existing file:", dest)
                print(unlink_error)
        try:
            generated.rename(dest)
            print("Test file saved as:", dest)
        except Exception as rename_error:
            print("Error moving test file to destination:")
            print(rename_error)
    else:
        print("No test file found for", program_name, file=sys.stderr)

    # Remove the _failing file if it exists
    if failing.exists():
        try:
            failing.unlink()
            print("Removed failing test file:", failing)
        except Exception as fail_remove_error:
            print("Error removing failing test file:", failing)
            print(fail_remove_error)

    # ---- Ensure tested program file is in tests folder (import will always work!) ----
    try:
        program_copy = tests_folder / py_file.name
        shutil.copy2(py_file, program_copy)
        print("Copied program file to test folder for import:", program_copy)
    except Exception as copy_error:
        print("Error copying program file for test import:")
        print(copy_error)

    # ---- Fix import in test file to use absolute import ----
    # e.g., from datasets.pynguin.programs import program_008 as module_0
    if dest.exists():
        try:
            with open(dest, "r", encoding="utf-8") as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if line.strip().startswith("import program_"):
                    prog_name = line.strip().split()[1]
                    lines[i] = f"from datasets.pynguin.programs import {prog_name} as module_0\n"
            with open(dest, "w", encoding="utf-8") as f:
                f.writelines(lines)
            print("Fixed import statement in:", dest)
        except Exception as fix_error:
            print("Error fixing import for:", dest)
            print(fix_error)

print("All Pynguin runs completed.")
print("You can now run the tests directly from the tests folder, imports will work.")
