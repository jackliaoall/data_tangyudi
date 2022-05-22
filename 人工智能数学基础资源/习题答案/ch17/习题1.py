import numpy as np
import matplotlib.pyplot as plt
import pymc3 as pm
if __name__ == '__main__':
    # 生成观察数据
    np.random.seed(123)

    alpha=1
    beta =[1, 2.5]
    se=1
    N=100

    X1=np.random.randn(N)
    X2=np.random.randn(N)
    Y=alpha + beta[0]*X1 + beta[1]*X2 + np.random.randn(N)*se

    #定义模型
    basic_model = pm.Model()
    with basic_model:
        alpha = pm.Normal('alpha', mu=0, sd=10)
        beta = pm.Normal('beta', mu=0, sd=10, shape=2)
        se = pm.HalfNormal('se', sd=1)

        mu = alpha + beta[0] * X1 + beta[1] * X2

        Y_obs = pm.Normal('Y_obs', mu=mu, sd=se, observed=Y)
    # 模型拟合
    with basic_model:
        # 用MAP获得初始点
        start = pm.find_MAP(model=basic_model)
        # 实例化采样器
        step = pm.Slice(vars=[se])
        # 对后验分布进行5000次采样
        trace = pm.sample(5000, step=step,start=start)
    #显示估计值
    print(pm.summary(trace))
