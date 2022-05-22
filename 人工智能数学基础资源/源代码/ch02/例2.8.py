import sympy
from sympy import oo # 注意无穷符号表示形式为两个小写字母 o
#import numpy as np
x=sympy.Symbol('x') 
f=sympy.sin(x)/(3*x+x**3)
print(sympy.limit(f,x,0))
