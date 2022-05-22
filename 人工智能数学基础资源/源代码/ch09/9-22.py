#9-22.py

import numpy as np
from scipy.stats import chi2

# draw a single sample
np.random.seed(42)
print(chi2.rvs(df=4), end="\n\n")

# draw 10 samples
print(chi2.rvs(df=4, size=10), end="\n\n")
