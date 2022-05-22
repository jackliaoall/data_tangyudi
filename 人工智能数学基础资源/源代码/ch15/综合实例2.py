#影响餐饮的2个因素：环境等级，食材等级
from scipy import stats
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
environmental =  [5,5,5,5,5,4,4,4,4,4,3,3,3,3,3,2,2,2,2,2,1,1,1,1,1]
ingredients    = [5,4,3,2,1,5,4,3,2,1,5,4,3,2,1,5,4,3,2,1,5,4,3,2,1]
score      =     [5,5,4,3,2,5,4,4,3,2,4,4,3,3,2,4,3,2,2,2,3,3,3,2,1]
data = {'E':environmental, 'I':ingredients, 'S':score}
df = pd.DataFrame(data)
formula = 'S~E+I'
results = anova_lm(ols(formula,df).fit() )
print(results)
