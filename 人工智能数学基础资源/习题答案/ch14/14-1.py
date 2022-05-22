# 导入相关库
import numpy as np  #numpy库
import pandas as pd  #panda库
#机器学习的工具包machine learning
from sklearn.preprocessing import StandardScaler    #标准化库
from sklearn.model_selection import train_test_split, cross_val_score

# 获取数据
data = pd.read_csv("Folds5x2_pp1.csv")
x = data[['AT', 'V', 'AP', 'RH']]
y = data[['PE']]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
# 设置70%为训练数据

from sklearn.linear_model import LinearRegression

# 建立模型
# 第2步：创建模型：线性回归
model = LinearRegression()
# model = Ridge(alpha=10)
# model = Lasso()
# model = ElasticNet()
# 第3步：训练模型
model.fit(x_train, y_train)
# 获得线性回归模型的参数
a = model.intercept_  # 截距
b = model.coef_  # 回归系数
print("最佳拟合线:截距", a, "\n回归系数：", b)
print(model.coef_[0])

# 对线性回归进行预测
y_pred = model.predict(x_test)
# 评价回归模型
from sklearn.metrics import explained_variance_score, mean_absolute_error, \
    mean_squared_error, median_absolute_error, r2_score

print("电力预测线性模型的平均绝对误差为：", mean_absolute_error(y_test, y_pred))
print("电力预测线性回归模型的均方误差MSE为：", mean_squared_error(y_test, y_pred))
print("电力预测线性回归模型的中值绝对误差为：", median_absolute_error(y_test, y_pred))
print("电力预测线性回归模型的可解释方差值为：", explained_variance_score(y_test, y_pred))
print("电力预测线性回归模型的判定系数即R平方为：", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
