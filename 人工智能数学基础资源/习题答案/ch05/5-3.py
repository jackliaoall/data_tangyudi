import numpy as np
A =[[1,2,3],[2,2,1],[3,4,3]]
B=np.array(A)
C=np.linalg.det(B)
print("B的行列式的值：\n",C)
B2=np.mat(A)
C1_inverse = np.linalg.inv(B)     #求C1的逆矩阵，不能使用I方法
C2_inverse = B2.I                #求C2的逆矩阵
print("通过inv()求出B的逆矩阵：\n",C1_inverse)
print("通过I属性求出B2的逆矩阵：\n",C2_inverse)


