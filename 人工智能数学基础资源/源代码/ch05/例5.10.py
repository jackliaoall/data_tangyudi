import numpy as np
B=[[1, -2, 3], [-1, 2, 1], [-3, -4, -2]]
A=np.array(B)
C= np.linalg.det(A)
print("A的行列式的值：\n",C)
print("C的-1次方：\n",C**(-1))
print("1/C：\n",1/C)
