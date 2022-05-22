import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
mpl.rcParams["font.sans-serif"] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False
x = np.linspace(0, 1, 100)
plt.plot(x, stats.beta.pdf(x,10,2),color='b',linestyle='-',linewidth=2 )
plt.plot(x, stats.beta.pdf(x,401,101),color='g',linestyle='-.',linewidth=2 )
plt.legend((u'A 商家 ', u'B 商家 '),loc='best')
#plt.savefig('B04958_01_05.png', dpi=300, figsize=(5.5, 5.5))
plt.show()