#9-19.py

# IMPORTS
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt
import matplotlib.style as style
from collections import Counter

# PLOTTING CONFIG
%matplotlib inline
style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (14, 7)

plt.figure(dpi=100)

##### COMPUTATION #####
# DECLARING THE "TRUE" PARAMETERS UNDERLYING THE SAMPLE
lambda_real = 7

# DRAW A SAMPLE OF N=1000
np.random.seed(42)
sample = poisson.rvs(mu=lambda_real, size=1000)

# ESTIMATE MU AND SIGMA
lambda_est = np.mean(sample)
print("Estimated LAMBDA: {}".format(lambda_est))

##### PLOTTING #####
# SAMPLE DISTRIBUTION
cnt = Counter(sample)
_, values = zip(*sorted(cnt.items()))
plt.bar(range(len(values)), values/np.sum(values), alpha=0.25);

# TRUE CURVE
plt.plot(range(18), poisson.pmf(k=range(18), mu=lambda_real), color="#fc4f30", \
         linestyle="dashed")

# ESTIMATED CURVE
plt.plot(range(18), poisson.pmf(k=range(18), mu=lambda_est), color="#e5ae38")

# LEGEND
plt.text(x=6, y=.06, s="sample", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=3.5, y=.14, s="true distrubtion", rotation=60, alpha=.75, weight="bold", \
         color="#fc4f30")
plt.text(x=1, y=.08, s="estimated distribution", rotation=60, alpha=.75, weight="bold", \
         color="#e5ae38")

# TICKS
plt.xticks(range(17)[::2])
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0.0009, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -2.5, y = 0.19, s = "Poisson Distribution - Parameter Estimation",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -2.5, y = 0.17, 
         s = ('Depicted below is the distribution of a sample (blue) drawn from a '
              'Poisson distribution with $\lambda = 7$.\nAlso the estimated distrubution '
              'with $\lambda \sim {:.3f}$ is shown (yellow).').format(np.mean(sample)),
         fontsize = 19, alpha = .85)
plt.show()
