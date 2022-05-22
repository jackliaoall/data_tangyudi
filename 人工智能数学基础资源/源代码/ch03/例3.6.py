import numpy as np 
from scipy.integrate import quad
func=lambda x:np.cos(np.exp(x))**2 # 定义被积分函数
solution=quad(func,0,3) # 调用 quad 积分函数
print(solution)
