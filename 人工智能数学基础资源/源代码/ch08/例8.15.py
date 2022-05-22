import numpy as np
from math import sqrt
#生成样本数据
nlist=range(0,9000000)
nlist=[float(i)/1000000 for i in nlist]
N=len(nlist)
#第一种方法编程实现，通过遍历数组来求样本的均值和方差：
sum1=0.0
sum2=0.0
for i in range(N):
    sum1+=nlist[i]
    sum2+=nlist[i]**2
mean=sum1/N
var=sum2/N-mean**2
std=sqrt(var)
print("1、均值为：%f,方差为：%f,标准差为:%f" % (mean,var,std))
#第二种方法：借助numpy的向量运算来求样本的均值和方差：
narray=np.array(nlist)
sum1=narray.sum()
narray2=narray*narray
sum2=narray2.sum()
mean1=sum1/N
var1=sum2/N-mean**2
std1=sqrt(var1)
print("2、均值为：%f,方差为：%f,标准差为:%f" % (mean1,var1,std1))
#第三种方法：借助numpy的函数来求样本的均值和方差：
arr_mean = np.mean(nlist)  # 求均值
arr_var = np.var(nlist)    # 求方差
arr_std = np.std(nlist, ddof=1)  # 求标准差
print("3、均值为：%f,方差为：%f,标准差为:%f" % (arr_mean,arr_var,arr_std))
