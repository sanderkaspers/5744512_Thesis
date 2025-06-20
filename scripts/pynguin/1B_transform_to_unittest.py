"""
This script wraps pytest-style test functions in a unittest.TestCase class.
It scans all test_XXX.py files in a folder, and rewrites them in unittest format.
"""

import os

# PATHS
tests_folder = "datasets/pynguin/tests"
backup_folder = tests_folder + "_backup"
file_names = None
file_path = None
original_lines = None
new_lines = None
func_start_indices = []
func_blocks = []
import_lines = []
has_pytest_funcs = False
test_func_name = ""
i = 0
idx = 0
current_func = []

# Create backup of tests_folder
if not os.path.exists(backup_folder):
    try:
        os.makedirs(backup_folder)
        print("Backup folder created:", backup_folder)
    except Exception as folder_error:
        print("Error creating backup folder:", backup_folder)
        print(folder_error)

print("Wrapping pytest functions in unittest class in folder:", tests_folder)

# Get all test_*.py files in tests_folder
file_names = [f for f in os.listdir(tests_folder) if f.startswith("test_") and f.endswith(".py")]
print("Found", len(file_names), "test files to process.")

for file_name in file_names:
    file_path = os.path.join(tests_folder, file_name)
    print("\nProcessing file:", file_path)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            original_lines = f.readlines()
    except Exception as read_error:
        print("Failed to read file:", file_path, "-", str(read_error))
        continue

    import_lines = []
    func_blocks = []
    func_start_indices = []
    has_pytest_funcs = False

    # Collect import lines and find function blocks
    i = 0
    while i < len(original_lines):
        line = original_lines[i]
        if line.strip().startswith("def test_"):
            has_pytest_funcs = True
            func_start = i
            current_func = [line]
            i += 1
            # collect function body
            while i < len(original_lines):
                if original_lines[i].startswith("def ") or original_lines[i].startswith("class "):
                    break
                current_func.append(original_lines[i])
                i += 1
            func_blocks.append(current_func)
        elif line.strip().startswith("import") or line.strip().startswith("from"):
            import_lines.append(line)
            i += 1
        else:
            i += 1

    if not has_pytest_funcs:
        print("No pytest-style test functions found in:", file_name)
        # Make a backup anyway
        backup_path = os.path.join(backup_folder, file_name)
        try:
            with open(backup_path, "w", encoding="utf-8") as backup_f:
                backup_f.writelines(original_lines)
            print("Original file backed up as:", backup_path)
        except Exception as backup_error:
            print("Error backing up file:", backup_path, "-", backup_error)
        continue

    # Write backup
    backup_path = os.path.join(backup_folder, file_name)
    try:
        with open(backup_path, "w", encoding="utf-8") as backup_f:
            backup_f.writelines(original_lines)
        print("Original file backed up as:", backup_path)
    except Exception as backup_error:
        print("Error backing up file:", backup_path, "-", backup_error)

    # Prepare new file lines
    new_lines = []
    new_lines.append("import unittest\n")
    for imp in import_lines:
        new_lines.append(imp)
    new_lines.append("\nclass TestAll(unittest.TestCase):\n")
    for func in func_blocks:
        for j, l in enumerate(func):
            if j == 0:
                # Always rewrite to def test_xxx(self):
                # Robust: strip everything, get function name, always add (self):
                l_strip = l.strip()
                if l_strip.startswith("def "):
                    func_name = l_strip.split()[1].split('(')[0]
                    new_lines.append(f"    def {func_name}(self):\n")
                else:
                    new_lines.append("    " + l_strip + "(self):\n")
            else:
                new_lines.append("    " + l if l.strip() else "    \n")
        new_lines.append("\n")
    print("Total test functions wrapped:", len(func_blocks))

    # Write new file over original
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("Written unittest-wrapped test file:", file_path)
    except Exception as write_error:
        print("Error writing new unittest file:", file_path, "-", write_error)

print("\nAll files processed. Check", backup_folder, "for original files.")
print("You can now run unittest/MutPy on these test files.")
