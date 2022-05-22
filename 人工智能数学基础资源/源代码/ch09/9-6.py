#9-6.py
from scipy.stats import norm

# additional imports for plotting purpose
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams["figure.figsize"] = (14, 7)

# continuous pdf for the plot
x_s = np.linspace(-3, 3, 50)
y_s = norm.pdf(x_s)
plt.scatter(x_s, y_s);
