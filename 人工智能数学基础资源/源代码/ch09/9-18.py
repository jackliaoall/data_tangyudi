#9-18.py

# IMPORTS
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style

# PLOTTING CONFIG
%matplotlib inline
style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (14, 7)

plt.figure(dpi=100)

# PDF LAM = 1
plt.scatter(np.arange(20),
            (stats.poisson.pmf(np.arange(20), mu=1)),
            alpha=0.75,
            s=100
       )
plt.plot(np.arange(20),
         (stats.poisson.pmf(np.arange(20), mu=1)),
         alpha=0.75,
        )

# PDF LAM = 5
plt.scatter(np.arange(20),
            (stats.poisson.pmf(np.arange(20), mu=5)),
            alpha=0.75,
            s=100
       )
plt.plot(np.arange(20),
         (stats.poisson.pmf(np.arange(20), mu=5)),
         alpha=0.75,
        )

# PDF LAM = 10
plt.scatter(np.arange(20),
            (stats.poisson.pmf(np.arange(20), mu=10)),
            alpha=0.75,
            s=100
       )
plt.plot(np.arange(20),
         (stats.poisson.pmf(np.arange(20), mu=10)),
         alpha=0.75,
        )

# LEGEND
plt.text(x=3, y=.1, s="$\lambda = 1$", alpha=.75, rotation=-65, \
         weight="bold", color="#008fd5")
plt.text(x=8.25, y=.075, s="$\lambda = 5$", alpha=.75, rotation=-35, \
         weight="bold", color="#fc4f30")
plt.text(x=14.5, y=.06, s="$\lambda = 10$", alpha=.75, rotation=-20, 
         weight="bold", color="#e5ae38")

# TICKS
plt.xticks(range(21)[::2])
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -2.5, y = .475, s = "Poisson Distribution - $\lambda$",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -2.5, y = .425, 
         s = ('Depicted below are three Poisson distributed random variables'
              'with varying $\lambda $. As one can easily\nsee the parameter'
              ' $\lambda$ shifts and flattens the distribution (the smaller'
              ' $ \lambda $ the sharper the function).'),
         fontsize = 19, alpha = .85)
