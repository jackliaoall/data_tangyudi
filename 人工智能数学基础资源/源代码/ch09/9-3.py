#9-3.py

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
plt.plot(np.linspace(-4, 4, 100), 
         stats.norm.pdf(np.linspace(-4, 4, 100)) 
         / np.max(stats.norm.pdf(np.linspace(-3, 3, 100))),
        )
plt.fill_between(np.linspace(-4, 4, 100),
                 stats.norm.pdf(np.linspace(-4, 4, 100)) 
                 / np.max(stats.norm.pdf(np.linspace(-3, 3, 100))),
                 alpha=.15,
                )
# CDF
plt.plot(np.linspace(-4, 4, 100), 
         stats.norm.cdf(np.linspace(-4, 4, 100)),
        )

# LEGEND
plt.text(x=-1.5, y=.7, s="pdf (normed)", rotation=65, 
         alpha=.75, weight="bold", color="#008fd5")
plt.text(x=-.4, y=.5, s="cdf", rotation=55, alpha=.75, 
         weight="bold", color="#fc4f30")

# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE
plt.text(x = -5, y = 1.25, s = "Normal Distribution - Overview",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -5, y = 1.1, 
         s = ('Depicted below are the normed probability density function (pdf)'
              'and the cumulative density \nfunction (cdf) of a normally distributed'
              ' random variable $ y \sim \mathcal{N}(\mu,\sigma) $,'
              'given $ \mu = 0 $ and $ \sigma = 1$.'),
         fontsize = 19, alpha = .85)
