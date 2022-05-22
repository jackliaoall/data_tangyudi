#9-27.py

from scipy.stats import beta

# draw a single sample
np.random.seed(42)
print(beta.rvs(a=2, b=2), end="\n\n")

# draw 10 samples
print(beta.rvs(a=2, b=2, size=10))
