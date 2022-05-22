#数据类型 Series 情况下
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series
index = pd.Index([3, 1, 2, 3, 4, np.nan])
#value_counts 直接用来计算series里面相同数据出现的频率
print(index.value_counts())
#当 normalize=True 时返回相同数据出现的频率。
s = pd.Series([3, 1, 2, 3, 4, np.nan])
print(s.value_counts(normalize=True))
#bins 常用于将连续型数据分割成指定数目的半开区间，从而将连续型数据转换成分类变量，bins 指定区间个数。
print(s.value_counts(bins=3))
#当 dropna=False 时，分类统计时考虑加入 NaN，NaN 一般用来标示空缺数据。
s.value_counts(dropna=False)

#数据类型 DataFrame 情况下
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series
df=DataFrame({'a':['Tokyo','Osaka','Nagoya','Osaka','Tokyo','Tokyo'],'b':['Osaka','Osaka','Osaka','Tokyo','Tokyo','Tokyo']})       #DataFrame用来输入两列数据，同时value_counts将每列中相同的数据频率计算出来
print(df)
df.apply(pd.value_counts)


