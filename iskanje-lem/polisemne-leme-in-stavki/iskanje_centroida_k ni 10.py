from collections import defaultdict
from math import sqrt
import csv

from sentence_transformers import SentenceTransformer

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.decomposition import PCA

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

all_sentences = defaultdict(list)

with open('seznam-polisemnih-urejeno-katarina.csv', 'r', encoding='utf-8') as input_file:
    csvreader = csv.reader(input_file, delimiter = ";")
    next(csvreader)

    for row in csvreader:
        besede = row[0].split(";")
        stavek = row[1]
        for b in besede:
            all_sentences[b].append(stavek)

with open('centroidi_katarina_test.txt', 'w', encoding='utf-8') as output_file:
    for beseda in all_sentences.keys():
        output_file.write("Beseda: {}\n".format(beseda))
        stavki = all_sentences[beseda]
        embeddings = model.encode(stavki)

        df = np.array(embeddings)

        # PCA
        sklearn_pca = PCA(n_components = 2)
        Y_sklearn = sklearn_pca.fit_transform(df)

        k = 10
        while k > 0:
            # Clustering
            kmeans = KMeans(n_clusters=k)
            fitted = kmeans.fit(Y_sklearn)
            predictions = kmeans.predict(Y_sklearn)

            if len(set(predictions)) == k:
                # All clusters have been formed
                break
            else:
                # Reduce k and try again
                k -= 1

        assert len(stavki) == len(predictions)

        # Find centroid
        centri = kmeans.cluster_centers_

        for i, c in enumerate(centri):
            min_dist = np.inf
            min_stavek = None
            for y, st in zip(Y_sklearn, stavki):
                c1, c2 = c
                y1, y2 = y

                curr_dist = sqrt((c1 - y1)**2 + (c2 - y2)**2)
                if curr_dist < min_dist:
                    min_dist = curr_dist
                    min_stavek = st

            output_file.write("CENTER {}: {}\n".format(i, min_stavek))

        output_file.write("\n")
