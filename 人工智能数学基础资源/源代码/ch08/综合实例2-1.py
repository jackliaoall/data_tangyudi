
import pandas as pd
import matplotlib.pyplot as plt
messages = pd.read_csv('data/QQ_data.csv')  #读取数据
fig = plt.figure(figsize=(12,5))
plt.title('Frequency of QQmessages')
plt.xlabel('Number of QQmessages')
plt.ylabel('Frequency')
plt.hist(messages['numbers'].values,range=[0, 60], bins=60, histtype='stepfilled')
plt.show()
