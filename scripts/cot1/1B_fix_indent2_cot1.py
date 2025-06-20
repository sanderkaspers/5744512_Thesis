from pathlib import Path

# Juiste pad naar de testbestanden
test_dir = Path(r"C:\Users\skaspers\OneDrive - Capgemini\Documents\Prompted Testsuite Analysis\datasets\GPT_4\Chain_of_thought1\tests")

def fix_with_indent_no_double(file_path):
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()
    result_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        result_lines.append(line)
        # Zoek een 'with'-regel
        if line.lstrip().startswith('with ') and line.rstrip().endswith(':'):
            # Zoek eerste niet-lege regel daarna
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                result_lines.append(lines[j])
                j += 1
            if j < len(lines):
                # Bepaal de juiste indent
                base_indent = len(line) - len(line.lstrip())
                correct_indent = ' ' * (base_indent + 4)
                stripped_line = lines[j].lstrip()
                # Check of die regel al correct is ingesprongen
                if not lines[j].startswith(correct_indent):
                    # Voeg de gecorrigeerde regel toe, maar sla de originele foutieve regel over
                    result_lines.append(correct_indent + stripped_line)
                else:
                    # Voeg hem gewoon toe zoals hij is
                    result_lines.append(lines[j])
                j += 1
            i = j
        else:
            i += 1
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(result_lines)
    print(f"{file_path.name}: netjes gefixt zonder dubbele regels.")

for file in test_dir.glob('test_*.py'):
    fix_with_indent_no_double(file)

print("Klaar: alle regels na 'with' netjes, geen dubbele regels.")
