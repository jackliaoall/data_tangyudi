import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
df=pd.read_csv('data.csv')
print(df)
formula = 'weight ~ group+nutrient'
results = anova_lm(ols(formula,df).fit() )
print (results)