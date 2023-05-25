import random
import csv

def create_wic_csv(input_file, output_file):
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

    sentence_pairs = []
    for group in groups:
        if len(group) > 1:
            random.shuffle(group)
            for i in range(len(group) - 1):
                sentence1 = group[i]
                sentence2 = group[i + 1]
                sentence_pairs.append([sentence1, sentence2])

    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['sentence1', 'sentence2'])  # Write header
        writer.writerows(sentence_pairs)

    print(f"CSV file '{output_file}' has been created.")

# Usage example
input_filename = 'centroidi_final.txt'  # Replace with your input file name
output_filename = 'WiC_final.csv'  # Replace with your output file name

create_wic_csv(input_filename, output_filename)
