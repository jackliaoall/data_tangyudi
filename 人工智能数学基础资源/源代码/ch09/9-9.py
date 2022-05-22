#9-9.py
from scipy.stats import binom

# additional imports for plotting purpose
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams["figure.figsize"] = (14,7)

# likelihood of x and y
x = 1
y = 7
print("pmf(X=1) = {}\npmf(X=7) = {}".format(binom.pmf(k=x, p=0.3, n=10), \
                                            binom.pmf(k=y, p=0.3, n=10)))

# continuous pdf for the plot
x_s = np.arange(11)
y_s = binom.pmf(k=x_s, p=0.3, n=10)
plt.scatter(x_s, y_s, s=100);
