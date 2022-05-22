# -*- coding: UTF-8 -*-
#加载相关库函数
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from math import log
import operator

def createDataSet():
	#生成数据集
	dataSet = [[0, 0, 0, 0, 'no'],						
			[0, 0, 0, 1, 'no'],
			[0, 1, 0, 1, 'yes'],
			[0, 1, 1, 0, 'yes'],
			[0, 0, 0, 0, 'no'],
			[1, 0, 0, 0, 'no'],
			[1, 0, 0, 1, 'no'],
			[1, 1, 1, 1, 'yes'],
			[1, 0, 1, 2, 'yes'],
			[1, 0, 1, 2, 'yes'],
			[2, 0, 1, 2, 'yes'],
			[2, 0, 1, 1, 'yes'],
			[2, 1, 0, 1, 'yes'],
			[2, 1, 0, 2, 'yes'],
			[2, 0, 0, 0, 'no']]
	#4个特征
	labels = ['F1-AGE', 'F2-WORK', 'F3-HOME', 'F4-LOAN']		
	return dataSet, labels


def createTree(dataset,labels,featLabels):
	#构建决策树
	#classList:数据集的分类类别
	classList = [example[-1] for example in dataset]
	# 所有样本属于同一类时，停止划分，返回该类别
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	# 所有特征已经遍历完，停止划分，返回样本数最多的类别
	if len(dataset[0]) == 1:
		return majorityCnt(classList)
	# 选择最好的特征进行划分
	bestFeat = chooseBestFeatureToSplit(dataset)
	bestFeatLabel = labels[bestFeat]
	featLabels.append(bestFeatLabel)
	# 以字典形式存储决策树
	myTree = {bestFeatLabel:{}}
	del labels[bestFeat]
	# 根据选择特征，遍历所有值，每个划分子集递归调用createDecideTree
	featValue = [example[bestFeat] for example in dataset]
	uniqueVals = set(featValue)
	for value in uniqueVals:
		sublabels = labels[:]
		myTree[bestFeatLabel][value] = createTree\
			(getDataSet(dataset,bestFeat,value),sublabels,featLabels)
	return myTree


#
#
def majorityCnt(classList):
	#如果决策树递归生成完毕，且叶子节点中样本不是属于同一类
	#则以少数服从多数原则确定该叶子节点类别
	classCount={}
	# 统计每个类别的样本个数
	for vote in classList:
		if vote not in classCount.keys():classCount[vote] = 0
		classCount[vote] += 1
	# iteritems：返回列表迭代器
	# operator.itemgeter(1):获取对象第一个域的值
	# True：降序
	sortedclassCount = sorted(classCount.items(),\
							  key=operator.itemgetter(1),reverse=True)
	return sortedclassCount[0][0]

def chooseBestFeatureToSplit(dataset):
	# 选择最好的特征来划分数据集
	featNum = len(dataset[0]) - 1
	# 计算样本熵值，对应公式中：H(D)
	baseEntropy = calcShannonEnt(dataset)
	bestInfoGain = 0
	bestFeature = -1
	# 以每一个特征进行分类，找出使信息增益最大的特征
	for i in range(featNum):
		#获得该特征的所有取值
		featList = [example[i] for example in dataset]
		#去掉重复值
		uniqueVals = set(featList)
		newEntropy = 0
		# 计算以第i个特征进行分类后的熵值
		for val in uniqueVals:
			subDataSet = getDataSet(dataset,i,val)
			prob = len(subDataSet)/float(len(dataset))
			# 计算满足第i个特征，值为val的数据集的熵，并累加到该特征的熵
			newEntropy += prob * calcShannonEnt(subDataSet)
		# 计算信息增益
		infoGain = baseEntropy - newEntropy
		# 找出最大的熵值以及其对应的特征
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i	
	return bestFeature
			

			
			
		
def getDataSet(dataset,featNum,featvalue):
	#划分数据集，返回第featNum个特征其值为value的样本集合，
	#并且返回的样本数据中已经删除给定特征featNum和值value
	retDataSet = []               #创建新的list对象
	for featVec in dataset:
		if featVec[featNum] == featvalue:
			#从样本中删除第featNum个特征其值为value
			reducedFeatVec = featVec[:featNum]
			reducedFeatVec.extend(featVec[featNum+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet
			
def calcShannonEnt(dataset):
	#计算给定数据集的熵
	numexamples = len(dataset)  # 样本总个数
	labelCounts = {}            # 类别字典，格式{类别：值}
	# 统计每个类别的样本个数，存到字典labelCounts
	for featVec in dataset:
		currentlabel = featVec[-1]
		if currentlabel not in labelCounts.keys():
			labelCounts[currentlabel] = 0
		labelCounts[currentlabel] += 1
	shannonEnt = 0
	# 计算数据集的熵值
	for key in labelCounts:
		prop = float(labelCounts[key])/numexamples
		shannonEnt -= prop*log(prop,2)
	return shannonEnt



def getNumLeafs(myTree):
	numLeafs = 0
	# 获取第一个节点的分类特征
	firstStr = next(iter(myTree))
	# 得到firstFeat特征下的决策树（以字典方式表示）
	secondDict = myTree[firstStr]
	# 遍历firstFeat下的每个节点
	for key in secondDict.keys():
		# 如果节点类型为字典，说明该节点下仍然是一棵树，此时递归调用getNumLeafs
	    if type(secondDict[key]).__name__=='dict':				
	        numLeafs += getNumLeafs(secondDict[key])
		# 否则该节点为叶节点
	    else:   numLeafs +=1
	return numLeafs


def getTreeDepth(myTree):
	maxDepth = 0												
	firstStr = next(iter(myTree))								
	secondDict = myTree[firstStr]								
	for key in secondDict.keys():
	    if type(secondDict[key]).__name__=='dict':				
	        thisDepth = 1 + getTreeDepth(secondDict[key])
	    else:   thisDepth = 1
	    if thisDepth > maxDepth: maxDepth = thisDepth			
	return maxDepth

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
	arrow_args = dict(arrowstyle="<-")											
	font = FontProperties(fname=r"c:\windows\fonts\simsunb.ttf", size=14)		
	createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',	
		xytext=centerPt, textcoords='axes fraction',
		va="center", ha="center", bbox=nodeType, arrowprops=arrow_args, FontProperties=font)


def plotMidText(cntrPt, parentPt, txtString):
	xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]																
	yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
	createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)


def plotTree(myTree, parentPt, nodeTxt):
	decisionNode = dict(boxstyle="sawtooth", fc="0.8")										
	leafNode = dict(boxstyle="round4", fc="0.8")											
	numLeafs = getNumLeafs(myTree)  														
	depth = getTreeDepth(myTree)															
	firstStr = next(iter(myTree))																								
	cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)	
	plotMidText(cntrPt, parentPt, nodeTxt)													
	plotNode(firstStr, cntrPt, parentPt, decisionNode)										
	secondDict = myTree[firstStr]															
	plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD										
	for key in secondDict.keys():								
		if type(secondDict[key]).__name__=='dict':											
			plotTree(secondDict[key],cntrPt,str(key))        								
		else:																														
			plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
			plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
			plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
	plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD


def createPlot(inTree):
	fig = plt.figure(1, facecolor='white')													#创建fig
	fig.clf()																				#清空fig
	axprops = dict(xticks=[], yticks=[])
	createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)    							#去掉x、y轴
	plotTree.totalW = float(getNumLeafs(inTree))											#获取决策树叶结点数目
	plotTree.totalD = float(getTreeDepth(inTree))											#获取决策树层数
	plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;								#x偏移
	plotTree(inTree, (0.5,1.0), '')															#绘制决策树
	plt.show()




if __name__ == '__main__':
	dataset, labels = createDataSet()
	featLabels = []
	#生成决策树
	myTree = createTree(dataset,labels,featLabels)
	#输出结果
	print(myTree)

	# createPlot(myTree)
	
	
	
	
	

	
	






						
