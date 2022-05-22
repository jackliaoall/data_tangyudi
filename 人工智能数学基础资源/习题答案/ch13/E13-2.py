#E13-2.py
import numpy as np
import scipy.stats as stats  

#data source
x = np.array([[1, 4, 2.5, 5, 6, 2.5],
              [2, 3, 1, 5, 6, 4],
             [1.5, 3, 1.5, 4, 5.5, 5.5]])
scoef, pvalue = stats.spearmanr(x, axis=1)    
print(scoef)
print(pvalue)