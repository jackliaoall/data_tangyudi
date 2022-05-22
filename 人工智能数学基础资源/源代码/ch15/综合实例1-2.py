from scipy.stats import f_oneway
import scipy.stats as stats
import numpy as np
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
cityA = [10,9,9,8,8,7,7,8,8,9]
cityB = [10,8,9,8,7,7,7,8,9,9]
cityC = [9,9,8,8,8,7,6,9,8,9]
#单因素方差分析
#第二种方法statsmodel库函数
#将数据存入dataframe中
df= pd.DataFrame()
names = locals()
for city in ['A','B','C']:
    s=names['city%c'%city]
    df_temp=pd.DataFrame({'city':city[-1], 'S':s})
    df=df.append(df_temp,ignore_index=True)
#使用线性OLSModel进行方差分析
model = ols('S ~ city', df).fit()
anovaResults = anova_lm(model)
print('单因素方差分析结果（anova_lm）:')
print(anovaResults)