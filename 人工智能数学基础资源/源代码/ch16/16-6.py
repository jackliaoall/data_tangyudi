#16-6.py

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#聚类操作
df = pd.read_csv('./datasets/ch1ex1.csv')
points = df.values

model = KMeans(n_clusters=3)
model.fit(points)
labels = model.predict(points)

#聚类中心
centroids = model.cluster_centers_
centroids_x = centroids[:,0]
centroids_y = centroids[:,1]

#原始数据点
xs = points[:,0]
ys = points[:,1]

#build marker list and colors list
mk0=['o', ',', 'v']
cs0=['r', 'g', 'b']
mk1=[]
cs1=[]
for e in labels:
    mk1.append(mk0[e])
    cs1.append(cs0[e])
#plot dots in the for loop and centroid out of loop
plt.figure(figsize=(10,6),dpi=120)
plt.subplot(111)
for x,y,cr,m in zip(xs,ys,cs1,mk1):
    plt.scatter(x, y, edgecolors=cr, facecolors='none', marker=m)
plt.scatter(centroids_x, centroids_y, marker='X', s=200,c='k')
plt.show()
