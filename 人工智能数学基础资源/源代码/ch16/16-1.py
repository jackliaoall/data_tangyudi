#16-1.py

#引入层次聚类函数、还有树状图函数
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
#引入坐标轴显示控制库
from matplotlib.ticker import MultipleLocator
#引入数据操作工具集
import pandas as pd

%matplotlib inline
#读取数据集
seeds_df = pd.read_csv('./datasets/seeds-less-rows.csv')
seeds_df.head()

#去除标识行及类别列
varieties = list(seeds_df.pop('grain_variety'))
samples = seeds_df.values

#进行层次聚类
mergings = linkage(samples, method='complete')

#树状图结果
plt.figure(figsize=(10,6),dpi=80)
ax=plt.subplot(111)
dendrogram(mergings,
           labels=varieties,
           leaf_rotation=90,
           leaf_font_size=10,
)
yminorLocator = MultipleLocator(0.2) 
ax.yaxis.set_minor_locator(yminorLocator)
plt.show()
