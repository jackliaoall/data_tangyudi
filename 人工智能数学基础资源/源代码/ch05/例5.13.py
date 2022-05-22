import numpy as np
A=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("A的各行向量：")
for i in range(np.shape(A)[0]):
    print("第 ",i,"行：",A[i,:].reshape(1,-1))
print("A的各列向量：")
for i in range(np.shape(A)[1]):
    print("第 ",i,"列\n",A[:,i].reshape(-1,1))
