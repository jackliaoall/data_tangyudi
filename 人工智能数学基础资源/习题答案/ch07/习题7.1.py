#coding: UTF-8
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#第1 步，定义随机变量
mu4 = 2  # 平均值：每天发生2次事故
# 发生事故次数，包含0次，1次，2次，3次，4次事故
X4 = np.arange(0,5,1)
pList4 = stats.poisson.pmf(X4,mu4)
pList4
# 第3步，绘图
plt.plot(X4,pList4,marker='o',linestyle='None')
plt.vlines(X4,0,pList4)
plt.xlabel('某路口发生k次事故')
plt.ylabel('概率')
plt.title('泊松分布：平均值mu=%i' % mu4 )
plt.show()
