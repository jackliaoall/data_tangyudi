import numpy as np
#线性核函数
def linear(X, Y):
    K= X.T.dot(Y)
    return K
#RBF
def gaussian (X,Y, sigma):#x和y为数据，sigma为参数
    K= np.exp(-np.linalg.norm(X-Y)**2 / (2 * sigma**2))
    return K
#多项式核函数
def poly(X, Y, gamma,c,degree): #通过数据计算转换后的核函数
    K = X.T.dot(Y)
    K= (gamma*K + c)**degree
    return K
