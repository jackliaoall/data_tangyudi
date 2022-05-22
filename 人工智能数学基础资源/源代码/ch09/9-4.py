#9-4.py
# IMPORTS
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style

%matplotlib inline
style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (14, 7)
plt.figure(dpi=100)

# PDF MU = 0
plt.plot(np.linspace(-4, 4, 100), 
         stats.norm.pdf(np.linspace(-4, 4, 100)),
        )
plt.fill_between(np.linspace(-4, 4, 100),
                 stats.norm.pdf(np.linspace(-4, 4, 100)),
                 alpha=.15,
                )

# PDF MU = 2
plt.plot(np.linspace(-4, 4, 100), 
         stats.norm.pdf(np.linspace(-4, 4, 100), loc=2),
        )
plt.fill_between(np.linspace(-4, 4, 100),
                 stats.norm.pdf(np.linspace(-4, 4, 100),loc=2),
                 alpha=.15,
                )

# PDF MU = -2
plt.plot(np.linspace(-4, 4, 100), 
         stats.norm.pdf(np.linspace(-4, 4, 100), loc=-2),
        )
plt.fill_between(np.linspace(-4, 4, 100),
                 stats.norm.pdf(np.linspace(-4, 4, 100),loc=-2),
                 alpha=.15,
                )

# LEGEND
plt.text(x=-1, y=.35, s="$ \mu = 0$", rotation=65, alpha=.75, \
         weight="bold", color="#008fd5")
plt.text(x=1, y=.35, s="$ \mu = 2$", rotation=65, alpha=.75, \
         weight="bold", color="#fc4f30")
plt.text(x=-3, y=.35, s="$ \mu = -2$", rotation=65, alpha=.75, \
         weight="bold", color="#e5ae38")

# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, 
plt.text(x = -5, y = 0.51, s = "Normal Distribution - $ \mu $",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -5, y = 0.45, 
         s = ('Depicted below are three normally distributed random variables '
              'with varying $ \mu $. As one can easily\nsee the parameter $\mu$ '
              'shifts the distribution along the x-axis.'),
         fontsize = 19, alpha = .85)
