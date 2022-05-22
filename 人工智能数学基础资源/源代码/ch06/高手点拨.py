import numpy as np
import pandas as pd
#1、读入数据集
header = ["user_id","item_id","rating","timestamp"]
data =pd.read_csv("u.data", sep="\t", names=header)
#2、生成用户—物品评分矩阵
#检查是否有重复的用户物品打分记录
data.duplicated(subset = ["user_id","item_id"]).sum()
item_id_user = data.groupby("item_id").count()["user_id"]
#构建用户物品矩阵
users_num = data.user_id.max()
items_num = data.item_id.max()
user_item_rating = np.zeros((users_num,items_num))
for line in data.itertuples():                         #以元组的方式赋值
    user_item_rating[line[1]-1,line[2]-1] = line[3]
np.savetxt("评分12.csv", user_item_rating, delimiter = ",")
#输出u.data中的前5行内容
data.head()
#输出u.data中的大小
print("数据集的大小",data.shape)
#输出客户数和电影数
print("客户数=",users_num)
print("电影数=",items_num)
#查看生成的user_item_rating非零元素
print("user_item_rating中的非零元素",user_item_rating.nonzero()[1])
#查看生成的user_item_rating矩阵的稀疏性
sparsity = round(len(user_item_rating.nonzero()[1])/float(users_num*items_num),3)
print("user_item_rating矩阵的稀疏性：", sparsity)
print("user_item_rating矩阵的大小",user_item_rating.shape )
#以表格形式显示用户—电影评分表矩阵
pd.DataFrame(user_item_rating)
