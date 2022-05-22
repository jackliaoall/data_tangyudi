#调用
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import summary_table
#回归公式是: y=3+6x+2x^3+e
#1、设定数据量
nsample=50
#2、创建一个表示x的array。这里，设x的值是-10到 10 等差排列，共50个数。
x=np.linspace(-10,10, nsample)
X=np.column_stack((x,x**3))
#3、使用 sm.add_constant() 在 array 上加入一列常项1。
X=sm.add_constant(X) #线性组合，在原始数据前加1
#4、设置模型里的 β0,β1，β2，这里要设置成3、6和2。
beta=np.array([3,6,2])  #β0, β1,β2分别为3、6和2
#5、误差分析，在数据中加上误差项。
e=np.random.normal(size=nsample)
#6、实际值y
y=np.dot(X,beta)+e     #回归公式是: y=3+6x+2x^3+e
#7、最小二乘法
model=sm.OLS(y,X)
#8、拟合数据
res=model.fit()
#9、获取结果，输出图形
#调取计算出的拟合回归模型参数即回归系数
print("回归方程的参数===",res.params)
#调用拟合结果的 fittedvalues 得到拟合的y_pred值
y_pred=res.fittedvalues
#将拟合结果画出来
fig,ax=plt.subplots()
ax.scatter(x,y,label="training data")
ax.plot(x,y_pred,'r',label='predict')
ax.legend()
ax.set(xlabel='x',ylabel='y')
plt.show()
#将回归拟合的摘要全部打印出来
res.summary()
