import numpy as np
A=np.array([[0,1,0],[1/2**0.5,0,1/2**0.5],[-1/2**0.5,0,1/2**0.5]])
print("A×A.T=\n",np.round(A.dot(A.T),0))