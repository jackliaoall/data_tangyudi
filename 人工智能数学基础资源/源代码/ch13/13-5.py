#13-5.py

import numpy as np
import scipy.stats as stats  
import matplotlib.pyplot as plt
#https://docs.scipy.org/doc/scipy-0.19.1/reference/stats.html#module-scipy.stats

#data source
x = [10.35, 6.24, 3.18, 8.46, 3.21, 7.65, 4.32, 8.66, 9.12, 10.31]  
y = [5.1, 3.15, 1.67, 4.33, 1.76, 4.11, 2.11, 4.88, 4.99, 5.12]  

#compute correlation and pvalue
correlation,pvalue = stats.pearsonr(x,y) 
print ('correlation',correlation)
print ('pvalue',pvalue)

#create figure and configuring
plt.figure(figsize=(8,5), dpi=80)
plt.subplot(111)

#plotting the scatter figure
plt.scatter(x,y,color='red')
plt.show();
