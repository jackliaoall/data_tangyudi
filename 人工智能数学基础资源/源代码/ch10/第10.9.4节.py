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
#为避免数据存在严重的量纲不一致的问题，强烈建议归一化数据，数据标准化的方法很多，本例使用数据预处理中标准化类StandardScaler，对数据进行标准化。
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
#预测结果并进行分析
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

from sklearn.metrics import accuracy_score,precision_score, \
        recall_score,f1_score,cohen_kappa_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
result_show_analyse(wine_test,wine_test_label)#调用结果模块


Kernel = ["linear","poly","rbf"]
for kernel in Kernel:
    model= SVC(kernel = kernel, gamma="auto", cache_size=5000)
    model.fit(wine_train,wine_train_label)
    print("核函数为：",Kernel)
result_show_analyse(wine_test,wine_test_label)


#取不同gamma值得到的准确率
score = []
gamma_range = np.logspace(-10, 1, 50) #得到不同的gamma值即对数刻度上均匀间隔的数
for i in gamma_range:
    model = SVC(kernel="rbf",gamma = i,cache_size=5000)
    model.fit(wine_train,wine_train_label)
    score_gamma=model.score(wine_test,wine_test_label)
    score.append(score_gamma)
print("最大的准确率为：",max(score))
print("对应的gamma值", gamma_range[score.index(max(score))])
plt.xlabel("gamma取值")
plt.ylabel("准确率")
plt.title("gamma的学习曲线")
plt.plot(gamma_range,score)
plt.show()

# 画出多分类的ROC曲线
# 调用相关的库
from itertools import cycle
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from scipy import interp


def plot_roc(test, test_label, test_pred):  # 三个参数，依次为测试样本的数据、标签、预测值
    class_num = sum(unique(test_label))  # 类别数
    Y_pred = test_pred
    # 对输出进行二值化
    # Y_label样例真实标签，Y_pred学习器预测的标签
    Y_label = label_binarize(test_label, classes=[i for i in range(class_num)])
    Y_pred = label_binarize(Y_pred, classes=[i for i in range(class_num)])
    # 计算每一类的ROC
    fpr = dict()  # 假正例率（False Positive Rate , FPR）
    tpr = dict()  # 真正例率（True Positive Rate , TPR）
    roc_auc = dict()  # ROC曲线下方的面积
    for i in range(class_num):
        fpr[i], tpr[i], _ = roc_curve(Y_label[:, i], Y_pred[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    # 计算micro-average ROC 曲线和ROC 面积
    fpr["micro"], tpr["micro"], _ = roc_curve(Y_label.ravel(), Y_pred.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

    # 计算 macro-average ROC 曲线 and ROC 面积
    # 第一步：aggregate all false positive rates
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(class_num)]))
    # 第二步：interpolate all ROC curves at this points
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(class_num):
        mean_tpr += interp(all_fpr, fpr[i], tpr[i])
    # 第三步：Finally average it and compute AUC
    mean_tpr /= class_num
    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
    # 画出具体的某一类的ROC曲线，如第一类
    plt.figure()
    lw = 2
    plt.plot(fpr[1], tpr[2], color="darkorange",
             lw=lw, label="ROC curve (area = %0.2f)" % roc_auc[1])
    plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("假正例率False Positive Rate（FPR）")
    plt.ylabel("真正例率True Positive Rate（TPR）")
    plt.title("Receiver operating characteristic example")
    plt.legend(loc="lower right")
    plt.show()

    # 画出所有类的ROC曲线
    lw = 2
    plt.figure()
    plt.plot(fpr["micro"], tpr["micro"],
             label="micro-average ROC 曲线 (area = {0:0.2f})"
                   "".format(roc_auc["micro"]),
             color="deeppink", linestyle=":", linewidth=4)

    plt.plot(fpr["macro"], tpr["macro"],
             label="macro-average ROC 曲线 (area = {0:0.2f})"
                   "".format(roc_auc["macro"]),
             color="navy", linestyle=":", linewidth=4)
    colors = cycle(["aqua", "darkorange", "cornflowerblue"])
    for i, color in zip(range(class_num), colors):
        plt.plot(fpr[i], tpr[i], color=color, lw=lw,
                 label="ROC curve of class {0} (area = {1:0.2f})"
                       "".format(i, roc_auc[i]))

    plt.plot([0, 1], [0, 1], "k--", lw=lw)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("假正例率False Positive Rate（FPR）")
    plt.ylabel("真正例率True Positive Rate（TPR）")
    plt.title('Some extension of Receiver operating characteristic'
              'to multi-class')
    plt.legend(loc="lower right")
    plt.show()


# 调用画ROC曲线的函数
model = SVC()  # 实例化，设置模型参数
model.fit(wine_train, wine_train_label)
wine_test_pred = model.predict(wine_test)
plot_roc(wine_test, wine_test_label, wine_test_pred)

