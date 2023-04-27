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

with open('/home/nives/Projekti/ONJ-p/seznam-polisemnih-nives-excel.csv', 'r') as input_file:
    csvreader = csv.reader(input_file, delimiter = ";")
    next(csvreader)

    for row in csvreader:
        besede = row[0].split(";")
        stavek = row[1]
        for b in besede:
            all_sentences[b].append(stavek)

print(all_sentences.keys())
#print(all_sentences["agresiven"])
print("St. besed:", len(all_sentences.keys()))


for beseda in all_sentences.keys():
    print("TOLE ZDAJ JE ZA BESEDO:", beseda)
    stavki = all_sentences[beseda]
    embeddings = model.encode(stavki)

    #print(beseda)
    #print(stavki[0])
    #print(embeddings[0])

    df = np.array(embeddings)
    #print(df)

    # PCA
    sklearn_pca = PCA(n_components = 2) # Using PCA to remove cols which has less co-relation
    Y_sklearn = sklearn_pca.fit_transform(df) #fit_transform() is used to scale training data to learn parameters such as 
    # mean & variance of the features of training set and then these parameters are used to scale our testing data.
    #print(Y_sklearn)

    plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1], s=100)
    plt.title("Besede: " + beseda)
    #plt.show()

    # Clustering
    kmeans = KMeans(n_clusters=10)# Partition 'n' no. of observations into 'k' no. of clusters. 
    #fitted = kmeans.fit(df) # Fitting k-means model  to feature array
    fitted = kmeans.fit(Y_sklearn)
    predictions = kmeans.predict(Y_sklearn) # predicting clusters class '0' or '1' corresponding to 'n' no. of observations
    #print(stavki[0], predictions[0])

    assert len(stavki) == len(predictions)

    plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1], c=predictions, s=100)
    plt.title("Besede: " + beseda)
    #plt.show()

    # Find centroid
    centri = kmeans.cluster_centers_
    #print(en_stavek_st)

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

        print("CENTER:", i, "STAVEK:", min_stavek)
    
    
    
    # Print resulting sentences
    pass

