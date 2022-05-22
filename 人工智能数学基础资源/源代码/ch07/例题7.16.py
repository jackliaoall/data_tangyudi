import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
def test_norm_pmf():
    # 正态分布是一种连续分布，其函数可以在实线上的任何地方取值。
    # 正态分布由两个参数描述：分布的平均值μ和方差σ2 。
    mu = 0 #mean
    sigma = 1#standard deviation
    x = np.arange(-5,5,0.1)     #生成随机数x
    # 得到对应的概率值y
    y = (1/(np.sqrt(2*np.pi*sigma*sigma)))* \
        np.exp(-(((x-mu)**2)/(2*sigma*sigma)))
    fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(10, 5))
    ax0.plot(x, y)
    ax1.plot(x,stats.norm.cdf(x,0,1))
    ax0.set_title('Normal: $\mu$=%.1f, $\sigma^2$=%.1f' % (mu,sigma))
    ax0.set_xlabel('x')
    ax0.set_ylabel('Probability density', fontsize=15)
    ax1.set_title('Normal: $\mu$=%.1f, $\sigma^2$=%.1f' % (mu, sigma))
    ax1.set_xlabel('x')
    ax1.set_ylabel('Cumulative density', fontsize=15)
    fig.subplots_adjust(wspace=0.4)
    plt.show()
test_norm_pmf()
