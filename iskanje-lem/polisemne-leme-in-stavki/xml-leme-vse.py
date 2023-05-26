import xml.etree.ElementTree as ET
import os
import csv
import re

with open('../zmanjsevanje-inventarja-polisemnih-lem/polisemne_besede.txt', 'r', encoding='utf-8') as f:
    polysemous_lemmas = set([line.strip() for line in f.readlines()])

stavki_s_polisemi = []

with open('seznam-polisemnih.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Stavek', 'Polisemna lema'])

    input_directory = "../../datasets/ccKres_LEMATIZIRAN"
    for filename in os.listdir(input_directory):
        if filename.endswith(".xml"):
            filepath = os.path.join(input_directory, filename)
            tree = ET.parse(filepath)
            root = tree.getroot()

            for odstavek_st, p in enumerate(root[1][0]):
                polisem_found_in_par = False

                for poved_st, s in enumerate(p):
                    #print(f"\n- Odstavek št. {odstavek_st}, poved št. {poved_st}:")
                    stavek = ""
                    polisem_found = False
                    polisem_lemmas = []

                    for w in s:
                        #print(w.tag)
                        #print(f"Posamezna beseda: {w.text}")
                        if w.text == None:
                            stavek += " "
                        else:
                            stavek += str(w.text)

                        if w.tag == '{http://www.tei-c.org/ns/1.0}w':
                            #print(w.attrib["lemma"], w.text)
                            lemma = w.attrib["lemma"]
                            #print("Lema: ", lemma)
                            if lemma in polysemous_lemmas:
                                polisem_found = True
                                polisem_lemmas.append(lemma)
                                print(f">>> Lema '{lemma}' je polisem.")

                    if polisem_found:
                        num_words = len(stavek.split())
                        if 10 < num_words < 250:
                            stavek = stavek.strip()
                            stavki_s_polisemi.append((odstavek_st, poved_st, stavek))
                            polisem_found_in_par = True
                            print(f"Stavek: {stavek}")
                            writer.writerow([stavek, ';'.join(polisem_lemmas)])

                if polisem_found_in_par == True:
                        print(f"- Polisem najden: odstavek št. {odstavek_st}.\n")
                        pass

print(f"Št. stavkov, ki vsebujejo poliseme: {len(stavki_s_polisemi)}")
print("\nStavki, ki vsebujejo poliseme:")
for i, (odstavek_st, poved_st, stavek) in enumerate(stavki_s_polisemi):
    print(f"{i+1}. (odstavek {odstavek_st}, poved {poved_st}): {stavek}")