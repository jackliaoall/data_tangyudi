#2. 分别创建一个 阶和 的矩阵，元素值为1~20的随机整数，
#计算这两个矩阵的相加、乘积，求两个矩阵的秩。
import numpy as np
arr1=np.random.randint(1,21,(3,4))
arr2=np.random.randint(1,21,(4,5))
print("arr1=\n",arr1)
print("arr2=\n",arr2)
mult=np.dot(arr1, arr2)
print("arr1的秩为：",np.linalg.matrix_rank(arr1))
print("arr2的秩为：",np.linalg.matrix_rank(arr2))
print("arr1和arr2的乘积：\n",mult)
print("arr1和arr2的和：\n",arr1+arr2)
