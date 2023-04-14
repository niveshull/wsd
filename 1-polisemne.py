import cla
import csv

# open the TSV file and read its contents
with open('elexis-wsd-1.0/elexis-wsd-sl_sense-inventory.tsv', 'r', encoding='utf-8') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')

    # create an empty list to store the polysemous words
    polysemous_words = []

    # create an empty dictionary to store the counts
    counts = {}

    # iterate over each row in the TSV file
    for row in reader:
        # extract the lemma and sense_id from the row
        lemma = row[0]
        sense_id = row[2]

        # if the lemma is not in the dictionary, add it with a count of 1
        if lemma not in counts:
            counts[lemma] = 1
        # if the lemma is already in the dictionary, increment its count
        else:
            counts[lemma] += 1

    # sort the lemmas based on their counts, in descending order
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    # add the polysemous words to the list
    for lemma, count in sorted_counts:
        if count > 1: # check if the count is greater than 1, meaning the word is polysemous
            polysemous_words.append(lemma)
            if len(polysemous_words) >= 250: # break out of the loop if 100 words have been added
                break

    # save the first 250 polysemous words to a new text file
    with open('polysemous_words.txt', 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(polysemous_words))
        print(f"Saved {len(polysemous_words)} polysemous words to polysemous_words.txt")



# open the TSV file and read its contents
with open('elexis-wsd-1.0/elexis-wsd-sl_sense-inventory.tsv', 'r', encoding='utf-8') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')

    # create an empty set to store the unique lemmas
    unique_lemmas = set()

    # iterate over each row in the TSV file
    for row in reader:
        # extract the lemma from the row
        lemma = row[0]

        # add the lemma to the set of unique lemmas
        unique_lemmas.add(lemma)

    # print the total number of unique lemmas
    print("There are", len(unique_lemmas), "unique lemmas in the file.")
