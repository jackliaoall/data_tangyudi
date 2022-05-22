#1.基本库函数的导入
import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from matplotlib import pyplot as plt

#2.读取数据集，并将数据集的特征和标签分开
df = pd.read_csv("iris.data")
# 原始数据没有给定列名，需要加上
df.columns = ["sepal_len", "sepal_wid", "petal_len", "petal_wid", "class"]
# 把数据分成特征和标签
X = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values
#3.定义降维函数PCA_sklearn()，使用sklearn库实现PCA降维功能，其中需要传递的参数是数据集和降维数。

def LDA_sklearn(X,Y,k):
    '''
    :param data:样本数据
    :param k:目标维度
    :return:降维后的数据data_new
    '''
    lda = LDA(n_components=k)#调用LDA函数，先实例化
    lda.fit(X,Y)#用数据X和Y来训练LDA模型
    data_new = lda.transform(X)
    print("截距: ", lda.intercept_)#输出截距
    print("权重向量: \n", lda.coef_)   #输出权重向量
    print("各维度的方差值占总方差值的比例: ",
          lda.explained_variance_ratio_)
    print("各维度的方差值之和占总方差值的比例: ",
          lda.explained_variance_ratio_.sum())
    return data_new          #返回降维后的数据


#4.调用PCA_sklearn()函数
from sklearn.preprocessing import StandardScaler
X=StandardScaler().fit_transform(X)

data = LDA_sklearn(X,y, 2)

#5.降维后的结果可视化
plt.figure(figsize=(6, 4))
for lab, marker, col in zip(("Iris-setosa", "Iris-versicolor", "Iris-virginica"),
                            ("^", "s", "o"), ("blue", "red", "green")):
    plt.scatter(data[y == lab, 0],
                data[y == lab, 1],
                label=lab,
                marker=marker,
                color=col)
plt.xlabel("principal Component 1")
plt.ylabel("principal Component 2")
plt.legend(loc="best")
plt.tight_layout()
plt.show()
