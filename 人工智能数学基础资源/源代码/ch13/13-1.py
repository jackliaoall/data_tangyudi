#13-1.py
import numpy as np
tang = np.array([[10, 10, 8, 9, 7],  
       [4, 5, 4, 3, 3],  
       [3, 3, 1, 1, 1]])
print('data source')
print(tang)

print('corrcoef between rowdata')
print(np.corrcoef(tang))

print('corrcoef between columndata')
print(np.corrcoef(tang,rowvar=0));
