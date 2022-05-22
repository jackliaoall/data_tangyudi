import numpy as np
B = [[4,2], [1,5]]
A= np.array(B)
eig_val,eig_vex=np.linalg.eig(A)         #eig()函数求解特征值和特征向量
print("A的特征值为：\n",eig_val)
print("A的特征向量为：\n",eig_vex)



sigma=np.diag(eig_val) #特征值的对角化
print("A×eig_vex与eig_vex×sigma是否相等：",
      np.allclose(A.dot(eig_vex),eig_vex.dot(sigma)))
print("A×eig_vex与sigma×eig_vex是否相等：",
      np.allclose(A.dot(eig_vex),sigma.dot(eig_vex)))



