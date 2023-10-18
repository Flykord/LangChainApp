# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:19:47 2023

@author: vazquezd
"""

import os
from sentence_transformers import SentenceTransformer
from nltk import flatten

# all-MiniLM-L6-v2 is the fastest mode in the
# size bracket. You can also use other models
# for better quality or choose smaller models
# for performance. 
# https://www.sbert.net/docs/pretrained_models.html#model-overview

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load corpus
data_dir = "./data"
os.listdir(data_dir)

corpus = []

for filename in os.listdir(data_dir):
    print(f"Loading file {filename}")
    
    with open(f"{data_dir}/{filename}",encoding="utf8") as f:
        doc = f.readlines()
        corpus.append(doc)
        
assert len(corpus) == len(os.listdir(data_dir))

# Build Embeddings
flattened_corpus = flatten(corpus)
embeddings = model.encode(flattened_corpus)
assert embeddings.shape[0] == len(corpus)