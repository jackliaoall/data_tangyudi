import sympy
#from sympy import oo # 注意无穷符号表示形式为两个小写字母 o
#import numpy as np
x=sympy.Symbol('x') # 注意 Symbol 第一字母大写
f=(x**2-1)/(x-1)
sympy.limit(f,x,1)
print(sympy.limit(f,x,1))
