from scipy import stats
from scipy.stats import norm
import numpy as np
import pylab as plt
X = norm()                    # 默认参数，loc=0，scale=1
Y = norm(loc=1.0,scale=2.0)   #loc 和 scale 参数 , 对应正态分布的期望和标准差
t = np.arange(-10,10,0.01)
plt.plot(t, X.pdf(t), label="$X$", color="red")
plt.plot(t, Y.pdf(t), "b--", label="$Y$")
plt.legend()
plt.show()