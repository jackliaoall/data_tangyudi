#9-33.py
# IMPORTS
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
from IPython.core.display import HTML

# PLOTTING CONFIG
%matplotlib inline
#style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (14, 7)

plt.figure(dpi=100)

# PDF
plt.plot(np.linspace(0, 1, 500), 
         stats.beta.pdf(np.linspace(0, 1, 500),a=82,b=220),label='a=82,b=220', \
         linewidth=1 
        )

plt.plot(np.linspace(0, 1, 500), 
         stats.beta.pdf(np.linspace(0, 1, 500),a=84,b=220),label='a=84,b=220', \
         linewidth=2, linestyle='dashed' 
        )

plt.plot(np.linspace(0, 1, 500), 
         stats.beta.pdf(np.linspace(0, 1, 500),a=182,b=420),label='a=182,b=420', \
         linewidth=3 
        )

#AXISES LABEL
plt.xlabel('X',size=20)
plt.ylabel('Density of Beta',size=20)

# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.xticks(np.linspace(0,1,11))

#SHOWING TEXT IN CANVAS
plt.legend()

plt.show()
