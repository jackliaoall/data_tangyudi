#13-3.py

import numpy as np
tang = np.array([[74, 71, 72, 68, 76,73,67,70,65,74],  
       [76, 75, 71, 70, 76, 79, 65, 77, 62, 72]])
print(tang[0])
print(tang[1])
print(np.corrcoef(tang))
