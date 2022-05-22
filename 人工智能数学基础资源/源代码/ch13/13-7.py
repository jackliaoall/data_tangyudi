#13-7.py

import numpy as np
import scipy.stats as stats  

x = [10.35, 6.24, 3.18, 8.46, 3.21, 7.65, 4.32, 8.66, 9.12, 10.31]  
y = [5.13, 3.15, 1.67, 4.33, 1.76, 4.11, 2.11, 4.88, 4.99, 5.12]  
correlation,pvalue = stats.spearmanr(x,y)  

print ('correlation',correlation)
print ('pvalue',pvalue)
