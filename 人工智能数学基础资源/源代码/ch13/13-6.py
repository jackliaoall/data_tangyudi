#13-6.py

import numpy as np
import scipy.stats as stats  

x = [0.6,0.7,1,2.1,2.9,3.2,5.5,6.7]
y = np.power(x,10)
correlation,pvalue = stats.pearsonr(x,y) 
print ('correlation',correlation)
print ('pvalue',pvalue)
