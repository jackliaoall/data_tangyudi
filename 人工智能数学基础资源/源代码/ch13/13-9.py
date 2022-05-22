#13-9.py

import numpy as np
import scipy.stats as stats  

x = [90, 84, 76, 71, 71, 71, 69, 68, 66, 64]  
y = [3, 2, 5, 7, 8, 6, 8, 7, 10, 9]
print(x)
print(y)
print()

x = [1,2,3,5,5,5,7,8,9,10]
x=stats.rankdata(x)
y = stats.rankdata(y)
print (x)
print (y)
print()
correlation,pvalue = stats.spearmanr(x,y)  

print ('correlation',correlation)
print ('pvalue',pvalue)
