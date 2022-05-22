#9-25.py

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
plt.plot(np.linspace(0, 20, 100), 
         stats.chi2.pdf(np.linspace(0, 20, 100), df=4) ,
        )
plt.fill_between(np.linspace(0, 20, 100),
                 stats.chi2.pdf(np.linspace(0, 20, 100), df=4) ,
                 alpha=.15,
                )

# CDF
plt.plot(np.linspace(0, 20, 100), 
         stats.chi2.cdf(np.linspace(0, 20, 100), df=4),
        )

# LEGEND
plt.xticks(np.arange(0, 21, 2))
plt.text(x=11, y=.25, s="pdf (normed)", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=11, y=.85, s="cdf", alpha=.75, weight="bold", color="#fc4f30")

# TICKS
plt.xticks(np.arange(0, 21, 2))
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -2, y = 1.25, s = r"Chi-Squared $(\chi^{2})$ Distribution - Overview",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -2, y = 1.1, 
         s = ('Depicted below are the normed probability density function (pdf) and '
              'the cumulative density\nfunction (cdf) of a Chi-Squared distributed '
              'random variable $ y \sim \chi^{2}(k) $, given $k$=4.'),
         fontsize = 19, alpha = .85);
