#9-2.py
from scipy.stats import norm

# probability of x less or equal 0.3
print("P(X <0.3) = {}".format(norm.cdf(0.3)))

# probability of x in [-0.2, +0.2]
print("P(-0.2 < X < 0.2) = {}".format(norm.cdf(0.2) - norm.cdf(-0.2)))
