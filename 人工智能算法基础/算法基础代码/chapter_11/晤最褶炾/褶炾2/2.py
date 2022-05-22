from sklearn import datasets  
import matplotlib.pyplot as plt  
import numpy as np
from sklearn import linear_model
  
#数据集  
diabetes = datasets.load_diabetes() #载入数据  
  
#获取一个特征  
diabetes_x_temp = diabetes.data[:, np.newaxis, 2]   
  
diabetes_x_train = diabetes_x_temp[:-20]   #训练样本  
diabetes_x_test = diabetes_x_temp[-20:]    #测试样本 后20行  
diabetes_y_train = diabetes.target[:-20]   #训练标记  
diabetes_y_test = diabetes.target[-20:]    #预测对比标记  
  
#回归训练及预测  
clf = linear_model.LinearRegression()  
clf.fit(diabetes_x_train, diabetes_y_train)  #注: 训练数据集  
  
#系数 残差平法和 方差得分  
print ('Coefficients :\n', clf.coef_)  
print ("Residual sum of square: %.2f" %np.mean((clf.predict(diabetes_x_test) - diabetes_y_test) ** 2))  
print ("variance score: %.2f" % clf.score(diabetes_x_test, diabetes_y_test))  
  
#绘图  
plt.title(u'LinearRegression Diabetes')   #标题  
plt.xlabel(u'Attributes')                 #x轴坐标  
plt.ylabel(u'Measure of disease')         #y轴坐标  
#点的准确位置  
plt.scatter(diabetes_x_test, diabetes_y_test, color = 'black')  
#预测结果 直线表示  
plt.plot(diabetes_x_test, clf.predict(diabetes_x_test), color='blue', linewidth = 3)  
plt.show()  
