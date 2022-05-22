from numpy import *
a,b=0,3
def f(x): # 例 3.6 的求积函数模型
 return cos(exp(x))**2
def trape(n): # 数值计算 --- 求解定积分的一种算法
 h=(b-a)/n
 x=a
 sum=0
 for i in range(1,n):
    x2=a+i*h
    sum=sum+(f(x)+f(x2))*h/2
    x=x2
 return sum
print(trape(10))
print(trape(100))
print(trape(1000))
print(trape(10000))
print(trape(100000))
