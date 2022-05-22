#9-14.py
import numpy as np
from scipy.stats import poisson

# draw a single sample
np.random.seed(42)
print(poisson.rvs(mu=10), end="\n\n")

# draw 10 samples
print(poisson.rvs(mu=10, size=10), end="\n\n")
