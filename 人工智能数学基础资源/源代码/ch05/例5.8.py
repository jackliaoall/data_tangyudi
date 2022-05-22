import numpy as np
A =[[1,-4,0,2],[-1,2,-1,-1],[1,-2,3,5],[2,-6,1,3]]
B=np.array(A)
B_inverse = np.linalg.inv(B)     #求B的逆矩阵
print("B的逆矩阵：\n",B_inverse)