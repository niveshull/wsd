import classla
#to je treba naredit samo prvič, ko uporabljaš
classla.download("sl")
#nastavim pipeline (lahko določim, da so stavki recimo že tokenizirani ..., če ne določim nič, je pa defolt)
nlp=classla.Pipeline(lang="sl")

stavek="Delamo z besedami."


#osnovna oblika
"""docx=nlp(stavek)

#lažje dostopam do info v obliki dictionaryja
dictx=docx.to_dict()
print(docx.to_conll())"""


'''
dictx
[([{'id': 1, 'text': 'Danes', 'lemma': 'danes', 'upos': 'ADV', 'xpos': 'Rgp', 'feats': 'Degree=Pos', 'head': 2, 'deprel': 'advmod', 'ner': 'O'}, {'id': 2, 'text': 'je', 'lemma': 'biti', 'upos': 'AUX', 
'xpos': 'Va-r3s-n', 'feats': 'Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin', 'head': 0, 'deprel': 'root', 'ner': 'O'}, {'id': 3, 'text': 'lep', 'lemma': 'lep', 'upos': 'ADJ', 'xpos': 'Agpmsnn', 'feats': 'Case=Nom|Definite=Ind|Degree=Pos|Gender=Masc|Number=Sing', 'head': 5, 'deprel': 'amod', 'ner': 'O'}, {'id': 4, 'text': 'sončen', 'lemma': 'sončen', 'upos': 'ADJ', 'xpos': 'Agpmsnn', 'feats': 'Case=Nom|Definite=Ind|Degree=Pos|Gender=Masc|Number=Sing', 'head': 5, 'deprel': 'amod', 'ner': 'O'}, {'id': 5, 'text': 'dan', 'lemma': 'dan', 'upos': 'NOUN', 'xpos': 'Ncmsn', 'feats': 'Case=Nom|Gender=Masc|Number=Sing', 'head': 2, 'deprel': 'nsubj', 'misc': 'SpaceAfter=No', 'ner': 'O'}, {'id': 6, 'text': '.', 'lemma': '.', 'upos': 'PUNCT', 'xpos': 'Z', 'head': 2, 'deprel': 'punct', 'ner': 'O'}], '# newpar id = 1\n# sent_id = 1.1\n# text = Danes je lep sončen dan.\n')]
'''