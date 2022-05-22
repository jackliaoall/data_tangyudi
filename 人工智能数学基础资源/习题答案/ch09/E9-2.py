#E9-2.py
# IMPORTS
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.style as style
from IPython.core.display import HTML

# PLOTTING CONFIG
%matplotlib inline
style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (14, 7)
plt.figure(dpi=100)

# PDF
plt.plot(np.linspace(-4, 4, 100), 
         norm.pdf(np.linspace(-4, 4, 100)) 
        )
plt.fill_between(np.linspace(-4, norm.ppf(0.05), 50),
                 norm.pdf(np.linspace(-4, norm.ppf(0.05), 50)), 
                 alpha=.15,
                )
plt.xticks([-4, -3, -2, norm.ppf(0.05), -1, 0, 1, 2, 3, 4],['-4', '-3', '-2','x2', '-1', '0', '1', '2', '3', '4'])
#plt.xticks([norm.ppf(0.05), 0],['x2', '0'])

plt.show()
