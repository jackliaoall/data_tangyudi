def pca(data, topk=999999):#利用numpy库实现PCA算法
    '''
    :param data: 样本数据
    :param topk: 目标维度
    :return: 降维后的数据lowDDataMat
    '''
    # 第一步：对样本数据X进行去中心化得到新矩阵X
    meanVals = (np.mean(data, axis=0))#求各个特征的均值
    print("每个特征的均值为：\n",meanVals)
    meanRemoved = data - meanVals #去均值
    print("每个特征去均值后的矩阵：\n",meanRemoved)
    # 第二步：计算去中心化的样本矩阵的协方差矩阵
    #利用numpy的cov()函数求协方差矩阵，
    #设置rowvar=False,此时列为变量计算方式 即X为列，Y也为列
    covmat = np.cov(meanRemoved,rowvar=False)
    print("协方差矩阵：\n", covmat)
    # 第三步：对协方差矩阵C进行特征分解，求出其特征值及对应的特征向量
    eigVals, eigVects = np.linalg.eig(np.mat(covmat))#特征值和特征向量
    # 第四步：将特征向量按对应特征值大从左到右按列排列成矩阵，取前topk列组成矩阵P
    print("特征值：\n", eigVals)
    print("特征向量：\n", eigVects)
    eigValInd = np.argsort(-eigVals)#将特征值从大到小排序
    eigValInd = eigValInd[:topk]  # 取前topk大的特征值的索引
    redEigVects = eigVects[:, eigValInd] #取特征值前topk大的特征向量
    print("前topk列的特征向量矩阵：\n",redEigVects)
    # 第五步：计算降维到k维后的样本特征
    lowDData = meanRemoved.dot(redEigVects) # 降维之后的数据
    print("降维后的数据:\n",lowDData)
    return lowDData

import numpy as np
X=np.array([[0,-1],[0,1],[1,1],[3,2],[1,2]])
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
data = [

        [2.3, 2.7, 5.6],
        [2.0, 1.6, 4.2],
        [1.0, 1.1, 0.7],
        [1.5, 1.6, 8.7],
        [1.1, 0.9, 5.3],
        [2.5, 2.4, 4.3],
        [0.5, 0.7, 2.6],
        [2.2, 2.9, 3.5],
        [1.9, 2.2, 0.5],
        [3.1, 3., 2.1],
    ]

data = np.array(data)
X=data
pca(X,2)


X=np.array([[0,-1],[0,1],[1,1],[3,2],[1,2]])
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
k=2
from sklearn.decomposition import PCA
pca1 = PCA(n_components=k)#调用PCA函数，先实例化
newX = pca1.fit_transform(X)     #等价于pca.fit(X) pca.transform(X)

print(newX)#在数据集data上进行降维。

