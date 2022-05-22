import numpy as np
from sklearn import svm
from sklearn.svm import SVC#导入SVM模型
from sklearn.model_selection import train_test_split   #导入测试库
from sklearn.datasets import load_wine             #导入wine数据集
from time import time
#（1）导入数据集
wine = load_wine()
wine_data = wine.data
wine_label = wine.target
#（2）数据预处理
# 数据标准化
from sklearn.preprocessing import StandardScaler
wine_data=StandardScaler().fit_transform(wine_data) #对数据进行标准化
#（3）分离数据
#将数据划分为训练集和测试集，训练集占80%，用于得到训练模型，测试集占20%，用于检验模型。
wine_train,wine_test,wine_train_label,wine_test_label = \
train_test_split(wine_data,wine_label,test_size = 0.2,random_state = 100)
#（4）以默认的SVM参数，训练数据集的训练，产生训练模型。
# 建立SVM模型，以默认的rbf为例
time0 = time()     #模型训练开始时间
model= SVC()#实例化，设置模型参数
model.fit(wine_train,wine_train_label) #用训练集数据训练模型
print("建立的SVM模型为：\n",model)
time1=time()  #模型训练结束时间
#（5）结果及分析
def result_show_analyse(test,test_label):
    from datetime import datetime
    #1、预测结果
    print("---------测试集的结果--------")
    test_pred = model.predict(test)
    print("测试集的真实结果为：\n",test_label)
    print("测试集的预测结果为：\n",test_pred)
    # 求出预测和真实一样的数目
    true = np.sum(test_pred == test_label)
    print("预测对的结果数目为：", true)
    print("预测错的结果数目为：", test_label.shape[0]-true)
    print("训练时间：",datetime.fromtimestamp(time1-time0).strftime("%M:%S:%f"))
    #2、结果分析，给出准确率、精确率、召回率、F1值、Cohen’s Kappa系数
    print("---------测试集的结果分析--------")
    print("使用SVM预测wine数据的准确率是：%f"
              %(accuracy_score(test_label,test_pred)))
    print("使用SVM预测wine数据的精确率是：%f"
              %(precision_score(test_label,test_pred,average="macro")))
        #对多分类要加average="macro"
    print("使用SVM预测wine数据的召回率是：%f"
              %(recall_score(test_label,test_pred,average="macro")))
    print("使用SVM预测wine数据的F1值是：%f"
              %(f1_score(test_label,test_pred,average="macro")))
    print("使用SVM预测wine数据的Cohen’s Kappa系数是：%f"
              %(cohen_kappa_score(test_label,test_pred)))
    print("使用SVM预测wine数据的分类报告为：\n",
              classification_report(test_label,test_pred))
    #3、画出预测结果和真实结果对比的图
    print("---------测试集的结果图--------")
    plt.plot(test_pred,'bo',label="预测")
    plt.plot(test_label,'r*',label="真实")
    plt.xlabel(r'测试集样本',color='r',fontsize=18)
    plt.ylabel(r'类别标签',color='r',fontsize=18,rotation=360)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title('测试集的实际分类和预测分类图',fontsize=18)
    plt.show()

#调用结果函数
#调用相关库
from sklearn.metrics import accuracy_score,precision_score, \
        recall_score,f1_score,cohen_kappa_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
#图表中显示中文
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
result_show_analyse(wine_test,wine_test_label)#调用结果模块

#（6）分类结果的混淆矩阵及图表显示
from sklearn import metrics
def cm_plot(y,yp):
    conf_mx = metrics.confusion_matrix(y, yp) # 模型对于测试集的混淆矩阵
    print("测试集的混淆矩阵：\n",conf_mx)
    plt.matshow(conf_mx,cmap=plt.cm.Greens)
    # 画混淆矩阵图，配色风格使用cm.Greens
    plt.colorbar()# 颜色标签
    for x in range(len(conf_mx)):
        for y in range(len(conf_mx)):
            plt.annotate(conf_mx[x,y],xy=(x,y),horizontalalignment='center',
                         verticalalignment='center')
            plt.ylabel('True label')# 坐标轴标签
            plt.xlabel('Predicted label')# 坐标轴标签
    return plt
    #函数调用
wine_test_pred=model.predict(wine_test)
cm_plot(wine_test_label, wine_test_pred).show()
