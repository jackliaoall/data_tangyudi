#13-12.py
import numpy as np
import scipy.stats as stats  

#data source
x = np.array([170, 150, 210, 180, 160])
y = np.array([188, 165, 190, 172, 168])
print(x)
print(y)
print()

#pearson coef
correlation,pvalue = stats.pearsonr(x,y) 
#r=np.sum((x-np.mean(x))*(y-np.mean(y)))/(np.std(x)*np.std(y))/5
r=np.sum((x-np.mean(x))*(y-np.mean(y)))/(np.sqrt(np.sum((x-np.mean(x))**2))) \
  /np.sqrt(np.sum((y-np.mean(y))*(y-np.mean(y))))
print ('pearson-coef-by-function =',correlation)
print ('pvalue =',pvalue)
print('pearson-coef-by-math =',r)
print()

#spearman coef
x=stats.rankdata(x)
y = stats.rankdata(y)
print (x)
print (y)
print(x-y)
print()
correlation,pvalue = stats.spearmanr(x,y)  
r=1-6*2/(5*5*5-5)
print ('spearman-coef-by-function =',correlation)
print ('pvalue =',pvalue)
print('spearman-coef-by-math =',r)