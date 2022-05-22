import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
%matplotlib inline

def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s

def sigmoid_derivative(x):
    s=sigmoid(x)
    ds = s*(1-s)
    return ds

#creating and configuration of the figure
plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)
plt.title('sigmoid function & sigmoid derivative function',fontsize=16)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.yaxis.set_ticks([0.2,0.4,0.6,0.8,1.0])
xminorLocator = MultipleLocator(0.5) 
yminorLocator = MultipleLocator(0.1) 
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

#creating x sequence
X = np.linspace(-10,10, 201,endpoint=True)
#print(X)

#plotting sigmoid function and its dirivative function
Y=sigmoid(X)
dY=sigmoid_derivative(X)
plt.plot(X,Y,color='green',linewidth=2,label='sigmoid function')
plt.plot(X,dY,color='red',linestyle='dashed',label='sigmoid derivative function')
plt.legend()
plt.show()