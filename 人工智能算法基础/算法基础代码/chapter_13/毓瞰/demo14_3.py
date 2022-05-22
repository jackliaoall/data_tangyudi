def lda(data, target, n_dim):
    '''
    :param data: 样本数据集(样本数为m,特征数为n)
    :param target: 数据类别N
    :param n_dim: 目标维度d
    :return: 降维后的样本数据集(样本数为m,特征数为n)
    '''
    labels = np.unique(target)#样本类别数
    print("样本类别数=\n",labels)
    if n_dim > len(labels)-1:#如果目标维度>样本类别数-1
        print("目标维度太大，请再次输入")
        exit(0)
    #第一步求出类内散度矩阵之和Sw
    Sw = np.zeros((data.shape[1],data.shape[1]))
    
    for i in labels:    #依次求出每类的类内散度矩阵
        datai = data[target == i]
        print("每类的数据：\n", datai)
        print("每类的均值：\n", datai.mean(0))
        datai = datai-datai.mean(0)   #每类样本去均值
        print("每类去均值后的数据：\n", datai)
        Swi = datai.T.dot(datai)      #第i类的类内散度矩阵
        print("每类的类内散度矩阵：\n", Swi)
        Sw += Swi                #所有类的类内散度矩阵之和
    print("类内散度矩阵之和Sw：\n", Sw)
    #第二步求出类间散度矩阵
    Sb = np.zeros((data.shape[1],data.shape[1]))
    u = data.mean(0).reshape(-1,1)    #所有样本的均值转换为列向量格式
    print("所有样本的均值转换为列向量格式\n",u)
    for i in labels:
        Ni = data[target == i].shape[0]  #第i个类别的样本数
        ui = data[target == i].mean(0).reshape(-1,1) #第i个类别的均值
        
        Sbi = Ni*(ui - u).dot((ui - u).T)          #第i类类内散度矩阵
        print("每类的类间散度矩阵：\n", Sbi)
        Sb += Sbi                        #所有类的类间散度矩阵之和
    print("类间散度矩阵之和Sb：\n", Sb)
    #第三步求Sw的逆矩阵和Sb的乘积
    S = np.linalg.inv(Sw).dot(Sb)
    #第四步求特征值，特征向量矩阵
    eigVals,eigVects = np.linalg.eig(S)
    print("特征值=",eigVals)
    print("特征向量\n",eigVects)
    #第五步取目标维度个特征向量
    eigValInd = np.argsort(-eigVals) #将特征值从大到小排序
    eigValInd = eigValInd[:n_dim] # 取前n_dim大的特征值的索引
    redEigVects = eigVects[:,eigValInd]  #取特征值前n_dim大的特征向量矩阵
    print("前n_dim列的特征向量矩阵：\n",redEigVects)
    #第六步求降维后的数据
    data_ndim = data.dot(redEigVects)
    print("降维后的数据：\n", data_ndim)
    return data_ndim


import numpy as np
X=np.array([[0,-1],[0,1],[1,1],[3,2],[1,2]])
Y=np.array([1,2,1,2,2])
lda(X, Y, 1)

