#9-28.py

from scipy.stats import beta

# additional import for plotting
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams["figure.figsize"] = (14, 7)


# continuous pdf for the plot
x_s = np.linspace(0, 1, 100)
y_s = beta.pdf(a=2, b=2, x=x_s)
plt.scatter(x_s, y_s);
