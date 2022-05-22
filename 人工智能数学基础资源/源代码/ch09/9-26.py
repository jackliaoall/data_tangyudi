#9-26.py

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

# PDF k = 1
plt.plot(np.linspace(0, 15, 500), 
         stats.chi2.pdf(np.linspace(0, 15, 500), df=1),
        )
plt.fill_between(np.linspace(0, 15, 500),
                 stats.chi2.pdf(np.linspace(0, 15, 500), df=1),
                 alpha=.15,
                )

# PDF k = 3
plt.plot(np.linspace(0, 15, 100), 
         stats.chi2.pdf(np.linspace(0, 15, 100), df=3),
        )
plt.fill_between(np.linspace(0, 15, 100),
                 stats.chi2.pdf(np.linspace(0, 15, 100), df=3),
                 alpha=.15,
                )

# PDF k = 6
plt.plot(np.linspace(0, 15, 100), 
         stats.chi2.pdf(np.linspace(0, 15, 100), df=6),
        )
plt.fill_between(np.linspace(0, 15, 100),
                 stats.chi2.pdf(np.linspace(0, 15, 100), df=6),
                 alpha=.15,
                )

# LEGEND
plt.text(x=.5, y=.7, s="$ k = 1$", rotation=-65, alpha=.75, weight="bold", color="#008fd5")
plt.text(x=1.5, y=.35, s="$ k = 3$", alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=5, y=.2, s="$ k = 6$", alpha=.75, weight="bold", color="#e5ae38")


# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -1.5, y = 2.8, s = "Chi-Squared Distribution - $ k $",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -1.5, y = 2.5, 
         s = ('Depicted below are three Chi-Squared distributed random variables '
              'with varying $ k $. As one can\nsee the parameter $k$ smoothens '
              'the distribution and softens the skewness.'),
         fontsize = 19, alpha = .85);
