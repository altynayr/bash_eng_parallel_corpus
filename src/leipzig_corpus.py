from typing import List, Any

import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup as soup
import lxml


# Load Leipzig corpora
corpora_paths = []
for dirpath, dirnames, filenames in os.walk(os.getcwd() + '/corpora'):
    for fname in filenames:
        if 'sentences' in fname:
            corpora_paths  = corpora_paths + [dirpath + '/' + fname]

data = []
for path in corpora_paths:
    with open(path, 'r') as f:
        corpus = [line.split('\t') +
                [len(line.split())] +
                [path.split('/')[-1]]
                for line in f.readlines()]
    data = data + corpus

df = pd.DataFrame(data, columns = ['id', 'sentence', 'word_count', 'file_name'])

# Load the unicode data to filter Bashkir texts
unicode = pd.read_csv("data/unicode_bash_encodings.txt",
                      header = 0)

cond_1 = [any([letter in sentence for letter in unicode.letter]) for sentence in df.sentence]
df_bashkir = df[cond_1]
df_bashkir_short = df_bashkir[df_bashkir['word_count'] < 8]

# np.histogram(df.word_count)

df_bashkir_short.to_csv("to_translate.csv")

# Wiktionary dump
file_name = 'enwiktionary-20221020-pages-meta-current.xml'

doc = []
with open(file_name, 'r') as f:
    for lines in f:
        if 'Bashkir' in line:
            print(line)