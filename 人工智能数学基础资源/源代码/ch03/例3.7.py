import numpy as np
from scipy.integrate import dblquad
def integrand(x,y):
  return np.exp(-x**2-y**2)
x_a=0
x_b=10
y_a=0
y_b=10
solution,abserr=dblquad(integrand,x_a,x_b, lambda x :y_a,lambda x:y_b)
print(solution,abserr)
