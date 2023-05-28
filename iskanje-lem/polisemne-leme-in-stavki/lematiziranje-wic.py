import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

input_file = 'preformatiran-manual-evaluation.tsv'
output_file = 'preformatiran-manual-evaluation-leme.tsv'

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def find_wordform(lemma, sentence):
    tokens = word_tokenize(sentence)
    for token in tokens:
        token_lemma = lemmatizer.lemmatize(token)
        if token_lemma == lemma:
            return token
    return None

with open(input_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='\t')
    rows = list(reader)

header_row = rows[0]
lemmas = header_row[1:]

# Process each lemma in the TSV file
for lemma in lemmas:
    # Add <target> tags around the correct wordform in each sentence for the current lemma
    for row in rows[1:]:
        if row[0] == lemma:
            wordform1 = find_wordform(row[0], row[1])
            wordform2 = find_wordform(row[0], row[2])
            if wordform1 is not None:
                row[1] = row[1].replace(wordform1, '<target>' + wordform1 + '</target>', 1)
            if wordform2 is not None:
                row[2] = row[2].replace(wordform2, '<target>' + wordform2 + '</target>', 1)

with open(output_file, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(rows)

print(f"Output file '{output_file}' has been generated.")
