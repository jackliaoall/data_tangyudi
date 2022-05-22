#方法二. numpy提供了np.linalg.solve()函数解线性方程组。
import numpy as np
A = np.array([[1, 1, 1], [1,2,4], [1, 3, 9]])   #系数矩阵
B = np.array([2, 3, 5]).reshape(3,1)            #系数矩阵
X= np.linalg.solve(A, B)                 #未知数矩阵X
print("利用solve()求出X的值为：\n",X)
C=np.dot(A, X)                  #系数矩阵A与X乘积
print("A和X的乘积C为：\n",C)
#利用allclose检验矩阵是否相等，True代表相等，False代表不等
print("B和C是否相等：",np.allclose(C, B))



