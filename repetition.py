#this script calculates Lempel ziv score

import pandas as pd

#introduces the stopwords and removes words not needed for repetition counter
cus_stopwords =['instrumental', 'verse', 'chorus', 'bridge', 'refrain', 'hook', 'intro', 'outro',
                              'Instrumental','spoken', 'prechorus',
                'postchorus', 'interlude', 'produced']
stops = cus_stopwords

#introduce file with lyrics section
df = pd.read_csv("Tokenized3.csv")
df['strip'] = df['lyrics'].apply(str)
df['strip'] = df['strip'].str.replace("[^\w\s]", "",regex = True).str.lower()

df['strip'] = df['strip'].apply(lambda x: ' '.join([item for item in x.split() if item not in stops]))
df['strip'].str.split(expand=True).stack().value_counts()

df["strip"].fillna(value ='no lyrics', inplace=True)

from lempel_ziv_complexity import lempel_ziv_complexity

def rich(row):
    return lempel_ziv_complexity(row)

df['repetition'] = df.apply(lambda row: rich(row['strip']), axis=1)

#outputs file with counted Lempel-Ziv score
df.to_csv('Tokenized4.csv')