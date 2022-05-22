#方法一：利用逆矩阵可以求解线性方程组
import numpy as np
A = np.array([[1, 1, 1], [1,2,4], [1, 3, 9]])   #系数矩阵
B = np.array([2, 3, 5]).reshape(3,1)            #系数矩阵
A_inv=np.linalg.inv(A)                  #A的逆矩阵
X=A_inv.dot(B)                        #未知数矩阵X
print("A的逆矩阵为：\n",A_inv)
print("利用逆矩阵求出X的值为：\n",X)
C=np.dot(A, X)                  #系数矩阵A与X乘积
print("A和X的乘积C为：\n",C)
#利用allclose检验矩阵是否相等，True代表相等，False代表不等
print("B和C是否相等：",np.allclose(C, B))