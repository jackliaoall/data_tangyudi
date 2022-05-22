#E13-1.py
import numpy as np
import scipy.stats as stats  

#data source
x = np.array([[1, 4, 2.5, 5, 6, 2.5],
              [2, 3, 1, 5, 6, 4],
             [1.5, 3, 1.5, 4, 5.5, 5.5]])
i = 0
while i < 3:
    pcoef, pvalue = stats.pearsonr(x[i], x[(i + 1) % 3])    
    print(pcoef, pvalue)
    i += 1