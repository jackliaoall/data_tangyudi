import numpy as np
from scipy import stats

mean1 = 30.97
mean2 = 21.79

std1 = 26.7
std2 = 12.1

nobs1 = 10
nobs2 = 10

modified_std1 = np.sqrt(np.float32(nobs1)/np.float32(nobs1-1)) * std1
modified_std2 = np.sqrt(np.float32(nobs2)/np.float32(nobs2-1)) * std2

(statistic, pvalue) = stats.ttest_ind_from_stats(mean1=mean1, std1=modified_std1, nobs1=10, mean2=mean2, std2=modified_std2, nobs2=10)

print("t statistic is: ", statistic)
print("pvalue is: ", pvalue)

