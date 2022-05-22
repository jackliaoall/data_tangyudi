import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
def Fun(x, y):
  return x-y + 2 * x * x + 2 * x * y + y * y
def PxFun(x, y): # 求 x 偏导
  return 1 + 4 * x + 2 * y
def PyFun(x, y): # 求 y 偏导
  return -1 + 2 * x + 2 * y
fig = plt.figure() #figure 对象
ax = Axes3D(fig) #Axes3D 对象
X,Y = np.mgrid[-2:2:40j, -2:2:40j]# 取样并作满射联合
Z = Fun(X, Y) # 取样点 Z 坐标打表
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="rainbow")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# 梯度下降
step = 0.0008 # 取步长
x = 0
y = 0
tag_x = [x]
tag_y = [y]
tag_z = [Fun(x, y)] # 三个坐标分别打入表中，该表用于绘制点
new_x = x
new_y = y
Over = False
while Over == False:
  new_x -= step * PxFun(x, y)
  new_y -= step * PyFun(x, y)
  if Fun(x, y) - Fun(new_x, new_y) < 7e-9:
    Over = True
  x = new_x # 更新旧点
  y = new_y 
  tag_x.append(x)
  tag_y.append(y)
  tag_z.append(Fun(x, y)) # 新点三个坐标打入表中
ax.plot(tag_x,tag_y,tag_z,'r')
plt.title('(x,y)~(' + str(x) + "," + str(y) + ')')
plt.show()
