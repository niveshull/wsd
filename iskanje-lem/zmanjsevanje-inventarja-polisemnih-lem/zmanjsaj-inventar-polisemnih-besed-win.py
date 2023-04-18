import xml.etree.ElementTree as ET
import os
import csv

import codecs

types_of_encoding = ["utf-8", "cp1252"]
for encoding_type in types_of_encoding:
    with codecs.open("inventar-polisemnih-besed.tsv", encoding=encoding_type, errors="replace") as f1:
        senses = [line.strip() for line in f1]

with open("polisemne_Klara.txt", "r") as f2:
    words = set([line.strip() for line in f2])

filtered_senses = [sense for sense in senses if sense.split("\t")[0] in words]

for encoding_type in types_of_encoding:
    with codecs.open("inventar-polisemnih-zmanjsan_Klara.tsv", "w", encoding=encoding_type, errors="replace") as f3:
        f3.write("\n".join(filtered_senses))
