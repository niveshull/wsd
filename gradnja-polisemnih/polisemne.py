import cla
import csv

#za generiranje uporabljen elexis-wsd-1.0, pot je potrebno prilagoditi, če se program vnovično uporablja

with open('../elexis-wsd-1.0/elexis-wsd-sl_sense-inventory.tsv', 'r', encoding='utf-8') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')

    polysemous_words = []

    counts = {}

    for row in reader:
        lemma = row[0]
        sense_id = row[2]

        if lemma not in counts:
            counts[lemma] = 1
        else:
            counts[lemma] += 1

    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    for lemma, count in sorted_counts:
        if count > 1:
            polysemous_words.append(lemma)
            if len(polysemous_words) >= 250:
                break

    with open('polysemous_words.txt', 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(polysemous_words))
        print(f"Saved {len(polysemous_words)} polysemous words to polysemous_words.txt")



with open('../elexis-wsd-1.0/elexis-wsd-sl_sense-inventory.tsv', 'r', encoding='utf-8') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')

    unique_lemmas = set()

    for row in reader:
        lemma = row[0]

        unique_lemmas.add(lemma)

    print("There are", len(unique_lemmas), "unique lemmas in the file.")
