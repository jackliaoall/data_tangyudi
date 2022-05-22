#1.基本库函数的导入
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

#2.读取数据集，并将数据集的特征和标签分开
df = pd.read_csv("iris.data")
# 原始数据没有给定列名，需要加上
df.columns = ["sepal_len", "sepal_wid", "petal_len", "petal_wid", "class"]
# 把数据分成特征和标签
X = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values
#3.定义降维函数PCA_sklearn()，使用sklearn库实现PCA降维功能，其中需要传递的参数是数据集和降维数。

def PCA_sklearn(data, k):
    '''
    :param data:样本数据
    :param k:目标维度
    :return:降维后的数据data_new
    '''
    pca = PCA(n_components=k)  # 调用PCA函数，先实例化
    pca.fit(data)  # 用数据data来训练PCA模型
    print("降维后的各主成分方差的贡献率：",\
          pca.explained_variance_ratio_)
    print("降维后的各主成分的方差值\n",
          pca.explained_variance_)
    print("降维后的累计贡献率\n", pca.explained_variance_ratio_.sum())
    data_new = pca.transform(data)  # 将数据data转换成降维后的数据
    return data_new


from sklearn.preprocessing import StandardScaler
X= StandardScaler().fit_transform(X)

#4.调用PCA_sklearn()函数


data = PCA_sklearn(X, 2)
 
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

plt.figure(figsize=(6, 4))
for lab, marker, col in zip(("Iris-setosa", "Iris-versicolor", "Iris-virginica"),\
                            ("^", "s", "o"), ("blue", "red", "green")):
    plt.scatter(X[y==lab, 1],
                X[y==lab, 0],
                label=lab,
                marker=marker,
                color=col)
plt.xlabel('X[1]')
plt.ylabel('X[0]')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

