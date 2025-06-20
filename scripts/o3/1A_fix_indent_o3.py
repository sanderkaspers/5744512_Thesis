import os
from pathlib import Path
import re

# Je doelmap:
test_dir = Path(r"C:\Users\skaspers\OneDrive - Capgemini\Documents\Prompted Testsuite Analysis\datasets\o3\tests")

def fix_file(file_path):
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()

    fixed_lines = []
    import_fixed = False

    # 1. Fix de importregel bovenaan
    for i, line in enumerate(lines):
        if line.startswith('from datasets.o3.programs'):
            # Pak progjeXXX nummer uit de foute import
            match = re.search(r'program_(\d+)', line)
            progje_nummer = match.group(1) if match else '001'
            new_line = f'from datasets.o3.programs.program_{progje_nummer} import *\n'
            fixed_lines.append(new_line)
            import_fixed = True
        else:
            fixed_lines.append(line)

    # 2. Fix de inspringing (zoals in vorige script)
    inside_function_or_class = False
    indent_level = 0
    lines_final = []
    for line in fixed_lines:
        stripped = line.lstrip()
        if stripped.startswith('def ') or stripped.startswith('class '):
            inside_function_or_class = True
            indent_level = len(line) - len(stripped) + 4
            lines_final.append(line.rstrip() + '\n')
            continue
        if stripped == '':
            lines_final.append('\n')
            continue
        if inside_function_or_class:
            if (stripped.startswith('def ') or stripped.startswith('class ')) and (len(line) - len(stripped) == 0):
                inside_function_or_class = True
                indent_level = 4
                lines_final.append(line.rstrip() + '\n')
            else:
                lines_final.append(' ' * indent_level + stripped)
        else:
            lines_final.append(line)

    # Overschrijf het bestand
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines_final)

    if import_fixed:
        print(f"{file_path.name}: Importregel aangepast en inspringing gefixt.")
    else:
        print(f"{file_path.name}: Geen importregel gevonden, alleen inspringing gefixt.")

# Loop over alle tstje_*.py bestanden
for file in test_dir.glob('test_*.py'):
    fix_file(file)

print("Klaar! Alle bestanden zijn aangepast.")
