#9-17.py

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
        height=(stats.poisson.pmf(np.arange(20), mu=5)), 
        width=.75,
        alpha=0.75
       )

# CDF
plt.plot(np.arange(20), 
         stats.poisson.cdf(np.arange(20), mu=5),
         color="#fc4f30",
        )

# LEGEND
plt.text(x=8, y=.45, s="pmf (normed)", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=8.5, y=.9, s="cdf", alpha=.75, weight="bold", color="#fc4f30")

# TICKS
plt.xticks(range(21)[::2])
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0.005, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -2.5, y = 1.25, s = "Poisson Distribution - Overview",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -2.5, y = 1.1, 
         s = ('Depicted below are the normed probability mass function (pmf) and the '
              'cumulative density\nfunction (cdf) of a Poisson distributed random '
              'variable $ y \sim Poi(\lambda) $, given $ \lambda = 5 $.'),
         fontsize = 19, alpha = .85)
