#9-16.py
from scipy.stats import poisson

# probability of x less or equal 0.3
print("P(X <=3) = {}".format(poisson.cdf(k=3, mu=5)))

# probability of x in [-0.2, +0.2]
print("P(2 < X <= 8) = {}".format(poisson.cdf(k=8, mu=5) - poisson.cdf(k=2, mu=5)))
