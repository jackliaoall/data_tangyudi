import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.stats.anova as anova
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

def startup():
    datas = pd.read_csv('salary.csv', encoding='gbk')
    model = ols('Salary ~ C(Male)+C(Experience)', data=datas.dropna()).fit()
    rst = anova.anova_lm(model)
    print(rst)
startup()