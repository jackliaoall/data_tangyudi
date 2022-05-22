#9-1.py
from scipy.stats import norm

# draw a single sample
print(norm.rvs(), end="\n\n")

# draw 10 samples
print(norm.rvs(size=10), end="\n\n")

# adjust mean ('loc') and standard deviation ('scale')
print(norm.rvs(loc=10, scale=0.1), end="\n\n")
