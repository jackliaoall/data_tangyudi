import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
theta_real =1
# 做 4 次试验结果，每次抛 20 次，正面朝上次数分别是：0，5，10，20
trials = [ 20, 20, 20, 20]
data = [ 0, 5, 10, 20]
beta_params = [(1, 1)]
dist = stats.beta #dist 设为 Beta 分布
x = np.linspace(0, 1, 100)
for idx, N in enumerate(trials):
    if idx == 0:
        plt.subplot(2,2, 1)
    else:
        plt.subplot(2, 2, idx + 1)
    y = data[idx]
    for (a_prior, b_prior), c in zip(beta_params, ('b')):
    # 后验概率
        p_theta_given_y = dist.pdf(x, a_prior + y, b_prior+N-y)
        plt.plot(x, p_theta_given_y, c)
        plt.fill_between(x, 0, p_theta_given_y, color=c, alpha=0.6)
    # 先验概率
    plt.plot(x, stats.beta.pdf(x, 1, 1), color='r', linestyle='--' \
             ,linewidth=1,alpha=0.5 )
    plt.plot(0, 0, label='{:d} 次试验 \n{:d} 次正面 '.format(N, y), alpha=0)
    plt.xlim(0, 1)
    plt.ylim(0, 12)
    plt.xlabel(r' 参数 $\theta$')
    plt.legend()
    plt.gca().axes.get_yaxis().set_visible(False)
plt.tight_layout()
plt.show()