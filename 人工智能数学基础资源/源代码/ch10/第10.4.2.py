import numpy as np
#映射函数
def f(Z):
    Z1=Z**2
    Z_shape=np.shape(Z)[1]-1
    Z0=[]
    for i in range(Z_shape,0,-1):
        for j in range(i-1,-1,-1):
            xy=Z[0,i]*Z[0,j]*2**0.5
            Z0.append(xy)
    Z2=np.array(Z0).reshape(1,-1)
    Z3=Z*2**0.5
    return np.hstack((Z1,Z2,Z3,[[1]]))
X=np.array([[1,2,3,4]])     #4维行向量
Y=np.array([[5,6,7,8]])
#使用多项式核函数计算
XY_poly = (X.dot(Y.T)+1)**2
print("使用多项式核函数计算的结果为：",XY_poly)
#使用映射的计算
X1=f(X)
Y1=f(Y)
print("使用映射计算的结果为：",X1.dot(Y1.T))
print("输出X的映射值为：\n",X1)
print("输出Y的映射值为：\n",Y1)
print("原输入空间的维度为：",np.shape(X)[1])
print("映射后特征空间的维度为：",np.shape(X1)[1])
