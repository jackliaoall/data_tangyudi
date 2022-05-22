import numpy as np

#create some probilities with the sum=1
np.random.seed(42)
x=np.random.randint(200,size=10)
x=np.unique(x)
x=x/np.sum(x)
print(x)

#output information entropy of uniform probility and random probility
print(np.sum(-1*x*np.log2(x)))
print(-1*np.log2(1/len(x)))