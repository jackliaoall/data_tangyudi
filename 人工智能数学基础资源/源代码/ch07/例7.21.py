from random import *
counter, times = 0, int(1e4)
for i in range(times):
    if len({randint(1,365) for i in range(50)}) != 50: # 存在同一天生日的人
        counter += 1
print('在 50 个人中有相同生日的概率为：',counter/times)
