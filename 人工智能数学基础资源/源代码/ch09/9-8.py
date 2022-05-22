#9-8.py
import numpy as np
from scipy.stats import binom

# draw a single sample
np.random.seed(42)
print(binom.rvs(p=0.3, n=10), end="\n\n")

# draw 10 samples
print(binom.rvs(p=0.3, n=10, size=10), end="\n\n")
