import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams['axes.unicode_minus'] = False
def Discrete_pmf():
    xk = [0,1,2, 3,4 ] # 所有可能的取值
    pk = [1/16, 1/4, 3/8, 1/4, 1/16]  # 各个取值的概率
    #用rv_discrete 类自定义离散概率分布rvs
    custome = stats.rv_discrete(name='rvs', values=(xk, pk))
    #调用其rvs方法20次，获得符合概率的随机数:
    custome1=custome.rvs(size=20)
    fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(10, 5))
    #显示概率函数
    ax0.set_title("概率函数")
    ax0.plot(xk, pk, 'ro', ms=8, mec='r')
    ax0.vlines(xk, 0, pk, colors='r', linestyles='-', lw=2)
    for i in xk:
        ax0.text(i,pk[i]+0.006,'%.2f'%pk[i],ha='center',va='bottom')
    #显示"分布函数"
    pk1=custome.cdf(xk)
    xmax=[1,2,3,4,5]
    ax1.hlines(pk1,xk,xmax,linestyles='-',colors='b')
    xk1=[1,2,3,4]
    ymin=pk1[0:4]
    ymax=pk1[1:5]
    ax1.vlines(xk1,ymin , ymax, colors='b', linestyles='-', lw=2)
    ax1.set_title("分布函数")
    fig.subplots_adjust(wspace=0.4)
    for i in xk:
        ax1.text(i, pk1[i] + 0.003, '%.2f' % pk1[i],ha='center', va='bottom')
    plt.show()
    plt.show()
Discrete_pmf()

