from sympy import * 
from sympy.abc import x,y,z,f
f=x**2+3*x*y+y**2
print(diff(f,x)) # 求偏导
print(diff(f,y))
fx=diff(f,x) # 求偏导并将结果赋给 fx
print(fx.evalf(subs={x:1,y:2}))# 以字典的形式传入多个变量的值，求函数值。
fy=diff(f,y)
print(fy.evalf(subs={x:1,y:2}))
