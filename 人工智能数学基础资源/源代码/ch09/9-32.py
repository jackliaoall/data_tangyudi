#9-32.py

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

# A / B = 1/3
plt.plot(np.linspace(0, 1, 200), 
         stats.beta.pdf(np.linspace(0, 1, 200), a=25, b=75),
        )
plt.fill_between(np.linspace(0, 1, 200),
                 stats.beta.pdf(np.linspace(0, 1, 200), a=25, b=75),
                 alpha=.15,
                )

# A / B = 1
plt.plot(np.linspace(0, 1, 200), 
         stats.beta.pdf(np.linspace(0, 1, 200), a=50, b=50),
        )
plt.fill_between(np.linspace(0, 1, 200),
                 stats.beta.pdf(np.linspace(0, 1, 200), a=50, b=50),
                 alpha=.15,
                )

# A / B = 3
plt.plot(np.linspace(0, 1, 200), 
         stats.beta.pdf(np.linspace(0, 1, 200), a=75, b=25),
        )
plt.fill_between(np.linspace(0, 1, 200),
                 stats.beta.pdf(np.linspace(0, 1, 200), a=75, b=25),
                 alpha=.15,
                )

# LEGEND
plt.text(x=0.15, y=5, s=r"$ \alpha = 25, \beta = 75$", rotation=80, alpha=.75, \
         weight="bold", color="#008fd5")
plt.text(x=0.39, y=5, s=r"$ \alpha = 50, \beta = 50$", rotation=80, alpha=.75, \
         weight="bold", color="#fc4f30")
plt.text(x=0.65, y=5, s=r"$ \alpha = 75, \beta = 25$", rotation=80, alpha=.75, \
         weight="bold", color="#e5ae38")


# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -.1, y = 11.75, s = \
         r"Beta Distribution - constant $\alpha + \beta$, varying $\frac{\alpha}{\beta}$",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -.1, y = 10, 
         s = 'Depicted below are three beta distributed random variables with '+ \
         r'equal $\alpha+\beta$ and varying $\frac{\alpha}{\beta} $'+ \
         '.\nAs one can see the fraction of ' + \
         r'$\frac{\alpha}{\beta} $ (mainly) shifts the distribution ' + \
         r'($\alpha$ towards 1, $\beta$ towards 0).',
         fontsize = 19, alpha = .85);
