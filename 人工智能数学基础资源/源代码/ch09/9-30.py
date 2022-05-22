#9-30.py

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
plt.plot(np.linspace(0, 1, 100), 
         stats.beta.pdf(np.linspace(0, 1, 100),a=2,b=2) 
        )
plt.fill_between(np.linspace(0, 1, 100),
                 stats.beta.pdf(np.linspace(0, 1, 100),a=2,b=2),
                 alpha=.15
                )

# CDF
plt.plot(np.linspace(0, 1, 100), 
         stats.beta.cdf(np.linspace(0, 1, 100),a=2,b=2),
        )

# LEGEND
plt.text(x=0.1, y=.7, s="pdf (normed)", rotation=52, alpha=.75, weight="bold", \
         color="#008fd5")
plt.text(x=0.45, y=.5, s="cdf", rotation=40, alpha=.75, weight="bold", \
         color="#fc4f30")

# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -.125, y = 1.85, s = "Beta Distribution - Overview",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -.125, y = 1.6, 
         s = ('Depicted below are the normed probability density function '
              '(pdf) and the cumulative density\nfunction (cdf) of a beta '
              'distributed random variable ') +\
         r'$ y \sim Beta(\alpha, \beta)$, given $ \alpha = 2 $ and $ \beta = 2$.',
         fontsize = 19, alpha = .85);
