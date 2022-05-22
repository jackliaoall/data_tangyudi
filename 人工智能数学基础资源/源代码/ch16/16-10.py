#16-10.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import DBSCAN
from collections import  Counter
%matplotlib inline

plt.figure(figsize=(12,8),dpi=100)
#Generate the Data Source with sklearn
X1, _=datasets.make_moons(n_samples=500, noise=.05)
X2, _= datasets.make_blobs(n_samples=100, n_features=2, centers=[[1.2,1.2]], 
                           cluster_std=[[.1]],random_state=9)
X = np.concatenate((X1, X2))

#colors and markers for the scatter graph
colors=['black','green','yellow','brown','blue','orange','red']
markers=['o',',','v','^','<','>','x']

#Graph for the Data Source
p11=plt.subplot(221)
p11.set_title('Data Source Graph')
plt.scatter(X[:, 0], X[:, 1],c=colors[0], marker=markers[0])

#Graph for the clustering with default params
p12=plt.subplot(222)
p12.set_title('Clustering BY DB with Defaut params')
y_pred = DBSCAN().fit_predict(X)
for x,y,i in zip(X[:,0],X[:,1],y_pred):
    plt.scatter(x,y,c=colors[i],marker=markers[i])

#Graph for the clustering with specified params
p21=plt.subplot(223)
p21.set_title('Clustering BY DB with Eps=0.1')
y_pred = DBSCAN(eps = 0.10, min_samples = 10).fit_predict(X)
#print(Counter(y_pred))
for x,y,i in zip(X[:,0],X[:,1],y_pred):
    plt.scatter(x,y,c=colors[i],marker=markers[i])
    
#Graph for the clustering with specified params    
p22=plt.subplot(224)
p22.set_title('Clustering BY DB with Eps=0.12')
y_pred = DBSCAN(eps = 0.12, min_samples = 10).fit_predict(X)
#print(Counter(y_pred))
for x,y,i in zip(X[:,0],X[:,1],y_pred):
    plt.scatter(x,y,c=colors[i],marker=markers[i])

plt.show()
