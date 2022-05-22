#9-31.py

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

# A = B = 1
plt.plot(np.linspace(0, 1, 200), 
         stats.beta.pdf(np.linspace(0, 1, 200), a=1, b=1),
        )
plt.fill_between(np.linspace(0, 1, 200),
                 stats.beta.pdf(np.linspace(0, 1, 200), a=1, b=1),
                 alpha=.15,
                )

# A = B = 10
plt.plot(np.linspace(0, 1, 200), 
         stats.beta.pdf(np.linspace(0, 1, 200), a=10, b=10),
        )
plt.fill_between(np.linspace(0, 1, 200),
                 stats.beta.pdf(np.linspace(0, 1, 200), a=10, b=10),
                 alpha=.15,
                )

# A = B = 100
plt.plot(np.linspace(0, 1, 200), 
         stats.beta.pdf(np.linspace(0, 1, 200), a=100, b=100),
        )
plt.fill_between(np.linspace(0, 1, 200),
                 stats.beta.pdf(np.linspace(0, 1, 200), a=100, b=100),
                 alpha=.15,
                )

# LEGEND
plt.text(x=0.1, y=1.45, s=r"$ \alpha = 1, \beta = 1$", alpha=.75, weight="bold", \
         color="#008fd5")
plt.text(x=0.325, y=3.5, s=r"$ \alpha = 10, \beta = 10$", rotation=35, alpha=.75, \
         weight="bold", color="#fc4f30")
plt.text(x=0.4125, y=8, s=r"$ \alpha = 100, \beta = 100$", rotation=80, alpha=.75, \
         weight="bold", color="#e5ae38")

# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -.1, y = 13.75, s = \
         r"Beta Distribution - constant $\frac{\alpha}{\beta}$, varying $\alpha + \beta$",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -.1, y = 12, 
         s = 'Depicted below are three beta distributed random variables with ' \
         + r'equal $\frac{\alpha}{\beta} $ and varying $\alpha+\beta$'+ \
         '.\nAs one can see the sum of ' + \
         r'$\alpha + \beta$ (mainly) sharpens the distribution (the bigger the sharper).',
         fontsize = 19, alpha = .85);
