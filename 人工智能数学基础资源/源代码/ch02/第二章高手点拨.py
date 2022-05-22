import sympy
#常用的 Sympy 内置符号。
print(sympy.E)
print(sympy.log(sympy.E))#自然对数的底 e 的表示方式。
print( 1/sympy.oo)#无穷大 ∞ 的表示方式。
print( sympy.sin(sympy.pi))#圆周率 π 的表示方式。



#Sympy 可以用一套符号系统来表示一个表达式，如函数、多项式等，并且可以进行求值。
x = sympy.Symbol('x')
fx = 2*x + 1     # fx 是一个表达式
print(fx.evalf(subs={x:2}))   # 用 evalf 函数，传入变量的值，对表达式进行求值

x,y = sympy.symbols('x y')
f = 2 * x + y
f.evalf(subs = {x:1,y:2}) # 以字典的形式传入多个变量的值

print(f.evalf(subs = {x:1}))# 如果只传入一个变量的值，则输出原来的表达式
print(f.evalf(subs = {x:1,y:2}))# 用 evalf 函数，传入变量的值，对表达式进行求值



#数组的操作
import numpy as np
a=np.array([1,2,3]) # 创建一个秩 (rank)1 数组
print(a[0], a[1], a[2])
b = np.array([[1,2,3],[4,5,6]]) # 创建一个秩 2 数组
print(b[0,0],b[0,1],b[1,0])


#在绘制三维图表时，需要用到 NumPy 中的 mgrid 函数
print (np.mgrid[-1:4:2])
print(np.mgrid[-1:4:2,-3:1:1])
print(np.mgrid[-1:4:2,-3:1:2])

#使用 scipy.misc 模块下的 derivative 方法函数
import numpy as np
from scipy.misc import derivative
def f(x): # 定义函数
  return x**5
print (derivative(f, 2, dx=1e-6))# 对函数在 x=2 处求导










