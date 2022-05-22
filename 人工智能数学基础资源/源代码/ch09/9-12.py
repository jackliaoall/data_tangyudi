#9-12.py

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

# PDF P = .2
plt.scatter(np.arange(21),
            (stats.binom.pmf(np.arange(21), p=.2, n=20)),
            alpha=0.75,
            s=100
       )
plt.plot(np.arange(21),
         (stats.binom.pmf(np.arange(21), p=.2, n=20)),
         alpha=0.75,
        )

# PDF P = .5
plt.scatter(np.arange(21),
            (stats.binom.pmf(np.arange(21), p=.5, n=20)),
            alpha=0.75,
            s=100
       )
plt.plot(np.arange(21),
         (stats.binom.pmf(np.arange(21), p=.5, n=20)),
         alpha=0.75,
        )

# PDF P = .9
plt.scatter(np.arange(21),
            (stats.binom.pmf(np.arange(21), p=.9, n=20)),
            alpha=0.75,
            s=100
       )
plt.plot(np.arange(21),
         (stats.binom.pmf(np.arange(21), p=.9, n=20)),
         alpha=0.75,
        )

# LEGEND
plt.text(x=3.5, y=.075, s="$p = 0.2$", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=9.5, y=.075, s="$p = 0.5$", alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=17.5, y=.075, s="$p = 0.9$", alpha=.75, weight="bold", color="#e5ae38")

# TICKS
plt.xticks(range(21)[::2])
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -2.5, y = .37, s = "Binomial Distribution - $p$",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -2.5, y = .32, 
         s = ('Depicted below are three Binomial distributed random variables with varying'
              '$p $. As one can see\nthe parameter $p$ shifts and skews the distribution.'),
         fontsize = 19, alpha = .85)
