#16-2.py

#引入pandas数据工具集
import pandas as pd
#引入机器学习库中的归一化函数
from sklearn.preprocessing import normalize
#引入层次聚类函数、还有树状图函数
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
#引入坐标轴显示控制库
from matplotlib.ticker import MultipleLocator

%matplotlib inline

scores_df = pd.read_csv('./datasets/eurovision-2016-televoting.csv', index_col=0)
country_names = list(scores_df.index)
scores_df.head()

#缺失值填充，没有的就先按满分算吧
scores_df = scores_df.fillna(12)

#归一化
samples = normalize(scores_df.values)

plt.figure(figsize=(10,12),dpi=80)
plt.subplots_adjust(hspace=0.5)

#single method distance clustering
mergings = linkage(samples, method='single')
p1=plt.subplot(211)
yminorLocator = MultipleLocator(0.05) 
p1.yaxis.set_minor_locator(yminorLocator)
dendrogram(mergings,
           labels=country_names,
           leaf_rotation=90,
           leaf_font_size=10,
)
p1.set_title("single-min distance",fontsize=18)

#complete method distance clustering
mergings = linkage(samples, method='complete')
p2=plt.subplot(212)
yminorLocator = MultipleLocator(0.05) 
p2.yaxis.set_minor_locator(yminorLocator)
dendrogram(mergings,
           labels=country_names,
           leaf_rotation=90,
           leaf_font_size=10,
)
p2.set_title("complete-max distance",fontsize=18)

plt.show()