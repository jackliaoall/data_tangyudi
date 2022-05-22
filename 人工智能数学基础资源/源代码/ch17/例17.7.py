import numpy as np
# 转移矩阵 matrix
matrix = np.matrix([[0.5,0.3,0.3],[0.2,0.1,0.6],[0.3,0.6,0.1]], dtype=float)
vector1 = np.matrix([[0,1,0]], dtype=float)
for i in range(100):
    vector1 = vector1*matrix # 下一个状态 = 上一个状态 * 转移矩阵
    print ('Current round:',i+1)
    print (vector1)