# Introduction

Word sense disambiguation (WSD) is an important task in natural language processing that consists of determining the correct meaning of a word based on its context, using a predetermined list of potential meanings. This process is usually performed unconsciously by humans. WSD can be viewed as a classification problem in which the goal is to assign an occurrence of a word to its appropriate sense class based on a dictionary of possible meanings. The context in which the word occurs, including neighboring words, serves as evidence for the classification task. WSD is applicable in various domains, such as machine translation, information retrieval and hypertext navigation, content and thematic analysis, speech processing, knowledge acquisition, information extraction, etc. [[1](#ref1)]

The goal of this project is to prepare a dataset for training WSD models using both automatic and manual methods. The project consists of four steps. To create the dataset, we will first create a list of highly polysemous words from the existing Elexis WSD dataset. Then, sentence pairs containing these words will be extracted from the ccKres corpus using clustering methods and automatic truth value assignment. The sentence pairs will be manually verified, and their truth values corrected as needed. We will also convert the existing Elexis WSD dataset to WiC format and create as many positive and negative examples as possible, which we will then join to the newly generated dataset. The resulting dataset will be used to train WSD models that can determine whether two occurrences of a word in different contexts have the same meaning or not.

Overall, this project aims to contribute to the development of WSD models that can accurately determine the correct meaning of polysemous words in natural language text, which is essential for improving the accuracy of machine translation and other NLP tasks.

# Related work
## WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations [[2](#ref2)]

Word-in-Context is a dataset based on three lexical resources: WordNet, VerbNet, and Wiktionary. It is a binary classification task that aims to determine whether a word used in two different contexts corresponds to the same meaning or not. The dataset consists of examples with a target word and two sentences containing the target word. Each example is either positive or negative, depending on whether the two sentences have the same meaning of the target word. The dataset was compiled by obtaining all possible positive and negative examples from different sources. The test and development sets were created with the intention of obtaining a diverse and balanced set. 1.600 and 800 examples were reserved for testing and development data set, respectively. The remaining examples were used for initial training.

## Elexis WSD [[3](#ref3)]

The dataset we will use to find highly polysemous words is Elexis WSD, a manually curated and annotated dataset consisting of five annotation layers for 10 European languages, including Slovene. The layers include tokenisation, sub-tokenisation, lemmatisation, POS tagging, and Word Sense Disambiguation (WSD). The Slovene dataset was processed using a highly accurate tool called CLASSLA tagger. Two different POS tagsets were used, which could cause confusion for the taggers. To solve this problem, the detailed tagging guidelines UD-POS [[4](#ref4)] for Slovene were consulted. Another problem with this process was the distinction between different categories, such as DET vs PRON and CCONJ vs ADV. In order to obtain more content words, named entity components that are not proper nouns were assigned their appropriate part of speech. Finally, some corrections were made to the lemmatisation, such as manually correcting the lemmatisation of prepositions. The process of tokenisation included no errors.


## References

[1]<a id="ref1"></a> Nancy Ide and Jean Véronis. 1998. Introduction to the Special Issue on Word Sense Disambiguation: The State of the Art. Computational Linguistics, 24(1):1–40.

[2]<a id="ref2"></a> Mohammad Taher Pilehvar and Jose Camacho-Collados. 2019. WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pages 1267–1273, Minneapolis, Minnesota. Association for Computational Linguistics.

[3]<a id="ref3"></a> Federico Martelli et al. 2021. Designing the ELEXIS Parallel Sense-Annotated Dataset in 10 European Languages. In eLex 2021 Proceedings, eLex Conference. Proceedings. Lexical Computing CZ.

[4]<a id="ref4"></a> Kaja Dobrovoljc, Tomaž Erjavec, and Simon Krek. 2017. The Universal Dependencies Treebank for Slovenian. In Proceedings of the 6th Workshop on Balto-Slavic Natural Language Processing, pages 33–38, Valencia, Spain. Association for Computational Linguistics.

[5]<a id="ref5"></a> Resmiyati Restu. 2017. The Distinction between Polysemy and Homonym on lexical Ambiguity. Universitas Indraprasta PGRI.
