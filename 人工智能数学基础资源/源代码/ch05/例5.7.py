import numpy as np
A =[[1,2], [2,5]]
C1=np.array(A)                 #C1= np.mat(A)结果一样
C2=np. mat(A)
C1_inverse = np.linalg.inv(C1)     #求C1的逆矩阵，不能使用I方法
C2_inverse = C2.I                #求C2的逆矩阵
print("通过inv()求出C1的逆矩阵：\n",C1_inverse)
print("通过I属性求出C2的逆矩阵：\n",C2_inverse)
print("C1与C1的逆相乘的结果：\n",np.dot(C1, C1_inverse))
