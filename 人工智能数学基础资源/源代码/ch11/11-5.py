import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
%matplotlib inline

def relu(x):
    s = np.where(x <= 0, 0, x)
    return s

def relu_derivative(x):
    ds = np.where(x <= 0, 0, 1)
    return ds

#creating and configuration of the figure
plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)
plt.title('relu function & relu derivative function',fontsize=16)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.yaxis.set_ticks([0.2,0.4,0.6,0.8,1.0])
xminorLocator = MultipleLocator(0.05) 
yminorLocator = MultipleLocator(0.1) 
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

#creating x sequence
X = np.linspace(-0.9,0.9, 91,endpoint=True)
#print(X)

#plotting relu function and its dirivative function
Y=relu(X)
dY=relu_derivative(X)
plt.plot(X,Y,color='green',linewidth=2,label='relu function')
plt.plot(X,dY,color='red',linestyle='dashed',label='relu derivative function')
plt.legend()
plt.show()