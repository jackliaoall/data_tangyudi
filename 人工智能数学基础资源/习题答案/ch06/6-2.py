#准备工作，调入相关的库
import numpy as np
from numpy import linalg as la
import pandas as pd
#第1部分：加载测试数据集，形成loadExData()函数。
#用户-物品矩阵行代表用户user，列代表物品item，其中的值代表用户对物品的打分。该矩阵存放在评分.csv文件中，使用前需要加载。由movie数据集生成该评分.csv的具体实现见6.9节。
#行：代表用户
#列：代表电影
#值：代表用户对电影的评分，0表示未评分
#记载数据集
def loadExData():
    return np.array(pd.read_csv("评分.csv",sep=",",header=None))
#第2部分：计算相似度，形成ecludSim()函数、pearsSim()函数、cosSim()函数。
'''
以下是三种计算相似度的算法，分别是欧式距离、皮尔逊相关系数和余弦相似度
注意三种计算方式的参数X和Y都是采用一维数组。
'''
# 利用欧式距离计算相似度 0~1之间
def ecludSim(X, Y):
    return 1.0 / (1.0 + la.norm(X - Y))  # linalg.norm()是向量A的模(2阶范数)计算方法，
#1/(1+ norm)表示将相似度归一到0与1之间。

# 利用皮尔逊相关系数计算相似度 0~1之间
def pearsSim(X, Y):
    if len(X) < 3: return 1.0
    return 0.5 + 0.5 * np.corrcoef(X, Y, rowvar=1)[0][1]
# corrcoef()表示皮尔逊相关系数的计算方法
#corrcoef() 在 -1 ~ 1之间，0.5 + 0.5*corrcoef()把其取值范围归一化到0到1之间。

#利用余弦相似度计算相似度0~1之间
def cosSim(X, Y):
    XY = float(X.dot(Y))  # 向量 X*Y
    XYnorm= la.norm(X) * la.norm(Y)  #向量A的模(2阶范数) * 向量B的模(2阶范数)
    return 0.5 + 0.5 * (XY / XYnorm)  #向量A 与 向量B 的夹角余弦 A*B / (||A||*||B||)
#范围在-1~1 ，将相似度归一到0与1之间。
#第3部分：对矩阵降维处理，形成svd_item()函数。
#本部分首先确定要选取的奇异值个数，然后进行降维计算矩阵的近似值。
#1.计算选取的奇异值数目k值，形成SigmaPct函数。
'''
按照前k个奇异值的平方和占总奇异值的平方和的百分比percentage确定k的值。
后续计算SVD时需要将item原始矩阵降维
'''
def SigmaPct(sigma, percentage):
    sum_sigma = sum(sigma ** 2)
    sum_sigma1 = sum_sigma * percentage  # 求所有奇异值sigma的平方和的百分比
    sum_sigma2 = 0  # sum_sigma2是前k个奇异值的平方和
    k = 0  # 计数
    for i in sigma:
        sum_sigma2 += i ** 2  # 计算每个奇异值的平方
        k += 1  # 计数增加1
        if sum_sigma2 >= sum_sigma1:  # 判断是否已达到percentage
            return k

#2.降维处理，形成svd_item()函数。
#（1）调用SigmaPct()函数，确定k值。
#（2）利用 ，求出降维后的 。
# 返回降维的物品数据
def svd_item(data, percentage):
    n = np.shape(data)[1]  # 物品种类数据
    U, s, VT = la.svd(data)  # 数据集进行奇异值分解，返回的s为对角线上的值
    k = SigmaPct(s, percentage)  # 确定了k的值,前k个已经包含了percentage的能力
    Sigma = np.eye(k) * s[:k]  # 构建对角矩阵
    # 将数据转换到k维空间(低维)，构建转换后的物品
    FormedItems = data.T.dot(U[:, :k].dot(la.inv(Sigma)))
    return FormedItems  # 返回降维的物品数据

#第4部分：在已经降维的数据中，对用户未打分的一个物品进行评分预测，形成svd_predict()函数。
'''
参数包含：数据矩阵、用户编号、物品编号和奇异值占比的阈值，
数据矩阵的行对应用户，列对应物品
函数的作用：基于item的相似性对用户未评过分的物品进行预测评分
'''
def svd_predict(data, user, simMeas, FormedItems, item, percentage):
    n = np.shape(data)[1]  # 得到数据集中的物品种类数据
    Totalsim = 0.0  # 初始化两个评分值
    TotalratSim = 0.0  # 相似性总和变量初始化
    # 遍历给定的用户行中的每个物品
    # 即（对用户评过分的物品进行遍历，并将它与其他物品进行比较），计算相似度
    for j in range(n):
        # 得到给定的用户user对商品的评分
        Rating_user = data[user, j]
        # 只对评价过的商品和不是自己的商品求相似度
        if Rating_user != 0 and j != item:
            # 计算 svd转换过后矩阵的相似度,物品item与物品j之间的相似度
            # 相似度的计算方法也会作为一个参数传递给该函数
            Similarity = simMeas(FormedItems[item, :], FormedItems[j, :])
            Totalsim += Similarity  # 对相似度不断累加求和
            TotalratSim += Similarity * Rating_user  # 对相似度及对应评分值乘积求和
    if Totalsim == 0:
        return 0
    else:
        return TotalratSim / Totalsim  # 得到对物品的预测评分，返回后用于分数的排序


#第5部分：产生前N个评分值高的物品，返回物品编号以及预测评分值，形成recommend()函数。
'''
函数recommend()产生预测评分最高的N个推荐结果，默认返回5个；
参数包括：数据矩阵、用户编号、相似度衡量的方法、预测评分的方法、以及奇异值占比的阈值。
'''
def recommend(data, user, FormedItems, N, simMeas, percentage):
    # 为未评价的物品建立一个用户未评分item的列表
    unratedItems = np.array(np.nonzero(data[user, :] == 0))[0]
    if len(unratedItems) == 0:
        return "你已评价完所有物品"  # 若都已经评过分，则退出
    Scoresitem = []
    for item in unratedItems:  # 对未评分的物品item，都计算其预测评分
        # 计算评价值
        estimatedScore = svd_predict(data, user, simMeas, FormedItems, item, percentage)
        Scoresitem.append((item, estimatedScore))  # 记录商品及评价值
    Scoresitem = sorted(Scoresitem, key=lambda x: x[1], reverse=True)  # 按照得分逆序排序
    return Scoresitem[:N]  # 返回前N个评分的物品名

#第6部分：对指定用户进行商品推荐，形成recommend_predict函数。
def recommend_predict():
    user_item = loadExData()
    percentage=0.9 #奇异值平方和的百分比
    n=4  #推荐个数
    FormedItems = svd_item(user_item, percentage)# 获得SVD降维后的物品
    print('利用余弦相似度计算距离，进行的奇异值分解推荐：')
    simMeas=cosSim #相似度
    for i in range(0,np.shape(user_item)[0]):
        print("对第",i,"个用户进行推荐：")
        print("按相似度推荐的物品编号为：", recommend(user_item, i, FormedItems, n, simMeas, percentage))
    print('利用欧式距离相似度计算距离，进行的奇异值分解推荐：')
    simMeas = ecludSim
    for i in range(0,np.shape(mymat1)[0]):
        print("对第",i,"个用户进行推荐：")
        print("按相似度推荐的物品编号为：", recommend(user_item, i, FormedItems, n, simMeas, percentage))
    print('利用皮尔逊相似度计算距离，进行的奇异值分解推荐：')
    simMeas= pearsSim
    for i in range(0,np.shape(mymat1)[0]):
        print("对第",i,"个用户进行推荐：")
        print("按相似度推荐的物品编号为：", recommend(user_item, user, FormedItems, n, simMeas, percentage))
#第7部分：调用recommend_predict()函数，获得结果。
#主程序
recommend_predict()
