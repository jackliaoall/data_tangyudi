from  scipy.stats import chi2_contingency
import numpy as np
kf_data = np.array([[37,27], [39,21]])
kf = chi2_contingency(kf_data)
print('chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s'%kf)

