import random
def coin_trial(): #模拟扔10次硬币
    heads=0   # heads:正面朝上的次数
    for i in range(10):
        if random.random()<=0.5:  #如果随机数小于 0.5，认为正面向上
            heads +=1
    return  heads
def simulate(n):
    trials=[]
    for i in range(n):  # n次扔硬币实验
        trials.append(coin_trial())
    return(sum(trials)/n)
