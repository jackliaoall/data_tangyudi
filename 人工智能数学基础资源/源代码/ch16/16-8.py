#16-8.py

import pandas as pd

df = pd.read_csv('./datasets/fish.csv')
species = list(df['species'])
del df['species']
df.head()
