#9-10.py
from scipy.stats import binom

# probability of x less or equal 0.3
print("P(X <=3) = {}".format(binom.cdf(k=3, p=0.3, n=10)))

# probability of x in [-0.2, +0.2]
print("P(2 < X <= 8) = {}".format(binom.cdf(k=8, p=0.3, n=10) - binom.cdf(k=2, p=0.3, n=10)))
