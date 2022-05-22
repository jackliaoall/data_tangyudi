#13-10.py

import scipy.stats as stats

x1 = [10, 9, 8, 7, 6]
x2 = [10, 8, 9, 6, 7]

tau, p_value = stats.kendalltau(x1, x2)
print ('tau',tau)
print ('p_value',p_value)
