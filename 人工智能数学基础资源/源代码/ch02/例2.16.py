import numpy as np
p = np.poly1d([1,2,0,3,0,5]) # 构造多项式
print(p) # 下面两行为多项式的显示形式，5、4、2 是下一行项数所对应的幂次。
print( np.polyder(p,1))# 求一阶导数
print( np.polyder(p,1)(1.0))# 求一阶导数在点 x=1 的值。
print (p.deriv(1))# 求一阶导数
print (p.deriv(1)(1.0))# 求一阶导数在点 x=1 的值。
