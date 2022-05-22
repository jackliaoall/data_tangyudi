#方法三：调用sympy库
from sympy import *

x, y, z = symbols("x y z")#三个变量
eq = [x+y+z-2,x+2*y+4*z-3,x+3*y+9*z-5]#将三个公式改写为等式为0
result=solve(eq,[x,y,z])
print("结果是：",result)


