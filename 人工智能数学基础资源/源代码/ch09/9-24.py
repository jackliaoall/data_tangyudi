#9-24.py

from scipy.stats import chi2

# probability of x less or equal 0.3
print("P(X <=3) = {}".format(chi2.cdf(x=3, df=4)))

# probability of x in [-0.2, +0.2]
print("P(2 < X <= 8) = {}".format(chi2.cdf(x=8, df=4) - chi2.cdf(x=2, df=4)))
