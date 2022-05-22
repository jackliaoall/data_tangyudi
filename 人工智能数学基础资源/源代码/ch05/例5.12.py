import numpy as np
A=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("A的第1行行向量：\n", A[1,:].reshape(1,-1))
print("A的第2列列向量：\n", A[:,2]. reshape(-1,1))
