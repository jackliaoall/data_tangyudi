import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pandas as pd
import scipy.optimize as opt
messages = pd.read_csv('data/QQ_data.csv')  #读取数据
y_obs = messages['numbers'].values
np.seterr(invalid='ignore')
def poisson_logprob(mu, sign=-1):
#根据泊松模型和参数值返回观测数据的总似然值。
    return np.sum(sign*stats.poisson.logpmf(y_obs, mu=mu))
freq_results = opt.minimize_scalar(poisson_logprob)
x = np.linspace(1, 60)
y_min = np.min([poisson_logprob(i, sign=1) for i in x])
y_max = np.max([poisson_logprob(i, sign=1) for i in x])
#根据不同的mu值[1,60]，画出数据集的似然函数变化曲线
fig = plt.figure(figsize=(6,4))
plt.plot(x, [poisson_logprob(mu, sign=1) for mu in x])
plt.fill_between(x, [poisson_logprob(mu, sign=1) for mu in x], \
                 y_min,color='#348ABD',alpha=0.3)
#画出似然函数值最大的红色竖线
plt.vlines(freq_results['x'], y_max, y_min, colors='red', linestyles='dashed')
plt.scatter(freq_results['x'], y_max, s=110, c='red', zorder=3)
plt.ylim(ymin=y_min, ymax=0)
plt.title('Optimization of $\mu$')
plt.xlabel('$\mu$')
plt.ylabel('Log probability of $\mu$ given data')
plt.show()