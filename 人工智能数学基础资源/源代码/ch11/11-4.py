import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
%matplotlib inline

def tanh(x):
    s = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    return s

def tanh_derivative(x):
    s=tanh(x)
    ds = 1-s*s
    return ds

#creating and configuration of the figure
plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)
plt.title('tanh function & tanh derivative function',fontsize=16)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.yaxis.set_ticks([-1.0,-0.8,-0.6,-0.4,-0.2,0.2,0.4,0.6,0.8,1.0])
xminorLocator = MultipleLocator(0.5) 
yminorLocator = MultipleLocator(0.1) 
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

#creating x sequence
X = np.linspace(-10,10, 201,endpoint=True)
#print(X)

#plotting tanh function and its dirivative function
Y=tanh(X)
dY=tanh_derivative(X)
plt.plot(X,Y,color='green',linewidth=2,label='tanh function')
plt.plot(X,dY,color='red',linestyle='dashed',label='tanh derivative function')
plt.legend()
plt.show()