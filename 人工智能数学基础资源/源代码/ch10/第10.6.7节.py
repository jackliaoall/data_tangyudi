import numpy as np
from sklearn.svm import SVC    #导入SVC模型
#一、导入数据
# 三个测试数据，两个特征值（分别表示横纵坐标），array类型,不能是mat类型
x=np.array([[4,3],[3,3],[1,1]])
y=np.array([1,1,-1]) #写出对应的类别
print("训练集为(最右一列为标签）：\n",np.hstack((x,y.reshape(3,1))))
#二、调用SVC，训练算法
model= SVC(kernel="linear")#实例化，设置的核函数为线性核函数
model.fit(x,y) #用训练集数据训练模型，和上一句配合使用
#三、预测数据
predict_val=model.predict([[4,5],[0,0],[1,3]])
print("预测数据[4,5],[0,0],[1,3]的类型值分别为：",predict_val)
#四、相关方法和返回值
w = model.coef_[0] #获取w
a = -w[0]/w[1] #斜率
print("支持向量：\n",model.support_vectors_)#打印支持向量
print("支持向量的标号：",model.support_)#打印支持向量的标号
print("每类支持向量的个数：",model.n_support_)#每类支持向量的个数
print("数据集X到分类超平面的距离：",model.decision_function(x))
print("参数（法向量）w=",w)
print("分类线的斜率a=",a)
print("分类平面截距b：",model.intercept_)#超平面的截距值（常数值）。
print("系数",model.coef_)#每个特征系数（重要性），只有LinearSVC核函数可用
