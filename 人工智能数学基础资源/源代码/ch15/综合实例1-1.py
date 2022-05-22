# 3个城市不同用户评分
from scipy.stats import f_oneway
import scipy.stats as stats
import numpy as np
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
cityA = [10,9,9,8,8,7,7,8,8,9]
cityB = [10,8,9,8,7,7,7,8,9,9]
cityC = [9,9,8,8,8,7,6,9,8,9]
# 首先检查方差是否相等
(W,p) = stats.levene(cityA,cityB,cityC)
if p<0.05:
    print(('Warning: the p-value of the Levene test is <0.05: p={0}'.format(p)))
#单因素方差分析
#第一种方法
F_statistic, pVal = stats.f_oneway(cityA,cityB,cityC)
print('单因素方差分析结果（f_oneway）: F = {0}, and p={1}'.format(F_statistic, pVal))
if pVal < 0.05:
    print('One of the groups is significantly different.')

