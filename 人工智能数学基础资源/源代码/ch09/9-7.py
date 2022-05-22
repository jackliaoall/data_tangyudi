#9-7.py
from scipy.stats import norm
import scipy.stats as stats
# additional imports for plotting purpose
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams["figure.figsize"] = (14, 7)

plt.figure(dpi=100)

##### COMPUTATION #####
# DECLARING THE "TRUE" PARAMETERS UNDERLYING THE SAMPLE
mu_real = 10
sigma_real = 2

# DRAW A SAMPLE OF N=1000
np.random.seed(42)
sample = stats.norm.rvs(loc=mu_real, scale=sigma_real, size=1000)

# ESTIMATE MU AND SIGMA
mu_est = np.mean(sample)
sigma_est = np.std(sample)
print("Estimated MU: {}\nEstimated SIGMA: {}".format(mu_est, sigma_est))

##### PLOTTING #####
# SAMPLE DISTRIBUTION
plt.hist(sample, bins=50,normed=True, alpha=.25)

# TRUE CURVE
plt.plot(np.linspace(2, 18, 1000), norm.pdf(np.linspace(2, 18, 1000),\
                loc=mu_real, scale=sigma_real), color="red",linestyle="dashed")

# ESTIMATED CURVE
plt.plot(np.linspace(2, 18, 1000), norm.pdf(np.linspace(2, 18, 1000),\
            loc=np.mean(sample), scale=np.std(sample)),color="green",linewidth=2)

# LEGEND
plt.text(x=9.5, y=.1, s="sample", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=7, y=.2, s="true distrubtion", rotation=55, alpha=.75, weight="bold", \
         color="red")
plt.text(x=5, y=.12, s="estimated distribution", rotation=55, alpha=.75, weight="bold", \
         color="green")

# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE
plt.text(x = 0, y = 0.3, s = "Normal Distribution",
               fontsize = 26, weight = 'bold', alpha = .75)
