#9-29.py

from scipy.stats import beta

# probability of x less or equal 0.3
print("P(X <0.3) = {:.3}".format(beta.cdf(a=2, b=2, x=0.3)))

# probability of x in [-0.2, +0.2]
print("P(-0.2 < X < 0.2) = {:.3}".format(beta.cdf(a=2, b=2, x=0.2) - \
                                         beta.cdf(a=2, b=2, x=-0.2)))
