import numpy as np
import matplotlib.pyplot as plt

#载入数据
X=np.array([[1,3,3],
           [1,4,3],
           [1,1,1],
           [1,0,2]])
#标签
Y=np.array([[1],
           [1],
           [-1],
           [-1]])
#权值初始化 ，3个输入，1个输出，3行1列，取值范围-1~1,本身取值范围为0~1
W=(np.random.random([3,1])-0.5)*2
print(W)

#设置学习率
lr=0.11
#神经网络输出
O=1

#权值更新
def update():
    global X,Y,W,lr
    O=np.sign(np.dot(X,W))
    W_C=lr*(X.T.dot(Y-O))/int(X.shape[0])
    W=W+W_C


for i in range(100):
    update()  # 更新权值
    print(W)  # 打印权值
    print(i)  # 打印当前迭代次数
    O = np.sign(np.dot(X, W))  # 计算当前输出
    if (O == Y).all():
        print("Finished")
        print("epoch:", i)
        break

# 正样本
x1 = [3, 4]
y1 = [3, 3]
# 负样本
x2 = [1, 0]
y2 = [1, 2]

# 计算分界线的斜率以及截距
k = -W[1] / W[2]
d = -W[0] / W[2]
print('k=', k)
print('d=', d)

xdata = (0, 5)

plt.figure()
plt.plot(xdata, xdata * k + d, 'r')
plt.scatter(x1, y1, c='b')
plt.scatter(x2, y2, c='r')
plt.show()
