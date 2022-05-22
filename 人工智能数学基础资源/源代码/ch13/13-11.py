#13-11.py
import scipy.stats as stats

x = [1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,0,0,0]
y = [84,82,76,60,72,74,76,84,88,90,78,80,92,94,96,88,90,78,76,74]
coef,pvalue=stats.pointbiserialr(x, y)

print('pointbiserialcorrcoef',coef)
print('pvalue',pvalue)
