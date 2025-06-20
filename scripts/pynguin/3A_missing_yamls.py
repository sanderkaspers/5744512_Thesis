"""
This script creates missing MutPy YAMLs using a plain text template fallback.
It avoids loading python-specific tags. Use for MutPy output only!
"""

import os
import shutil
import re
import glob
import yaml
from datetime import datetime

PROJECT_ROOT = r"C:\Users\skaspers\OneDrive - Capgemini\Documents\Prompted Testsuite Analysis"
MUTATION_RESULTS_DIR = os.path.join(PROJECT_ROOT, 'results/pynguin/filtered_mutation_results')
LOGS_DIR = os.path.join(MUTATION_RESULTS_DIR, 'logs')
YAML_TEMPLATE_FILE = os.path.join(MUTATION_RESULTS_DIR, 'program_046_report.yaml')
TESTS_WITH_MISSING_YAML = [1, 6, 17, 26, 69]
HTML_REPORT_PREFIX = "program_{:03d}_html"
YAML_REPORT_NAME = "program_{:03d}_report.yaml"

print("=== Start patch_missing_yaml_reports.py ===")
print("Project root:", PROJECT_ROOT)
print("YAML template file:", YAML_TEMPLATE_FILE)
print("Will patch:", TESTS_WITH_MISSING_YAML)

# --- Laad YAML als tekst voor template ---
if not os.path.exists(YAML_TEMPLATE_FILE):
    print("ERROR: Example YAML template not found:", YAML_TEMPLATE_FILE)
    exit(1)

def simple_yaml_template_from_text(yaml_path):
    """Load all lines up to 'mutations:' as template prefix, rest is programmatically gegenereerd."""
    with open(yaml_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Vind waar 'mutations:' staat
    mutations_line = None
    for i, line in enumerate(lines):
        if line.strip().startswith('mutations:'):
            mutations_line = i
            break
    if mutations_line is None:
        raise Exception("No 'mutations:' found in template yaml!")
    # Gebruik alles tot aan 'mutations:'
    header_lines = lines[:mutations_line+1]
    header_text = ''.join(header_lines)
    return header_text

yaml_prefix = simple_yaml_template_from_text(YAML_TEMPLATE_FILE)

def extract_mutation_info_from_html(html_dir):
    mutant_files = [fn for fn in os.listdir(html_dir) if fn.endswith('.html') and fn != 'index.html']
    n_mutants = len(mutant_files)
    print(f"Found {n_mutants} mutant HTML files in:", html_dir)
    return n_mutants

def parse_log_file(log_file):
    results = []
    mutation_score = None
    if not os.path.exists(log_file):
        print("WARNING: No log file found for:", log_file)
        return results, mutation_score
    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            m = re.match(r"\s*-\s*\[#\s*(\d+)\]\s+(\w+)\s+.*:\s+\[[^\]]*\]\s+(\w+)(.*)", line)
            if m:
                idx, op, status, details = m.groups()
                result = {
                    "number": int(idx),
                    "operator": op,
                    "status": status,
                    "details": details.strip(),
                }
                results.append(result)
            if "Mutation score:" in line:
                m = re.search(r"Mutation score:\s*([0-9.]+)", line)
                if m:
                    mutation_score = float(m.group(1))
    print(f"Extracted {len(results)} mutant lines, mutation_score: {mutation_score}")
    return results, mutation_score

def write_yaml_from_template(test_idx, mutant_results, mutation_score):
    yaml_path = os.path.join(MUTATION_RESULTS_DIR, YAML_REPORT_NAME.format(test_idx))
    with open(yaml_path, "w", encoding="utf-8") as f:
        # Schrijf de header
        f.write(yaml_prefix)
        # Schrijf mutants
        for res in mutant_results:
            f.write("  - exception_traceback: null\n")
            f.write(f"    killer: {res.get('details', 'null')}\n")
            f.write(f"    module: datasets.pynguin.programs.program_{test_idx:03d}\n")
            f.write(f"    mutations:\n")
            f.write(f"    - operator: {res['operator']}\n")
            f.write(f"      lineno: 0\n")
            f.write(f"    number: {res['number']}\n")
            f.write(f"    status: {res['status']}\n")
            f.write(f"    tests_run: 1\n")
            f.write(f"    time: 0.0\n")
        # Rest van de yaml: simpel sjabloon, minimale info
        f.write(f"number_of_tests: 1\n")
        f.write(f"targets:\n- datasets.pynguin.programs.program_{test_idx:03d}\n")
        f.write(f"tests:\n- name: datasets.pynguin.tests.test_{test_idx:03d}\n  target: null\n  time: 0.0\n")
        f.write("time_stats:\n  create_mutant_module: 0.0\n  create_target_ast: 0.0\n  mutate_module: 0.0\n  run_tests_with_mutant: 0.0\n")
        f.write("total_time: 0.0\n")
        f.write("coverage:\n  all_nodes: 0\n  covered_nodes: 0\n")
        f.write(f"mutation_score: {mutation_score if mutation_score is not None else 0.0}\n")
    print("Written:", yaml_path)

for test_idx in TESTS_WITH_MISSING_YAML:
    print(f"\n--- Patching test index: {test_idx:03d} ---")
    html_dir = os.path.join(MUTATION_RESULTS_DIR, HTML_REPORT_PREFIX.format(test_idx))
    yaml_path = os.path.join(MUTATION_RESULTS_DIR, YAML_REPORT_NAME.format(test_idx))
    log_file = os.path.join(LOGS_DIR, f"program_{test_idx:03d}.log")
    if os.path.exists(yaml_path):
        print("YAML already exists, skipping:", yaml_path)
        continue
    if not os.path.isdir(html_dir):
        print("ERROR: HTML report directory missing for:", html_dir)
        continue

    print("Parsing HTML & log for:", test_idx)
    n_mutants = extract_mutation_info_from_html(html_dir)
    mutant_results, mutation_score = parse_log_file(log_file)
    if not mutant_results:
        print("WARNING: No mutants found in log; writing dummy mutants.")
        for n in range(n_mutants):
            mutant_results.append({'number': n+1, 'operator': 'AOR', 'status': 'survived', 'details': None})
    write_yaml_from_template(test_idx, mutant_results, mutation_score)

print("\nDone! Check your missing YAMLs in:", MUTATION_RESULTS_DIR)
