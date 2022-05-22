#分别创建一个四阶零矩阵和四阶单位矩阵，以及对角线元素分别为1,2,3,4的对角矩阵。
import numpy as np
A=np.zeros((4,4))
print("通过zeros函数创建的四阶零矩阵A：\n",A)
E1= np.eye(4)
E2= np.identity(4)
print("通过eye()创建的四阶单位矩阵E1为：\n",E1)
print("通过identity ()创建的四阶单位矩阵E2为：\n",E2)
b=[1,2,3,4]  #对角线元素
arr1=np.diag(b)  #使用diag()创建对角矩阵
print("创建主对角线为1,2,3,4的对角矩阵arr1为：\n",arr1)
arr2=np.diag(arr1)
print("获取矩阵arr1的对角线元素：\n",arr2)
print("arr2的类型",arr2.shape)

