#1.导入库
import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn import svm
from matplotlib import pyplot as plt
#读取数据集，并将数据集的特征和标签分开
df = pd.read_csv('wine.csv')
# 原始数据没有给定列名的时候需要我们自己加上
#df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
# 把数据分成特征和标签
X = df.iloc[:,1:].values
data=X
y = df.iloc[:,0].values
#2.数据集划分
#该数据集在PCA之前需要对特征进行标准化，保证所有特征在相同尺度下均衡。代码如下：
from sklearn.preprocessing import StandardScaler
X=StandardScaler().fit(X).transform(X)

x_train,x_test,y_train,y_test = train_test_split(X, y,train_size=0.7,\
                                                 random_state=16)
#3.降维
k=2
lda = LDA(n_components=k)#调用LDA函数，先实例化
x_train_lda=lda.fit_transform(x_train,y_train) #在训练集上训练模型并进行降维
x_test_lda = lda.transform(x_test)#将测试集降维

#4.利用降维后的训练集建SVC模型。
clf = svm.SVC()
clf.fit(x_train_lda, y_train)
#5.	对降维后的测试集进行分类，并进行模型评估
y_test_svm = clf.predict(x_test_lda)

print("测试集精确度：\n", metrics.accuracy_score(y_test,y_test_svm))
print(classification_report(y_test,y_test_svm))#输出评估报告
plt.figure(figsize=(6, 4))
for lab, marker,col in zip((1,2,3),
                       ('^', 's', 'o'), ('blue', 'red', 'green')):
     plt.scatter(data[y==lab, 0],
                data[y==lab, 1],
                label=lab,
                 marker=marker,
                 color=col)
plt.xlabel(' principal Component 1')
plt.ylabel(' principal Component 2')
plt.legend(loc='best')
plt.tight_layout()
plt.show()