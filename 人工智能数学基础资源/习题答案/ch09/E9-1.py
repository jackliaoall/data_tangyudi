#E9-1.py
from scipy.stats import norm

# probability of x less or equal 0.3
print("P(X < {}) = 0.1".format(norm.ppf(0.1)))

# probability of x in [-0.2, +0.2]
print("P(X < {}) = 0.05".format(norm.ppf(0.05)))
