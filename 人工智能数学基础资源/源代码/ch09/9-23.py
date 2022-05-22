#9-23.py

from scipy.stats import chi2

# additional imports for plotting purpose
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams["figure.figsize"] = (14,7)

# continuous pdf for the plot
x_s = np.arange(15)
y_s = chi2.pdf(x=x_s, df=4)
plt.scatter(x_s, y_s, s=100);
