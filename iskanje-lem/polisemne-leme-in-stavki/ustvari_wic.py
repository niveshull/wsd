import random

def create_wic_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()

    groups = []
    group = []
    for line in lines:
        line = line.strip()
        if line.startswith('Beseda:'):
            pass
        elif ":" in line:
            cent, poved = line.split(":", 1)
            group.append(poved.strip())

        if not line or line == lines[-1]:
            if group:
                groups.append(group)
            group = []

    with open(output_file, 'w', encoding='utf-8-sig') as f:
        for group in groups:
            if len(group) > 1:
                random.shuffle(group)
                for i in range(len(group) - 1):
                    sentence1 = group[i]
                    sentence2 = group[i + 1]
                    f.write(f"{sentence1}\t{sentence2}\n")

    print(f"WiC file '{output_file}' has been created.")

# Usage example
input_filename = 'a_test.txt'  # Replace with your input file name
output_filename = 'b_test.wic'  # Replace with your output file name

create_wic_file(input_filename, output_filename)
