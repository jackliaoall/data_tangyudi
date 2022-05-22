import numpy as np
import matplotlib.pyplot as plt
import math
def p(x):
#标准正态分布
    mu=0
    sigma=1
    return 1/(math.pi*2)**0.5/sigma*np.exp(-(x-mu)**2/2/sigma**2)
def q(x):
#参考分布选用[-4,4]上的均匀分布
    return np.array([0.125 for i in range(len(x))])
x=np.linspace(-4,4,500)
k=3.5
N=1000  #样本个数
i=1
count=0
samples=np.array([])
while i<N:
    u=np.random.rand(10)   #每次评估10个样本
    x=(np.random.rand(10)-0.5)*8
    res=u < (p(x)/(q(x)*k))
    if any(res):
        #接受满足条件的样本
        samples=np.hstack((samples,x[res]))
        i+=len(x[res])
    count+=10
count -=len(samples)-1000
samples=samples[:1000]
x=np.linspace(-4,4,500)
plt.plot(x,p(x))
plt.hist(samples,100,density=True,facecolor='blue')
plt.title('Rejection Sampling',fontsize=24)
plt.xlabel('x',fontsize=14)
plt.ylabel('p(x)',fontsize=14)
plt.show()
print(N/count)

