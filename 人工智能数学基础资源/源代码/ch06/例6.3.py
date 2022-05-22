import numpy as np
B = [[4,2], [1,5]]
A= np.array(B)
n=3
eig_val,eig_vex=np.linalg.eig(A)   #eig()函数求解特征值和特征向量
sigma=np.diag(eig_val**3)           #特征值的对角化
C=eig_vex.dot(sigma.dot(np.linalg.inv(eig_vex)))
D=A.dot(A.dot(A))
print("C与D是否相同",np.allclose(C,D))
print("A的三次方=\n",A)
