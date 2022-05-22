#方法一
import numpy as np
A = np.array([[1, 2, 1], [2,-1,3], [3, 1, 2]])    #系数矩阵A
B = np.array([7, 7, 18]).reshape(3,1)        #常数项矩阵B
A_inv=np.linalg.inv(A)                  #A的逆矩阵
X=A_inv.dot(B)                        #未知数矩阵X
print("A的逆矩阵为：\n",A_inv)
print("利用逆矩阵求出X的值为：\n",X)
C=np.dot(A, X)                  #系数矩阵A与X乘积
print("A和X的乘积C为：\n",C)
#利用allclose检验矩阵是否相等，True代表相等，False代表不等
print("B和C是否相等：",np.allclose(C, B))

#方法二 利用np.linalg.solve()函数求出未知数 ，最后验证 。
import numpy as np
A = np.array([[1, 2, 1], [2,-1,3], [3, 1, 2]])    #系数矩阵A
B = np.array([7, 7, 18]).reshape(3,1)        #常数项矩阵B
X= np.linalg.solve(A, B)                 #未知数矩阵X
print("利用solve()求出X的值为：\n",X)
C=np.dot(A, X)                  #系数矩阵A与X乘积
print("A和X的乘积C为：\n",C)
#利用allclose检验矩阵是否相等，True代表相等，False代表不等
print("B和C是否相等：",np.allclose(C, B))

#方法三
"""
x+2y+z=7
2x-y+3z=7
3x+y+2z=18
"""
#调用sympy库
from sympy import *
x, y, z = symbols("x y z")#三个变量
eq = [x+2*y+z-7,2*x-y+3*z-7,3*x+y+2*z-18]#将三个公式改写为等式为0
result=solve(eq,[x,y,z])
print("结果是：",result)




