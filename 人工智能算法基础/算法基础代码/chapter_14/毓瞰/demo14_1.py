#1)	导入相关的库
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn import metrics
import xgboost as xgb   #XGBoost原生接口
#2)	数据集的准备
#数据集使用sklearn库datasets模块的make_classification生成一个随机的二分类数据集，进行可视化显示，并将数据划分为训练集和测试集，代码如下：
X, Y = make_classification(n_samples=400, n_features=2, n_redundant=0,\
                             n_clusters_per_class=1, n_classes=2)
for lab, marker,col in zip((0,1), ("^", "s"), ("blue", "red")):
    plt.scatter(X[Y==lab, 0],X[Y==lab, 1],label=lab,marker=marker,
                 color=col)
plt.show()
#划分数据集
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.3,\
                                                random_state=0)

 
#3)	使用原生接口进行训练和预测
#(1)设置参数
params={
    "max_depth":3, 
    "min_child_weight":1,
    "gamma":0.3, 
    "subsample":0.8,
    "colsample_bytree":0.8,
    "booster":"gbtree",
    "objective": "binary:logistic",
    "nthread":12,
    "scale_pos_weight": 1,
    "lambda":1,  
    "seed":28,
    "eval_metric": "auc",
    "eta": 0.3
}
#（2）将数据转换为DMatrix格式
Dtrain = xgb.DMatrix(Xtrain, label=Ytrain)
Dvalid = xgb.DMatrix(Xtest, label=Ytest)
Dtest = xgb.DMatrix(Xtest)
#（3）模型训练
watchlist_xgb = [(Dtrain, "train"), (Dvalid, "valid")]
model_bst = xgb.train(params, Dtrain, 40, evals=watchlist_xgb,\
                      early_stopping_rounds=10, verbose_eval=10)
#verbose_eval=10意思是每10轮打印一次评价指标
print("best_iteration=",model_bst.best_iteration)
print("best_score=",model_bst.best_score)
print("best_ntree_limit=",model_bst.best_ntree_limit)
#（4）预测结果
#预测结果为概率值
Ypred_prod= model_bst.predict(Dtest) 
#将概率值转换为类别值，当概率值大于0.5时，设置类别为1
Ypred= (Ypred_prod >= 0.5)*1 

#4、树模型可视化及特征重要性可视化
#代码如下：
import graphviz
#画出第1棵树的树结构
xgb.plot_tree(model_bst,num_trees=0) 
plt.show()
xgb.plot_tree(model_bst,num_trees=1) 
plt.show()
#将树模型的值转换为dataframe输出。
print(model_bst.trees_to_dataframe())#pima_bst为模型名
#特征重要性可视化
xgb.plot_importance(model_bst) 
plt.show()


 
#5、模型保存与加载
import pickle #导入pickle包
#用dump函数来保存模型，将模型model_bstbst命名成pima.dat。
pickle.dump(model_bst, open("bst.dat", "wb"))
#用load函数来加载数据bst.dat命名为模型 bst_bst。
bst_bst = pickle.load(open("bst.dat", "rb"))
