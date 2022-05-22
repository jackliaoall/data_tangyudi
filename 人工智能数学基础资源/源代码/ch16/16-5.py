#16-5.py

import pandas as pd
from sklearn.cluster import KMeans
#聚类操作
df = pd.read_csv('./datasets/ch1ex1.csv')
points = df.values

model = KMeans(n_clusters=3)
model.fit(points)
labels = model.predict(points)
print(labels)
