from pathlib import Path

# Juiste pad naar de testbestanden
test_dir = Path(r"C:\Users\skaspers\OneDrive - Capgemini\Documents\Prompted Testsuite Analysis\datasets\GPT_4\Few_shot\tests")

def fix_block_indent_no_double(file_path):
    block_keywords = ['with ', 'try:', 'except', 'else:', 'finally:']
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()
    result_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        result_lines.append(line)
        stripped = line.lstrip()
        is_block = False
        for keyword in block_keywords:
            if (stripped.startswith(keyword) or stripped.startswith(keyword.replace(':',''))) and line.rstrip().endswith(':'):
                is_block = True
                break
        if is_block:
            # Zoek eerste niet-lege regel daarna
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                result_lines.append(lines[j])
                j += 1
            if j < len(lines):
                base_indent = len(line) - len(line.lstrip())
                correct_indent = ' ' * (base_indent + 4)
                stripped_line = lines[j].lstrip()
                if not lines[j].startswith(correct_indent):
                    result_lines.append(correct_indent + stripped_line)
                else:
                    result_lines.append(lines[j])
                j += 1

                # -- NIEUW -- Controleer of 2 regels na blok een assert staat (vooral voor try:)
                # Sla lege regels na blok over
                temp_j = j
                empty_count = 0
                while temp_j < len(lines) and lines[temp_j].strip() == '' and empty_count < 2:
                    result_lines.append(lines[temp_j])
                    temp_j += 1
                    empty_count += 1

                # Check assert 2 regels na het blok
                # Voorbeeld: try:   <- i
                #   ...             <- j
                #                   <- temp_j = j+1 (leeg)
                #   assert ...      <- temp_j = j+2 (assert)

                if temp_j < len(lines):
                    stripped_temp = lines[temp_j].lstrip()
                    if stripped_temp.startswith("assert"):
                        # Pas inspringing aan als nodig
                        if not lines[temp_j].startswith(correct_indent):
                            result_lines.append(correct_indent + stripped_temp)
                        else:
                            result_lines.append(lines[temp_j])
                        temp_j += 1
                    j = temp_j
            i = j
        else:
            i += 1
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(result_lines)
    print(f"{file_path.name}: netjes gefixt inclusief asserts na try.")

for file in test_dir.glob('test_*.py'):
    fix_block_indent_no_double(file)

print("Klaar: alle regels na blok-statements netjes, inclusief asserts na try.")

