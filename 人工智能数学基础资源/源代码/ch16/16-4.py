#16-4.py
#散点图观察
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./datasets/ch1ex1.csv')
points = df.values

plt.figure(figsize=(10,6),dpi=80)

xs = points[:,0]
ys = points[:,1]

plt.scatter(xs, ys)
plt.show()
