import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import scipy.stats as stats
import scipy.optimize as opt
import statsmodels.api as sm
messages = pd.read_csv('data/QQ_data.csv')  #读取数据
y_obs = messages['numbers'].values
np.seterr(invalid='ignore')
def poisson_logprob(mu, sign=-1):
    # 根据泊松模型和参数值返回观测数据的总似然值
    print(" 参数 mu: ",mu)
    return np.sum(sign*stats.poisson.logpmf(y_obs, mu=mu))
freq_results = opt.minimize_scalar(poisson_logprob)
print("参数 mu 的估计值: %s" % freq_results['x'])
