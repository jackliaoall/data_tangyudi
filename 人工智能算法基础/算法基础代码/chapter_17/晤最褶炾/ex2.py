import numpy as np
import pylab as pl
from matplotlib import pyplot
from sklearn.datasets import load_digits
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split


# sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# sigmoid函数的一阶导
def dsigmoid(x):
    return x * (1 - x)


class NeuralNetwork:
    def __init__(self, layers):  # (64,100,10)
        # 权值的初始化，范围-1到1
        self.V = np.random.random((layers[0] + 1, layers[1] + 1)) * 2 - 1  # 加的1为偏置值
        self.W = np.random.random((layers[1] + 1, layers[2])) * 2 - 1

    def train(self, X, y, lr=0.11, epochs=10000):
        # 添加偏置
        temp = np.ones([X.shape[0], X.shape[1] + 1])
        temp[:, 0:-1] = X
        X = temp

        for n in range(epochs + 1):
            i = np.random.randint(X.shape[0])  # 随机选取一个数据
            x = [X[i]]
            x = np.atleast_2d(x)  # 转为2维数据

            L1 = sigmoid(np.dot(x, self.V))  # 隐层输出
            L2 = sigmoid(np.dot(L1, self.W))  # 输出层输出

            L2_delta = (y[i] - L2) * dsigmoid(L2)
            L1_delta = L2_delta.dot(self.W.T) * dsigmoid(L1)

            self.W += lr * L1.T.dot(L2_delta)
            self.V += lr * x.T.dot(L1_delta)

            # 每训练1000次预测一次准确率
            if n % 1000 == 0:
                predictions = []
                for j in range(X_test.shape[0]):
                    o = self.predict(X_test[j])
                    predictions.append(np.argmax(o))  # 获取预测结果
                accuracy = np.mean(np.equal(predictions, y_test))
                print('epoch:', n, 'accuracy:', accuracy)

    def predict(self, x):
        # 添加偏置
        temp = np.ones(x.shape[0] + 1)
        temp[0:-1] = x
        x = temp
        x = np.atleast_2d(x)  # 转为2维数据

        L1 = sigmoid(np.dot(x, self.V))  # 隐层输出
        L2 = sigmoid(np.dot(L1, self.W))  # 输出层输出
        return L2


# 查看前30个图像
digits = load_digits()  # 载入数据集
X = digits.data  # 数据
y = digits.target  # 标签
print(digits.data.shape)

# pl.gray()#灰度化图片
# pl.matshow(digits.images[1])
# pl.show()
rows = 3
cols = 10
fig1, ax1 = pyplot.subplots(rows, cols, figsize=(10, 5))

# 标签字体
fontdict = {'fontsize': 20, 'fontweight': 6, 'verticalalignment': 'baseline', 'horizontalalignment': 'center'}
for j in range(rows):
    for i in range(cols):
        ax1[j][i].imshow(digits.images[j * cols + i].reshape(8, 8))
        ax1[j][i].axis('off')
        ax1[j][i].set_title(y[j * cols + i], fontdict=fontdict)

'''
数据归一化的解释：如果数据不做归一化，数据本身的数值太大时，如等于100000时，
该值经过激活函数(如sigmoid函数)后，其值将会无限接近于1，其一阶导数即梯度将无限接近于0，
而数据训练时，权值每次迭代的改变量是和负梯度成正比的，当梯度接近于0时，
权值每次改变都非常小，导致权值无法正常调整，从而导致训练结出来的模型效果很差
'''
# 输入数据归一化
X -= X.min()
X /= X.max()

nm = NeuralNetwork([64, 100, 10])  # 创建网络

X_train, X_test, y_train, y_test = train_test_split(X, y)  # 分割数据1/4为测试数据，3/4为训练数据

# 二值化是指将数字变成计算机易于处理的0和1的方式，如0->1000000000  3->0001000000
labels_train = LabelBinarizer().fit_transform(y_train)  # 标签二值化     0,8,6   0->1000000000  3->0001000000
labels_test = LabelBinarizer().fit_transform(y_test)  # 标签二值化

print('start')

nm.train(X_train, labels_train, epochs=20000)

print('end')