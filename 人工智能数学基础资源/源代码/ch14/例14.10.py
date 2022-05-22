#调用库
import statsmodels.api as sm #最小二乘
import numpy as np      #numpy库
import matplotlib.pyplot as plt  #导入图形展示库
#利用Statsmodels进行最小二乘法进行线性回归。
#设回归公式是: Y=2+6*x
#1、设定数据量
nsample=20
#2、创建一个表示x的array。这里，设x的值从 0到 30 等差排列，共20个数。
x=np.linspace(0,30, nsample)
#3、使用 sm.add_constant() 在原始数据前加一列常项1。
x=sm.add_constant(x)
#4、设置模型里的 β0,β1，这里要设置成2和6。
beta=np.array([2,6])  #β0, β1分别为2和6
#5、误差分析，在数据中加上误差项，所以生成一个长度为k的正态分布样本。
e=np.random.normal(size=nsample)
#6、产生因变量y的实际值
y=np.dot(x,beta)+e     #回归公式是: Y=2+6*x+ e
#7、创建模型（利用最小二乘法）
model=sm.OLS(y,x)
#8、训练模型
res=model.fit()
#9、获取结果，输出图形
#调取计算出的拟合回归模型参数即回归系数
print("回归方程的参数===",res.params)
#调用拟合结果的 fittedvalues 得到预测值y_pred值
y_pred=res.fittedvalues
#将拟合结果画出来
fig,ax=plt.subplots()
ax.scatter(x[:,-1],y,label="training data")
ax.plot(x[:,-1],y_pred,'r',label='predict')
ax.legend()
ax.set(xlabel='x',ylabel='y')
plt.show()
#将回归拟合的摘要全部打印出来
print(res.summary())
