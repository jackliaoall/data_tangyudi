#创建一个四阶方阵，元素值为1~20的随机浮点数，
# 根据其上三角和下三角矩阵，分别创建对应的对称矩阵。
import numpy as np
arr=np.random.uniform(1,21,(4,4))
upper_A=np.triu(arr,0)#上三角矩阵
low_A=np.tril(arr,0)#下三角矩阵
print("arr矩阵：\n",arr)
print("A的上三角矩阵：\n",upper_A)
print("A的下三角矩阵：\n",low_A)
#生成上三角矩阵的对称矩阵
upper_A += upper_A.T - np.diag(np.diag(upper_A))#将上三角”拷贝”到下三角部分
print("生成的对称矩阵arr2：\n",upper_A)
#生成下三角矩阵的对称矩阵
low_A += low_A.T - np.diag(np.diag(low_A))#将上三角”拷贝”到下三角部分
print("生成的对称矩阵arr2：\n",low_A)


