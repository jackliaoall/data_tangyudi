import pandas as pd
import numpy as np
import random
from sklearn.naive_bayes import BernoulliNB
columnsName=['buying', 'maint', 'doors', 'persons','lug-boot','safety','label']
#从数据集中获得数据，并进行整理
def getDataSet(file):
    fr = open(file)
    rdata = []
    for line in fr.readlines():
        tmp = line.strip().split(',')
        rdata.append(tmp)
    df = pd.DataFrame(rdata)
    df.columns = columnsName
    #feature_codes记录特征及数据标签的编码表，如：'buying'特征的取值及对应的编码：'vhigh': 0, 'high': 1, 'med': 2, 'low': 3
    feature_codes = [{'vhigh': 0, 'high': 1, 'med': 2, 'low': 3},
            {'vhigh': 0, 'high': 1, 'med': 2, 'low': 3},
            {'2': 0, '3': 1, '4': 2, '5more': 3},
            {'2': 0, '4': 1, 'more': 2},
            {'small': 0, 'med': 1, 'big': 2},
            {'high': 0, 'med': 1, 'low': 2},
            {'unacc':0,'acc': 1,'good': 2,'vgood':3} ]
    for i in range(0,7):
        df.iloc[:, i]=df.iloc[:,i].map(feature_codes[i])
    # Xtrain, Xtest, Ytrain, Ytest = train_test_split(df.iloc[:, 1:6], df.iloc[:, 7], test_size=0.17, random_state=420)
    return df
#随机抽取数据,将数据集分成训练集和测试集
def getTrainTest(data, trainNum):
    # 从0到len（data）整数列表中随机截取trainNum个片段
    choose = random.sample(range(len(data)), trainNum)
    choose.sort()
    j = 1
    dftrain = pd.DataFrame(columns= columnsName)
    dftest =pd.DataFrame(columns= columnsName)
    for i in range(1,len(data)):
        # 如果被随机选中，加入训练集，否则测试集
        if (j < trainNum and i == choose[j]):
            dftrain.loc[dftrain.shape[0]]=data.iloc[i]
            j += 1
        else:
            dftest.loc[dftrain.shape[0]]=data.iloc[i]
    return dftrain, dftest

if __name__ == '__main__':
    dfData=getDataSet('data/car.txt')
    #
    #设置训练数据集
    trainData, testData = getTrainTest(dfData, 1500)
    train_X =trainData.iloc[:,:-1]
    train_Y =np.asarray(trainData.iloc[:,-1],dtype="|S6")
    test_X = testData.iloc[:,:-1]
    test_Y = np.asarray(testData.iloc[:,-1],dtype="|S6")

    clf=BernoulliNB()
    clf.fit(train_X,train_Y)#训练
    predicted = clf.predict(test_X)
    print('精度为：%f ' %np.mean(predicted == test_Y))