import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats
from math import sqrt
#解决汉字显示
mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams['axes.unicode_minus'] = False
f = plt.figure(figsize=(16, 8))
# [0,1]范围内的均匀分布的均值和方差
mean, var = 0.5, 1.0/12
def p_norm(nvr):
#由中心极限定理得：n个随机变量的和服从正态分布，画出正态分布曲线
    mu = mean
    sigma = np.sqrt(var/nvr)
    norm_dis = stats.norm(mu, sigma)
    norm_x = np.linspace(0, 1, 128)
    pdf = norm_dis.pdf(norm_x)
    plt.plot(norm_x, pdf, 'r', alpha=0.6, label='N(${0:.1f}, {1:.2f}^2$)'.format(mu, sigma))
    plt.legend(loc='upper left', prop={'size': 8})
def sample(rv_num):
#对随机变量（X1+X2+...）进行一次采样
    single_sample_dist = stats.uniform(loc=0, scale=1)  # 定义[0，1]上的均匀分布
    x=0
    for j in range(rv_num):
        x+=single_sample_dist.rvs()
    x *= 1 / rv_num   #返回一个 样本
    return x
def plotHist(rv_num, n_):
#画出n个随机变量和样本的直方图，rv_num:随机变量的个数 , Sample_num:样本数目
    x = np.zeros((Sample_num))
    sp = f.add_subplot(2, 2, n_)
    for i in range(Sample_num):  #采样1000次
        x[i]=sample(rv_num)
    #画出直方图
    plt.hist(x, 500,density=True,color='#348ABD',label='{} 个随机变量'.format(rv_num))
    plt.setp(sp.get_yticklabels(), visible=False)
    #画出红色的正态分布曲线
    p_norm(rv_num)
#主程序
Sample_num = 1000     #样本数目
nvr = ([1, 2, 32, 64])         #随机变量的个数分别为1，2，32,64
for i in range(np.size(nvr)):
    plotHist(nvr[i], i + 1)
plt.suptitle("服从均匀分布U[0,1]的多个随机变量和的均值逼近于正态分布")
plt.show()