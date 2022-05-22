import numpy as np
#一、读取文件
#获取的已经是矩阵，所以不用再转化
data=np.loadtxt("iris.csv",delimiter=",",dtype=np.str,skiprows=1)
#二、获取数据和标签
X_data= data[:,:-1].astype('float')
Y_data=data[:,-1]
print("数据集中的样本数为%d，列数为%d"%(data.shape[0],data.shape[1]))
#使用numpy获取数据集的第0个样本
data_0= X_data[0]
print("数据集的第0个样本\n",data_0)
print("数据集的属性值类型：",type(X_data[1,0]))
print("数据集的类型标签值类型：",type(Y_data[1]))