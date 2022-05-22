#13-2.py

import numpy as np
import scipy.stats as stats
tang = np.array([[3.8, 4, 5.8, 8, 11.3, 14.4,16.5,16.2,13.8,10.8,6.7,4.7],  
       [77.7, 51.2, 60.1, 54.1, 55.4, 56.8, 45, 55.3, 67.5, 73.3, 76.6, 79.6]])
print(tang)

print(np.corrcoef(tang))
