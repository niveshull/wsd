with open("inventar-polisemnih-besed.tsv", "r", encoding="utf-8") as f1:
    senses = [line.strip() for line in f1]

with open("polisemne_besede.txt", "r", encoding="utf-8") as f2:
    words = set([line.strip() for line in f2])

filtered_senses = [sense for sense in senses if sense.split("\t")[0] in words]

with open("inventar-polisemnih-zmanjsan.tsv", "w", encoding="utf-8") as f3:
    f3.write("\n".join(filtered_senses))