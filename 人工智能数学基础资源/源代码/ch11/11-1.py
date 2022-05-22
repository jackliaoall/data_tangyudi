import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#creating and configuration of the figure
plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.yaxis.set_ticks([1,2,3,4,5,6])

X = np.linspace(0,1, 101,endpoint=True)
X=X[1:100]

#output the probility sequence
print(X)

#plotting the uncertainty of coresponding to probility
Y=-1*X*np.log2(X)
print(X[np.argmax(Y)],np.max(Y))
plt.plot(X,Y,color='green',linewidth=2,label='p*log2(p)')

#plotting information entropy
Y=-1*np.log2(X)
plt.plot(X,Y,color='red',linestyle='dashed',label='log2(p)')

#showing the figure label
plt.legend();