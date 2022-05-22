import numpy as np
import random
import pandas as pd
columnsName=['buying', 'maint', 'doors', 'persons','lug-boot','safety','label']
#从数据集中获得数据
def getDataSet(file):
    fr = open(file)
    rdata = []
    for line in fr.readlines():
        tmp = line.strip().split(',')
        rdata.append(tmp)
    df = pd.DataFrame(rdata)  #读入数据到DATAFrame变量df，类似二维表
    df.columns =columnsName   #设置df的列名
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
#定义朴素贝叶斯模型
class NBClassify(object):
    def __init__(self):
        #tabProbablity核心字典，记录各类别的先验概率，格式：{'unacc':概率值, 'acc': 概率值, 'vgood': 概率值, 'good': 概率值}
        _tagProbablity=None
        #featuresProbablity核心字典，记录各类别下各特征取值的条件概率。三级字典，
        #格式：类别1: {'特征1': {'值1': 概率值, ...'值n': 概率值}, '特征2':{}...},类别2：{'特征1': {'值1': 概率值, ...'值n': 概率值},
        _featuresProbablity=None

    def train(self,df):
        # 计算每种类别的先验概率
        self._tagProbablity=df['label'].value_counts(value for value in df['label'])
        print("各类别的先验概率：\n",self._tagProbablity)

        # 计算各特征及对应取值的出现次数dictFeaturesBase
        #格式：  {特征1:{值1:出现5次, 值2:出现1次}, 特征2:{值1:出现1次, 值2:出现5次}}
        dictFeaturesBase={}.fromkeys(df.columns)
        for column in df.columns:
             seriesFeature = df[column].value_counts()
             dictFeaturesBase[column] =seriesFeature
        #从特征值字典删去类别信息
        del dictFeaturesBase['label']

        # 初始化字典 dictFeatures
        #格式：{类别1:{'特征1':{'值1':None,...'值n':None},'特征2':{...}},类别2：{'特征1':{'值1':None, ...},...}
        dictFeatures = {}.fromkeys(df['label'])
        for key in dictFeatures.keys():
            dictFeatures[key] = {}.fromkeys([key for key in dictFeaturesBase])
        for key, value in dictFeatures.items():
            for subkey in value.keys():
                value[subkey] = {}.fromkeys([x for x in dictFeaturesBase[subkey].keys()])

        # 计算各类别、对应特征及对应取值的出现次数，存入字典dictFeatures
        for i in range(0, len(df)):
            label=df.iloc[i]['label']    #类别
            for feature in columnsName[0:6]:   #对应的特征
                fvalue=df.iloc[i][feature]  #对应的特征取值
                if dictFeatures[label][feature][fvalue] == None:
                    dictFeatures[label][feature][fvalue] = 1 #该类别下该特征值第一个出现的样本
                else:
                    dictFeatures[label][feature][fvalue] +=1  #如果已有，次数加一


        # 该类数据集若未涵盖此特征值时，加入Laplace平滑项
        for tag, featuresDict in dictFeatures.items():
            for featureName, featureValueDict in featuresDict.items():
                for featureKey, featureValues in featureValueDict.items():
                    if featureValues == None:
                        featureValueDict[featureKey] = 1

        # 由字典dictFeatures计算每个类别下每种特征对应值的概率，即特征的似然概率P(feature|tag)
        for tag, featuresDict in dictFeatures.items():
            for featureName, featureValueDict in featuresDict.items():
                totalCount = sum([x for x in featureValueDict.values() if x != None])
                for featureKey, featureValues in featureValueDict.items():
                    featureValueDict[featureKey] = featureValues / totalCount
        self._featuresProbablity = dictFeatures
        print("每个类别下每种特征对应值的似然概率:\n",dictFeatures)

    # 对测试集进行预测
    def classify(self, featureTuple):
        resultDict = {}
        # 计算样本属于每个类别的后验概率
        for tag, featuresDict in self._featuresProbablity.items():
            iNumList = []
            i=0
            #将各特征值对应的似然概率添加到列表iNumList
            for feature,featureValueDict in featuresDict.items():
                featureValue=str(featureTuple[i])
                iNumList.append(self._featuresProbablity[tag][feature][featureValue])
                i=i+1
            #列表iNumList中的概率相乘，得到似然概率
            conditionProbability = 1
            for iNum in iNumList:
                conditionProbability *= iNum
            #将先验概率乘以似然概率得到后验概率resultDict
            resultDict[tag] = self._tagProbablity[tag] * conditionProbability
        # 对比每个类别的后验概率resultDict的大小
        resultList = sorted(resultDict.items(), key=lambda x: x[1], reverse=True)
        #返回最大后验概率的类别
        return resultList[0][0]
if __name__ == '__main__':
    dfData=getDataSet('data/car.txt')
    # 避免过拟合，采用交叉验证，随机选取1500个数据作为测试集，剩余为训练集
    trainData, testData = getTrainTest(dfData, 1500)
    #定义朴素贝叶斯模型
    model = NBClassify()
    #代入训练数据集，进行模型训练
    model.train(trainData)
    #对测试数据集进行预测，并计算错误率
    errorCount = 0
    for i in range(0, len(testData)):
        result = model.classify(testData.iloc[i][0:6])
        # 将预测的类别和实际值比较
        if testData.iloc[i][6]!=result: errorCount += 1
    print("The error rate is %f" %(float(errorCount) / len(testData)))
