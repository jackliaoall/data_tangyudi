#9-21.py

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

# PDF loc=0, scale=1
plt.plot(np.linspace(-8, 8, 100), 
         stats.uniform.pdf(np.linspace(-8, 8, 100),loc=0, scale=1),
        )
plt.fill_between(np.linspace(-8, 8, 100),
                 stats.uniform.pdf(np.linspace(-8, 8, 100),loc=0, scale=1),
                 alpha=.15,
                )

# PDF loc=0, scale=2
plt.plot(np.linspace(-8, 8, 100), 
         stats.uniform.pdf(np.linspace(-8, 8, 100), loc=0, scale=2),
        )
plt.fill_between(np.linspace(-8, 8, 100),
                 stats.uniform.pdf(np.linspace(-8, 8, 100),loc=0, scale=2),
                 alpha=.15,
                )

# PDF loc=-3, scale=3
plt.plot(np.linspace(-8, 8, 100), 
         stats.uniform.pdf(np.linspace(-4, 4, 100), loc=-3, scale=3),
        )
plt.fill_between(np.linspace(-8, 8, 100),
                 stats.uniform.pdf(np.linspace(-4, 4, 100),loc=-3, scale=3),
                 alpha=.15,
                )

# LEGEND
plt.text(x=-1, y=.65, s="loc=0, scale=1", rotation=65, alpha=.75, \
         weight="bold", color="#008fd5")
plt.text(x=1, y=.65, s="loc=0, scale=2", rotation=65, alpha=.75, \
         weight="bold", color="#fc4f30")
plt.text(x=-3, y=.65, s="loc=-3, scale=3", rotation=65, alpha=.75, \
         weight="bold", color="#e5ae38")


# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, 
plt.text(x = -5, y = 1.1, s = "Uniform Distribution - loc and scale",
               fontsize = 26, weight = 'bold', alpha = .75)
