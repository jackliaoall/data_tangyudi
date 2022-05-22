from scipy.stats import f_oneway
import scipy.stats as stats
import numpy as np
import pandas as pd
cityA = [10,9,9,8,8,7,7,8,8,9]
cityB = [10,8,9,8,7,7,7,8,9,9]
cityC = [9,9,8,8,8,7,6,9,8,9]
df= pd.DataFrame()
names = locals()
for city in ['A','B','C']:
    s=names['city%c'%city]
    df_temp=pd.DataFrame({'city':city[-1], 'S':s})
    df=df.append(df_temp,ignore_index=True)
groups = df.groupby('city')
# The "total sum-square" is the squared deviation from the mean
ss_total = np.sum((df['S']-df['S'].mean())**2)
# 计算SSE和SSA
(ss_treatments, ss_error) = (0, 0)
for val, group in groups:
    ss_error += sum((group['S'] - group['S'].mean())**2)
    ss_treatments += len(group) * (group['S'].mean() - df['S'].mean())**2
df_groups = len(groups)-1
df_residuals = len(df)-len(groups)
F = (ss_treatments/df_groups) / (ss_error/df_residuals)
df = stats.f(df_groups,df_residuals)
p = df.sf(F)
print(('单因素方差分析结果(手动计算）: F = {0}, and p={1}'.format(F, p)))