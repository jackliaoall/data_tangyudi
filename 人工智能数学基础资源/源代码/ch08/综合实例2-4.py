import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import scipy.optimize as opt
messages = pd.read_csv('data/QQ_data.csv')  #读取数据
y_obs = messages['numbers'].values
np.seterr(invalid='ignore')
def poisson_logprob(mu, sign=-1):
#根据泊松模型和参数值返回观测数据的总似然值。
    return np.sum(sign*stats.poisson.logpmf(y_obs, mu=mu))
freq_results = opt.minimize_scalar(poisson_logprob)
fig = plt.figure(figsize=(11, 3))
# 画出参数mu为18泊松分布图
x_lim = 60
mu = np.int(freq_results['x'])
for i in np.arange(x_lim):
    plt.bar(i, stats.poisson.pmf(mu, i), color='#348ABD')
plt.xlim(0, x_lim)
plt.ylim(0, 0.1)
plt.title('Estimated Poisson distribution for QQmessages')
plt.xlabel('Number of QQmessages')
plt.ylabel('Probability mass')
plt.ylabel('Probability mass')
plt.legend(['$\mu$ = %s' % mu])
plt.show()
