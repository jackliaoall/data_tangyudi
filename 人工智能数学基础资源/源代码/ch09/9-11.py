#9-11.py

# IMPORTS
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
from IPython.core.display import HTML

# PLOTTING CONFIG
%matplotlib inline
style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (14, 7)

plt.figure(dpi=100)

# PDF
plt.bar(x=np.arange(20), 
        height=(stats.binom.pmf(np.arange(20), p=.5, n=20)), 
        width=.75,
        alpha=0.75
       )
# CDF
plt.plot(np.arange(20),
         stats.binom.cdf(np.arange(20), p=.5, n=20),
         color="#fc4f30",
        )

# LEGEND
plt.text(x=4.5, y=.7, s="pmf (normed)", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=14.5, y=.9, s="cdf", alpha=.75, weight="bold", color="#fc4f30")

# TICKS
plt.xticks(range(21)[::2])
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0.005, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -2.5, y = 1.25, s = "Binomial Distribution - Overview",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -2.5, y = 1.1, 
         s = ('Depicted below are the normed probability mass function (pmf) and the '
         'cumulative density\nfunction (cdf) of a Binomial distributed random variable '
         '$ y \sim Binom(N, p) $, given $ N = 20$ and $p =0.5 $.'),
         fontsize = 19, alpha = .85)
