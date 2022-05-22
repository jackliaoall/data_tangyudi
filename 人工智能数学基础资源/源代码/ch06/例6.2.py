import numpy as np
B = [[4,2], [1,5]]
A= np.array(B)
eig_val,eig_vex=np.linalg.eig(A)   #eig()函数求解特征值和特征向量
print("A的特征值为：\n",eig_val)
print("A的特征向量为：\n",eig_vex)
sigma=np.diag(eig_val)           #特征值的对角化
print("特征值矩阵：\n",sigma)
C=eig_vex.dot(sigma.dot(np.linalg.inv(eig_vex)))
print("A与新构造出的矩阵C是否相同",np.allclose(A,C))
