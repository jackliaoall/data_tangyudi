#E16-2.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import DBSCAN
from collections import  Counter
%matplotlib inline

plt.figure(figsize=(12,8),dpi=100)
#read Data Source with pandas
df = pd.read_csv('./ch1ex1.csv')
X = df.values

#colors and markers for the scatter graph
colors=['black','green','yellow','brown','blue','orange','red']
markers=['o',',','v','^','<','>','x']


#Graph for the clustering with default params
p12=plt.subplot(121)
p12.set_title('Clustering BY DB with Defaut params')
y_pred = DBSCAN().fit_predict(X)
for x,y,i in zip(X[:,0],X[:,1],y_pred):
    plt.scatter(x,y,c=colors[i],marker=markers[i])

#Graph for the clustering with specified params
p21=plt.subplot(122)
#可以调整参数，进行最近邻聚类观察
eps = 0.6
min_samples = 3
p21.set_title('Clustering BY DB with Eps={:.2f}, MinPts={:2d}'.format(eps,min_samples))

y_pred = DBSCAN(eps = eps, min_samples = min_samples).fit_predict(X)
#print(Counter(y_pred))
for x,y,i in zip(X[:,0],X[:,1],y_pred):
    plt.scatter(x,y,c=colors[i],marker=markers[i])
    
plt.show()