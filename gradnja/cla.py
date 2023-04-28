import classla
#classla.download("sl")
nlp=classla.Pipeline(lang="sl")

word = input("Enter a word: ")

d = nlp(word)

lemma_dict = {}
lemma = d[1]
word_form = d[0]
if lemma not in lemma_dict:
    lemma_dict[lemma] = [word_form]
else:
    lemma_dict[lemma].append(word_form)

print(lemma_dict)
