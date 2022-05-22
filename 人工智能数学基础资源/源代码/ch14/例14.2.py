import pandas as pd
from io import StringIO
from sklearn import linear_model
import matplotlib.pyplot as plt
# get_data函数：读取数据
def get_data(file_name):
     data = pd.read_csv(file_name)
     X_parameter = []
     Y_parameter = []
     for single_square_feet ,single_price_value in zip(data['output'],data['profit']):
           X_parameter.append([float(single_square_feet)])
           Y_parameter.append(float(single_price_value))
     return X_parameter,Y_parameter
# linear_model_main函数： 利用样本数据训练线性回归模型
def linear_model_main(X_parameters,Y_parameters,predict_value):
 # 创建 linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] =regr.predict(predict_value)
    return predictions
# 函数show_linear_line：显示线性回归结果
def show_linear_line(X_parameters,Y_parameters):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters,Y_parameters,color='blue')
    plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()
X,Y = get_data('sales.csv')
predictvalue = [[200]]  #预测产值200的毛利润
result = linear_model_main(X,Y,predictvalue)
print("Intercept value ",result['intercept'])
print("coefficient" , result['coefficient'])
print("Predicted value: ",result['predicted_value'])
show_linear_line(X,Y)


