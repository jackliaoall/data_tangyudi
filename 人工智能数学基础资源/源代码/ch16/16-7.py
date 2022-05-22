#16-7.py

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

seeds_df = pd.read_csv('./datasets/seeds.csv')
#print(seeds_df.grain_variety.value_counts())
varieties = list(seeds_df['grain_variety'])
del seeds_df['grain_variety']
seeds_df.head()

samples = seeds_df.values
#print(len(samples))
ks = range(1, 6)
inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)
    # Fit model to samples
    model.fit(samples)
    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)
    
plt.figure(figsize=(10,6),dpi=80)
plt.subplot(111)
# Plot ks vs inertias
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()
