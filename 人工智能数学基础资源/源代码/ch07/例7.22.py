from functools import reduce
#定义参数，input_Prob:3个硬币抛出正面的概率，正面记为H，反面记为T
input_Prob = {1:0.3, 2:0.5, 3:0.7}
H = 49
T = 31
p=0
#估计可能性最大的硬币
def Max_Prob():
    max_prob = -1
    max_person =1
    for  key in input_Prob:
        current_prob=Prob(input_Prob[key])
        print('第%d个硬币的概率%10.3f' % (key, current_prob))
        if current_prob>max_prob:     #比较概率值
            max_prob=current_prob
            max_person=key
    print('选中第%d个硬币的概率最大%10.3f' % (max_person,max_prob))
#根据命中率p,求概率值
def Prob(p):
    f1 = Factorial(H + T) / (Factorial(H) * Factorial(T))
    f2 = (p **H) * ((1.0 - p) **T)
    return f1 * f2
#求x的阶乘
def Factorial(x):
    return reduce(lambda x, y: x * y, range(1, x + 1))
if __name__ == '__main__':
    Max_Prob ()
