#9-13.py

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

# PDF N = 10
plt.scatter(np.arange(11),
            (stats.binom.pmf(np.arange(11), p=.5, n=10)),
            alpha=0.75,
            s=100
       )
plt.plot(np.arange(11),
         (stats.binom.pmf(np.arange(11), p=.5, n=10)),
         alpha=0.75,
        )

# PDF N = 15
plt.scatter(np.arange(16),
            (stats.binom.pmf(np.arange(16), p=.5, n=15)),
            alpha=0.75,
            s=100
       )
plt.plot(np.arange(16),
         (stats.binom.pmf(np.arange(16), p=.5, n=15)),
         alpha=0.75,
        )

# PDF N = 20
plt.scatter(np.arange(21),
            (stats.binom.pmf(np.arange(21), p=.5, n=20)),
            alpha=0.75,
            s=100
       )
plt.plot(np.arange(21),
         (stats.binom.pmf(np.arange(21), p=.5, n=20)),
         alpha=0.75,
        )

# LEGEND
plt.text(x=6, y=.225, s="$N = 10$", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=8.5, y=.2, s="$N = 15$", alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=11, y=.175, s="$N = 20$", alpha=.75, weight="bold", color="#e5ae38")

# TICKS
plt.xticks(range(21)[::2])
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -2.5, y = .31, s = "Binomial Distribution - $N$",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -2.5, y = .27, 
         s = ('Depicted below are three Binomial distributed random variables with varying '
              '$N$. As one can see\nthe parameter $N$ streches the distribution (the larger '
              '$N$ the flatter the distribution).'),
         fontsize = 19, alpha = .85)
