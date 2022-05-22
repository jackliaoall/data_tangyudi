#调用相关的库：
import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles#画圆圈的库
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
#画分类数据集
def plot_decision_boundary (model,X,y,h=0.03,draw_SV=True,title='decision_boundary'):
    X_min, X_max = X[:,0].min()- 1, X[:,0].max() + 1
    y_min, y_max = X[:,1].min() - 1,X[:, 1].max() + 1
    # 画决策边界，需要有网格，利用np.meshgrid()生成一个坐标矩阵
    xx, yy = np.meshgrid(np.arange(X_min, X_max, h),np.arange(y_min, y_max, h))
#预测坐标矩阵中每个点所属的类别
    label_predict = model.predict(np.stack((xx.flat, yy.flat), axis=1))       
    # 将结果放入彩色图中
    label_predict = label_predict.reshape(xx.shape)   # 使之与输入的形状相同
    plt.title(title)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.contourf(xx, yy, label_predict, alpha=0.5)#用contourf()函数为坐标矩阵中不同类别填充不同颜色    
    markers = ['x', '^', 'o']
    colors = ['b', 'r', 'c']
    classes = np.unique(y)
    #画出每一类数据的散点图
    for label in classes:
        plt.scatter(X[y==label][:, 0], X[y==label][:, 1], 
                    c=colors[label], s=60,marker=markers[label])
    #标记出支持向量，将两类支持向量机用不同颜色表示出来
    if draw_SV:
        SV = model.support_vectors_         #获取支持向量
        n=model.n_support_[0]              #第一类支持向量个数
        plt.scatter(SV[:n, 0],SV[:n, 1], s=15,c='black',marker='o')
        plt.scatter(SV[n:, 0],SV[n:, 1], s=15,c='g',marker='o')
#一、生成模拟分类数据集，并画出数据集
X, y = make_circles(200,factor=0.1,noise=0.1)#产生样本点
plt.scatter(X[y==0, 0], X[y==0, 1], c='b', s=20, marker = 'x')
plt.scatter(X[y==1, 0], X[y==1, 1], c='r', s=20, marker = '^')
plt.xticks(())
plt.yticks(())
plt.title('数据集')
plt.show()          #画出数据集
#分别利用线性核函数和多项式核函数进行分类，并画出的决策边界
plt.figure(figsize=(12,10),dpi=200)
#使用线性核函数进行分类
model_linear = SVC(C=1.0, kernel='linear')#实例化，设置的核函数为线性核函数
model_linear.fit(X,y)#用训练集数据训练模型，和上一句配合使用
#画出使用线性核函数的分类边界
plt.subplot(2,2,1)
plot_decision_boundary(model_linear, X, y,title='线性核函数')#调用画图函数
print("采用线性核函数生成的支持向量个数：",model_linear.n_support_)
#使用多项式核函数进行分类
model_poly = SVC(C=1.0, kernel='poly', degree=3,gamma="auto")#实例化，设置的核函数为多项式核函数
model_poly.fit(X,y)#用训练集数据训练模型
#画出使用多项式核函数的分类边界
plt.subplot(2,2,2)
plot_decision_boundary(model_poly, X, y,title='多项式核函数')#调用画图函数
print("采用多项式函数生成的支持向量个数：",model_poly.n_support_)
plt.show()
plt.figure(figsize=(12,10),dpi=200)
for j, gamma in enumerate((10,1,0.1, 0.01)):
    plt.subplot(2,2,j+1)
    model_rtf= SVC(C=1.0, kernel='rbf', gamma=gamma)
    model_rtf.fit(X,y)#高斯核函数
    #调用画图函数
    plot_decision_boundary(model_rtf, X, y, title='rbf函数，'
                                                  '参数gamma='+str(gamma))
    print("rbf函数，参数gamma=",str(gamma),"支持向量个数：",model_rtf.n_support_)
plt.show()


from sklearn.model_selection import GridSearchCV
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1,0.1,0.01],'C': [0.1, 1,10]},
                 {'kernel': ['linear'], 'C': [0.1, 1,10]},
                 {'kernel': ['poly'],'gamma': [1,0.1,0.01],
                  'C': [0.1, 1,10]}]
model_grid = GridSearchCV(SVC(), tuned_parameters, cv=5)
model_grid.fit(X, y)
print("The best parameters are %s with a score of %0.2f"
      % (model_grid.best_params_, model_grid.best_score_))

