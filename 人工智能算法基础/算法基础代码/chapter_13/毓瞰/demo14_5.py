#1.	数据集及库函数导入
#首先引入数据，代码如下：
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report
#读取数据集
df = pd.read_csv("iris.data")
# 把数据分成特征和标签
X = df.iloc[:,0:4].values
Y = df.iloc[:,4].values
#将Y的种类转换为整数
y=pd.Categorical(Y).codes
#2.	数据集划分
#利用函数train_test_split将数据集分为训练集占70％，测试集占30%。
#在PCA之前需要对特征进行标准化，保证所有特征在相同尺度下均衡。
from sklearn.preprocessing import StandardScaler
X=StandardScaler().fit_transform(X)
#利用函数train_test_split将数据集分为训练集占70％，测试集占30%。
x_train,x_test,y_train,y_test = train_test_split(X, y,train_size=0.7,\
                                                 random_state=6)

x_t=StandardScaler().fit(x_train)
x_train1=x_t.transform(x_train)
x_test1=x_t.transform(x_test)

                                                 
#3.	对训练集和测试集分别进行PCA降维处理
k=0.98     #设置降维的占比
pca = PCA(n_components=k)#调用PCA函数，先实例化
x_train_pca=pca.fit_transform(x_train) #在训练集上拟合模型并进行降维
x_test_pca = pca.transform(x_test)#将测试集降维
print("主成分的数量：",pca.n_components_)

pca1 = PCA(n_components=k)#调用PCA函数，先实例化

x_train_pca1=pca.fit_transform(x_train1) #在训练集上拟合模型并进行降维
x_test_pca1 = pca.transform(x_test1)#将测试集降维
print("主成分的数量：",pca.n_components_)


#4.	利用降维后的训练集建立逻辑回归模型。
model =LogisticRegression()
model.fit(x_train_pca, y_train)
#5.	对降维后的测试集进行分类，并进行模型评估
y_test_pca = model.predict(x_test_pca)
print("测试集分类准确率：\n", metrics.accuracy_score(y_test,y_test_pca))
print(classification_report(y_test,y_test_pca))#输出评估报告

model1 =LogisticRegression()
model1.fit(x_train_pca1, y_train)
#5.	对降维后的测试集进行分类，并进行模型评估
y_test_pca1 = model1.predict(x_test_pca1)
print("测试集精确度：\n", metrics.accuracy_score(y_test,y_test_pca1))
print(classification_report(y_test,y_test_pca1))#输出评估报告
