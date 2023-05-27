import csv

input_file = 'NLP manual evaluation.csv'
output_file = 'preformatiran-manual-evaluation.tsv'

with open(input_file, newline='', encoding="utf-8-sig") as csvfile:
    reader = csv.reader(csvfile)
    cleaned_data = []

    for row in reader:
        # Remove trailing commas from each field in the row
        cleaned_row = [field.rstrip(',') for field in row]
        cleaned_data.append(cleaned_row)

with open(output_file, 'w', newline='', encoding="utf-8-sig") as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    writer.writerows(cleaned_data)

print("CSV file converted to TSV and saved as", output_file)