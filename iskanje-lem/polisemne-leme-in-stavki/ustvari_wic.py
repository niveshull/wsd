import random
import csv

def remove_quotes(sentence):
    if sentence.startswith('"') and sentence.endswith('"'):
        return sentence[1:-1]
    return sentence

def create_wic_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()

    lemma = ''
    sentence_pairs = []

    for line in lines:
        line = line.strip()

        if line.startswith('Beseda:'):
            lemma = line.split()[1]
        elif ":" in line:
            cent, poved = line.split(":", 1)
            sentence_pairs.append([lemma, remove_quotes(poved.strip()), ''])

    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['lema', 'stavek_1', 'stavek_2', 'oznaka (label)'])  # Write header
        writer.writerows(sentence_pairs)

    print(f"CSV file '{output_file}' has been created.")


# Usage example
input_filename = 'iskanje-lem/polisemne-leme-in-stavki/centroidi_final.txt'  # Replace with your input file name
output_filename = 'iskanje-lem/polisemne-leme-in-stavki/WiC_final.csv'  # Replace with your output file name

create_wic_csv(input_filename, output_filename)
