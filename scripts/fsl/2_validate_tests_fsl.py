"""
This script checks, filters, and logs Python test files.
It runs the tests, measures coverage, and saves the results in files.
"""

# IMPORTS
import coverage
import os  # File and directory operations
import json  # JSON parsing
import shutil
import sys
import unittest

# PATHS
total_tests_so_far = 100
test_data_path = "datasets/GPT_4/Few_shot/tests"
filtered_path = "datasets/GPT_4/Few_shot/filtered_tests"
fsl_result_dir = "results/fsl"
LOG_FILE_FINAL_v2 = "results/fsl/validation_log.txt"
JSON_NAME_X = "results/fsl/filtered_tests_fsl.json"

# GLOBAL VARIABLES
idx_now = 1
now_test_name = ""
now_test_path = ""
loader_unittesty = None
suite_tests = None
result_test_unit = None
errors_in_test_x = 0
excluded_list = []
manual_checklist = []
oklist = []
f_out = None
f_json = None
THRESHOLD_MAX_ERRORS = 2
coverage_per_test = {}

# CREATE OUTPUT FOLDERS
try:
    if not os.path.exists(filtered_path):
        print("Output folder (filtered_tests) does not exist, creating...")
        os.makedirs(filtered_path)
        print("Output folder (filtered_tests) created.")
    else:
        print("Output folder (filtered_tests) already exists.")
    if not os.path.exists(fsl_result_dir):
        print("Result folder (fsl) does not exist, creating...")
        os.makedirs(fsl_result_dir)
        print("Result folder (fsl) created.")
    else:
        print("Result folder (fsl) already exists.")
except Exception as folder_create_error:
    print("Failed to create output folder:", folder_create_error)

# VALIDATION LOOP
idx_now = 1

root_dir = os.path.abspath(".")
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

while idx_now <= total_tests_so_far:
    print("Validation loop started for file", idx_now)
    now_test_name = "test_" + str(idx_now).zfill(3) + ".py"
    now_test_path = test_data_path + "/" + now_test_name
    prog_name = "program_" + str(idx_now).zfill(3) + ".py"
    prog_path = "datasets/GPT_4/Few_shot/programs/" + prog_name
    loader_unittesty = unittest.TestLoader()

    try:
        # Start coverage for the program code
        cov = coverage.Coverage(
            source=["datasets/GPT_4/Few_shot/programs"]
        )
        cov.start()

        # Discover and run the test suite
        suite_tests = loader_unittesty.discover(
            start_dir=test_data_path, pattern=now_test_name
        )
        print(f"\n--- Running tests in {now_test_name} ---")
        runner = unittest.TextTestRunner(verbosity=2)
        result_test_unit = runner.run(suite_tests)
        print(f"--- Done with {now_test_name} ---\n")

        cov.stop()
        cov.save()

        errors_in_test_x = (
            len(result_test_unit.failures) + len(result_test_unit.errors)
        )

        # Calculate coverage for the program file
        try:
            prog_path_abs = os.path.abspath(prog_path)
            analysis = cov.analysis(prog_path_abs)
            total_statements = len(analysis[1])  # executable lines
            missing_lines = len(analysis[2])     # missing lines
            if total_statements > 0:
                percent_covered = 100.0 * (total_statements - missing_lines) / total_statements
                percent_covered = round(percent_covered, 2)
            else:
                percent_covered = 100.0  # Full coverage for empty file
        except Exception as cov_analysis_error:
            print("Error analyzing coverage for", prog_name, ":", cov_analysis_error)
            percent_covered = "ERROR"
        print("Coverage percentage for", prog_name, ":", percent_covered)
        coverage_per_test[prog_name] = percent_covered

    except Exception as discover_error:
        print("ERROR loading test suite:", discover_error)
        print("Skipping file due to suite error")
        excluded_list.append(
            ("test_" + str(idx_now).zfill(3), 999, 0, [], [])
        )
        idx_now = idx_now + 1
        continue

    # Collect failed test method names and error messages
    failed_test_names = []
    failed_msgs = []
    for fail in result_test_unit.failures:
        failed_test_names.append(fail[0]._testMethodName)
        failed_msgs.append(fail[1])
    for fail in result_test_unit.errors:
        failed_test_names.append(fail[0]._testMethodName)
        failed_msgs.append(fail[1])

    if errors_in_test_x == 0:
        try:
            if not os.path.exists(filtered_path + "/" + now_test_name):
                shutil.copy(now_test_path, filtered_path + "/" + now_test_name)
                print("Copied to filtered:", now_test_name)
            else:
                print("File already copied this run:", now_test_name)
        except Exception as copy_error:
            print("Copying FAILED:", now_test_name, "-", str(copy_error))
        oklist.append("tst_" + str(idx_now).zfill(3))
    else:
        manual_checklist.append(
            (
                "test_" + str(idx_now).zfill(3),
                errors_in_test_x,
                result_test_unit.testsRun,
                failed_test_names,
                failed_msgs,
            )
        )
        print(
            f"Manual check: {now_test_name} with {errors_in_test_x} errors out of {result_test_unit.testsRun}"
        )
        if len(failed_test_names) > 0:
            print("  Failed tests and reasons:")
            for i in range(len(failed_test_names)):
                print("    FAILED:", failed_test_names[i])
                if i < len(failed_msgs):
                    print(
                        "        "
                        + failed_msgs[i].replace("\n", "\n        ")
                    )
    idx_now = idx_now + 1

print("Validation loop complete")

# re-run each test inside coverage
coverage_per_test = {}

idx_now = 1
while idx_now <= total_tests_so_far:
    now_test_name = "test_" + str(idx_now).zfill(3) + ".py"
    now_test_path = test_data_path + "/" + now_test_name

    cov = coverage.Coverage(source=["datasets/GPT_4/Few_shot/programs"])
    try:
        cov.start()
        # run the discovered test suite so the program code is executed
        suite_tests = unittest.TestLoader().discover(
            start_dir=test_data_path, pattern=now_test_name
        )
        unittest.TextTestRunner(verbosity=0).run(suite_tests)
        cov.stop()
        cov.save()
        # Now measure coverage of the program file!
        prog_name = "program_" + str(idx_now).zfill(3) + ".py"
        prog_path = "datasets/GPT_4/Few_shot/programs/" + prog_name
        prog_path_abs = os.path.abspath(prog_path)
        analysis = cov.analysis(prog_path_abs)
        total_statements = len(analysis[1])
        missing_lines = len(analysis[2])
        if total_statements > 0:
            percent_covered = round(100.0 * (total_statements - missing_lines) / total_statements, 2)
        else:
            percent_covered = 100.0
        print("Coverage percentage for", prog_name, ":", percent_covered)
        coverage_per_test[prog_name] = percent_covered
    except Exception as coverage_error:
        print(
            "Coverage measurement failed for",
            prog_name,
            "with error:",
            coverage_error,
        )
        coverage_per_test[prog_name] = "ERROR"

    idx_now += 1

print("All coverage measurements per test suite are done!")
cov_outpath = "results/fsl/coverage_per_test_fsl.json"
try:
    with open(cov_outpath, "w", encoding="utf-8") as cov_outf:
        json.dump(coverage_per_test, cov_outf, indent=2)
    print("Coverage results saved in:", cov_outpath)
except Exception as coverage_write_error:
    print("Error writing coverage results:", coverage_write_error)

# SUMMARY
print("Number ok:", len(oklist))
print("Number manual check:", len(manual_checklist))
print("Number excluded:", len(excluded_list))

# LOGGING
try:
    f_out = open(LOG_FILE_FINAL_v2, "w", encoding="utf-8")
    print("Log file opened:", LOG_FILE_FINAL_v2)
    f_out.write("EXCLUDED tests (3+ errors):\n")
    for exc_test in excluded_list:
        n_exc = exc_test[0]
        err_exc = exc_test[1]
        total_exc = exc_test[2]
        print("Log: exclude:", n_exc, "with", err_exc, "errors out of", total_exc)
        f_out.write(n_exc + ": " + str(err_exc) + "/" + str(total_exc) + " failures\n")
    f_out.write("\nMANUAL CHECK recommended (1-2 errors):\n")
    for man_test in manual_checklist:
        n_man = man_test[0]
        err_man = man_test[1]
        total_man = man_test[2]
        print("Log: manual check:", n_man, "with", err_man, "errors out of", total_man)
        f_out.write(n_man + ": " + str(err_man) + "/" + str(total_man) + " failures\n")
    f_out.close()
    print("Log file at:", LOG_FILE_FINAL_v2)
except Exception as log_write_error:
    print("Error writing log:", log_write_error)

# JSON OUTPUT
print("Step 5: Writing JSON file...")
try:
    f_json = open(JSON_NAME_X, "w", encoding="utf-8")
    json.dump(oklist, f_json, indent=2)
    f_json.close()
    print("JSON ok files written:", JSON_NAME_X)
except Exception as json_write_error:
    print("Error writing JSON:", json_write_error)

print("- JSON file:", JSON_NAME_X)
print("- Log file:", LOG_FILE_FINAL_v2)

manual_check_file = "results/fsl/manual_checklist.txt"
try:
    f_manual = open(manual_check_file, "w", encoding="utf-8")
    for man_test in manual_checklist:
        prog_num = man_test[0].replace("test", "program")  # e.g. program_002
        program_file_name = prog_num + ".py"
        program_path = os.path.join("datasets/GPT_4/Few_shot/programs", program_file_name)
        test_file_name = man_test[0] + ".py"
        test_file_path = os.path.join("datasets/GPT_4/Few_shot/tests", test_file_name)

        # Write program file header
        f_manual.write(prog_num + " (source):\n")
        # Try to read and write the program file
        try:
            with open(program_path, "r", encoding="utf-8") as prog_file:
                for line in prog_file:
                    f_manual.write("    " + line)
        except Exception as file_read_error:
            f_manual.write("    (Could not read program file)\n")

        # Now write only the code of the *failed* test functions
        failed_names = man_test[3]
        f_manual.write(prog_num + " (failed test code):\n")
        if failed_names:
            try:
                with open(test_file_path, "r", encoding="utf-8") as test_file:
                    test_lines = test_file.readlines()
                for test_name in failed_names:
                    in_func = False
                    for i, line in enumerate(test_lines):
                        if line.strip().startswith(f"def {test_name}("):
                            in_func = True
                            f_manual.write("    " + line)
                            # Now write the function body (all indented lines after the def)
                            j = i + 1
                            while j < len(test_lines):
                                body_line = test_lines[j]
                                # Stop at next top-level def or class (no indentation)
                                if body_line.startswith("def ") or body_line.startswith("class ") or (body_line.strip() and not body_line.startswith((" ", "\t"))):
                                    break
                                f_manual.write("    " + body_line)
                                j += 1
                            f_manual.write("\n")
                            break
                    else:
                        f_manual.write(f"    (Test code for {test_name} not found)\n")
            except Exception as test_read_error:
                f_manual.write("    (Could not read test file)\n")
        else:
            f_manual.write("    (no failed tests)\n")

        # Now write failed assert errors
        failed_msgs = man_test[4] if len(man_test) > 4 else []
        f_manual.write(f"\n{prog_num} (assert errors):\n")
        if failed_names and failed_msgs:
            for i in range(len(failed_names)):
                f_manual.write(f"    FAILED: {failed_names[i]}\n")
                if i < len(failed_msgs):
                    f_manual.write("        " + failed_msgs[i].replace("\n", "\n        ") + "\n")
        else:
            f_manual.write("    (no assert errors)\n")
        f_manual.write("\n")
    f_manual.close()
    print("Manual checklist written to:", manual_check_file)
except Exception as manual_write_error:
    print("Error writing manual checklist:", manual_write_error)