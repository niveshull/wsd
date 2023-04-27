ELEXIS-WSD – A Parallel Sense-Annotated Corpus
v1.0
http://hdl.handle.net/11356/1674
CC-BY-SA 4.0

Lead: Federico Martelli, Roberto Navigli, Simon Krek
Estonian: Jelena Kallas, Kristina Koppel, Margit Langemets, Tiiu Üksik
Slovene: Simon Krek, Polona Gantar, Jaka Čibej, Kaja Dobrovoljc, Tina Munda
English: Kaja Dobrovoljc, Luka Terčon
Danish: Sanni Nimb, Bolette Sandford Pedersen, Sussi Olsen
Bulgarian: Svetla Koeva
Spanish: Rafael Ureña-Ruiz, José-Luis Sancho-Sánchez
Hungarian: Veronika Lipp, Tamás Váradi, András Győrffy, Simon László
Italian: Valeria Quochi, Monica Monachini, Francesca Frontini
Dutch: Carole Tiberius, Rob Tempelaars
Portuguese: Rute Costa, Ana Salgado

ELEXIS-WSD is a parallel sense-annotated corpus in which content words (nouns, adjectives, verbs, and adverbs) have been assigned senses. Version 1.0 contains sentences for 10 languages: Bulgarian, Danish, English, Spanish, Estonian, Hungarian, Italian, Dutch, Portuguese, and Slovene.

##### CORPUS COMPILATION #####
The corpus was compiled by automatically extracting a set of sentences from WikiMatrix (Schwenk et al., 2019), a large open-access collection of parallel sentences derived from Wikipedia, using an automatic approach based on multilingual sentence embeddings. The sentences were manually validated according to specific formal, lexical, and semantic criteria (e.g. by removing incorrect punctuation, morphological errors, notes in square brackets and etymological information typically provided in Wikipedia pages). To obtain a satisfying semantic coverage, we filtered out sentences with less than 5 words and less than 2 polysemous words were filtered out. Subsequently, in order to obtain datasets in the other nine target languages, for each selected sentence in English, the corresponding WikiMatrix translation into each of the other languages was retrieved. If no translation was available, the English sentence was translated manually. The resulting corpus is comprised of 2,024 sentences for each language.

The compilation process is described in more detail in Martelli et al. (2021).

##### ANNOTATION #####
The sentences were tokenized, lemmatized, and tagged with POS tags using UDPipe v2.6 (https://lindat.mff.cuni.cz/services/udpipe/). Senses were annotated using LexTag (https://elexis.babelscape.com/): each content word (noun, verb, adjective, and adverb) was assigned a sense from among the available senses from the sense inventory selected for the language (see below) or BabelNet. Sense inventories were also updated with new senses during annotation.

List of sense inventories
BG: Dictionary of Bulgarian
DA: DanNet – The Danish WordNet
EN: Open English WordNet
ES: Spanish Wiktionary
ET: The EKI Combined Dictionary of Estonian
HU: The Explanatory Dictionary of the Hungarian Language
IT: PSC + Italian WordNet
NL: Open Dutch WordNet
PT: Portuguese Academy Dictionary (DACL)
SL: Digital Dictionary Database of Slovene

##### FORMAT #####
The corpus is available in a CONLL-like tab-separated format, with each sentence starting with the attributes "# text" (containing the entire text of the sentence) and "# sent_id" (containing the ID of the sentence). The sentence IDs consist of the sentence number and the language – The English sentence 1.en corresponds to the Bulgarian sentence 1.bg, the Danish sentence 1.da, etc.

# text = In the fifth season the program was implemented in accordance with a new concept: one young footballer from each country was chosen to represent it.
# sent_id = 1.en

In order, the columns contain the token ID, its form, its lemma, its UPOS-tag, its whitespace information (whether the token is followed by a whitespace or not), the ID of the sense assigned to the token, and the index of the multiword expression (if the token is part of an annotated multiword expression).

##### MULTIWORD TOKENS #####
Multiword tokens have token IDs containing "-", with the first number representing the starting token and the second number the ending token. Individual tokens are listed directly after the multiword token, as in the Dutch example below, where "solosucces" was subtokenized into "solo" and "succes". Individual tokens were then annotated with the corresponding senses.

# text = Frey behaalde solosucces in de jaren tachtig.
# sent_id = 1450.nl
1	Frey	Frey	PROPN	_	_	_
2	behaalde	behalen	VERB	_	6053e953dde807025a6e8fa3@_r_v_1169	_
3-4	solosucces	_	_	_	_	_
3	solo	solo	ADV	_	lexli:flVfR72htqdmabg4ZwLa3BFenDXYDdQrA39FbOdgSUaptRfdrgpL4s0fAo	_
4	succes	succes	NOUN	_	6053e953dde807025a6f1c95@_r_n_36543	_
5	in	in	ADP	_	non-content-word	_
6	de	de	DET	_	non-content-word	_
7	jaren	jaar	NOUN	_	6053e953dde807025a6ec9f2@_r_n_18341	_
8	tachtig	tachtig	NOUN	SpaceAfter=No	6053e953dde807025a6f1dc0@_o_n_692562577	_
9	.	.	PUNCT	_	non-content-word	_


##### MULTIWORD EXPRESSIONS #####
Multiword expresssions are annotated in the seventh (last) column – all tokens included in a MWE contain the same MWE-index (e.g. "MWE_1", "MWE_2").

MWEs containing multiword tokens are annotated on the level of the multiword token, not on the level of individual tokens. See the Dutch example below, where "Kamerparlement" was subtokenized as "Kamer" and "parlement" and is part of the multiword expression "Tweede Kamerparlement".

5	Tweede	tweede	ADJ	_	lexli:1QMTfjTLjrWFU2wWhACzUIjfNF2jJiB4uVyBIl1PngdO0vMDqXPSBGAJu1	MWE_1
6-7	Kamerparlement	_	_	SpaceAfter=No	lexli:1QMTfjTLjrWFU2wWhACzUIjfNF2jJiB4uVyBIl1PngdO0vMDqXPSBGAJu1	MWE_1
6	Kamer	kamer	NOUN	_	_	_
7	parlement	parlement	NOUN	_	_	_
8	,	,	PUNCT	_	non-content-word	_

##### SENSE INVENTORIES #####
Each language has a separate sense inventory containing all the senses (and their definitions) used for annotation in the corpus. Not all the senses from the sense inventory are necessarily included in the corpus annotations: for instance, all occurrences of the English noun "bank" in the corpus might be annotated with sense of "financial institution", but the sense inventory also contains the sense "edge of a river" as well as all other possible senses to disambiguate between.

Some of the corpora have (to varying extents) also been annotated using BabelNet concepts – BabelNet synset IDs are available in version 1.0, but the definitions are not included in the sense inventories. For definitions of these synset IDs, please refer to BabelNet (https://babelnet.org/).

##### REFERENCES #####
Martelli, Federico, Roberto Navigli, Simon Krek, Jelena Kallas, Polona Gantar, Svetla Koeva, Sanni Nimb, Bolette Sandford Pedersen, Sussi Olsen, Margit Langemets, Kristina Koppel, Tiiu Üksik, Kaja Dobrovoljc, Rafael Ureña-Ruiz, José-Luis Sancho-Sánchez, Veronika Lipp, Tamás Váradi, András Győrffy, Simon László, Valeria Quochi, Monica Monachini, Francesca Frontini, Carole Tiberius, Rob Tempelaars, Rute Costa, Ana Salgado, Jaka Čibej, Tina Munda. (2021): Designing the ELEXIS Parallel Sense-Annotated Dataset in 10 European Languages. In: Iztok Kosem, Michal Cukr, Miloš Jakubíček, Jelena Kallas, Simon Krek, Carole Tiberius (eds.). Electronic lexicography in the 21st century. Proceedings of the eLex 2021 conference. 5–7 July 2021, virtual. Brno: Lexical Computing CZ, s.r.o., pp. 377–395.  https://elex.link/elex2021/wp-content/uploads/2021/08/eLex_2021_22_pp377-395.pdf

@article{martellietal2021,
   author={Martelli, Federico and Roberto Navigli and Simon Krek and Jelena Kallas and Polona Gantar and Svetla Koeva and Sanni Nimb and Bolette Sandford Pedersen and Sussi Olsen and Margit Langemets and Kristina Koppel and Tiiu Üksik and Kaja Dobrovoljc and Rafael Ureña-Ruiz and José-Luis Sancho-Sánchez and Veronika Lipp and Tamás Váradi and András Győrffy and Simon László and Valeria Quochi and Monica Monachini and Francesca Frontini and Carole Tiberius and Rob Tempelaars and Rute Costa and Ana Salgado and Jaka Čibej and Tina Munda},
   title={Designing the ELEXIS Parallel Sense-Annotated Dataset in 10 European Languages},
   journal={Electronic lexicography in the 21st century. Proceedings of the eLex 2021 conference.},
   editor={Iztok Kosem and Michal Cukr and Miloš Jakubíček and Jelena Kallas and Simon Krek and Carole Tiberius},
   year=2021,
   pages={377-395}
}

Schwenk, Holger, Vishrav Chaudhary, Shuo Sun, Hongyu Gong, Francisco Guzmán. (2019): WikiMatrix: Mining 135M Parallel Sentences in 1620 Language Pairs from Wikipedia. CoRR 2019. https://arxiv.org/abs/1907.05791

@article{DBLP:journals/corr/abs-1907-05791,
  author    = {Holger Schwenk and
               Vishrav Chaudhary and
               Shuo Sun and
               Hongyu Gong and
               Francisco Guzm{\'{a}}n},
  title     = {WikiMatrix: Mining 135M Parallel Sentences in 1620 Language Pairs
               from Wikipedia},
  journal   = {CoRR},
  volume    = {abs/1907.05791},
  year      = {2019},
  url       = {http://arxiv.org/abs/1907.05791},
  eprinttype = {arXiv},
  eprint    = {1907.05791},
  timestamp = {Wed, 17 Jul 2019 10:27:36 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1907-05791.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}

##### ACKNOWLEDGMENTS #####
The ELEXIS project (European Lexicographic Infrastructure) has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 731015.

