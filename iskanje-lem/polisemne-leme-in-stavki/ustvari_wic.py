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
    groups = {}
    group = []
    for line in lines:
        line = line.strip()
        if line.startswith('Beseda:'):
            lemma = line.split()[1]
        elif ":" in line:
            cent, poved = line.split(":", 1)
            group.append(remove_quotes(poved.strip()))

        if not line or line == lines[-1]:
            if group:
                if lemma in groups:
                    groups[lemma].extend(group)
                else:
                    groups[lemma] = group
            group = []

    sentence_pairs = []
    used_sentences = set()
    for lemma, group in groups.items():
        if len(group) > 1:
            random.shuffle(group)
            for i in range(len(group) - 1):
                sentence1 = group[i]
                sentence2 = group[i + 1]
                if sentence1 not in used_sentences and sentence2 not in used_sentences:
                    sentence_pairs.append([lemma, sentence1, sentence2])
                    used_sentences.add(sentence1)
                    used_sentences.add(sentence2)

    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['lema', 'stavek_1', 'stavek_2', 'oznaka (label)'])  # Write header
        writer.writerows(sentence_pairs)

    print(f"CSV file '{output_file}' has been created.")


# Usage example
input_filename = 'centroidi_final.txt'  # Replace with your input file name
output_filename = 'WiC_final.csv'  # Replace with your output file name

create_wic_csv(input_filename, output_filename)
