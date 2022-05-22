# 用M-h算法实现对瑞利分布的采样，转移概率用自由度为xt的开方分布
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
def Rayleigh (x, sigma):
    #返回瑞利分布
    if x<0:
        return 0
    elif sigma>0:
        return ((x/sigma**2)*math.exp(-x**2/(2*(sigma**2))))
m=10000
sigma=4
x=[0.00 for i in range(m)]
#从开方分布中获得初始状态x[1]
x[1]=stats.chi2.rvs(df=1)
k=0
for i in range(2,m):
    xt = x[i-1]
    x_star = stats.chi2.rvs(df=math.ceil(xt))
    num = Rayleigh(x_star,sigma)*stats.chi2.pdf(xt,df=math.ceil(x_star))
    den = Rayleigh(xt,sigma)*stats.chi2.pdf(x_star,df=math.ceil(xt))
    u = np.random.uniform(0,1)  #从均匀分布中生成随机数u
    if u <=min(1,num/den):
        x[i]=x_star   #接收样本
    else:
        x[i]=xt
        k=k+1
print("被拒绝的样本数目：",k)
index=[number for number in range(5000,5500)]
y1=x[5000:5500]
fig1 = plt.figure(num='fig1', figsize=(10, 3), dpi=75, facecolor='#FFFFFF', edgecolor='#0000FF')
#马氏链部分样本路径图
plt.plot(index,y1)
fig2 = plt.figure(num='fig2', figsize=(6, 3), dpi=75, facecolor='#FFFFFF', edgecolor='#FF0000')
b=2001  #去掉达到平稳状态之前的样本
y=x[b:m]
#瑞利分布密度函数曲线图
plt.scatter(y,[ Rayleigh (i,4) for i in y] ,color='red',linewidth=1 )
#样本的直方图
plt.hist(y, 25, density=True,facecolor='white', edgecolor='black',alpha=1)
plt.show()