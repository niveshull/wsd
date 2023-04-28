import csv

with open('seznam-polisemnih-nives.csv', 'r', encoding="utf-8-sig") as infile, open('seznam-polisemnih-urejeno-nives.csv', 'w', newline='', encoding="utf-8") as outfile:
    reader = csv.reader(infile, delimiter=',')
    writer = csv.writer(outfile, delimiter=';')

    # sort the rows based on the second column
    sorted_rows = sorted(reader, key=lambda row: row[1])

    # swap the contents of the first and second columns and remove quotes from second column
    for row in sorted_rows:
        row[0], row[1] = row[1].replace('"', ''), row[0].replace('"', '')

        writer.writerow(row)