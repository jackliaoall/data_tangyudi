#13-4.py

import numpy as np
import scipy.stats as stats
tang = np.array([[74, 71, 72, 68, 76,73,67,70,65,74],  
       [76, 75, 71, 70, 76, 79, 65, 77, 62, 72]])
print(tang[0])
print(tang[1])
cor,pv=stats.pearsonr(tang[0],tang[1])
print(cor)
print(pv)
