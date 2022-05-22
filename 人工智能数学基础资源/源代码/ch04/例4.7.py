from numpy import *

def f(n):
  sum1=1
  m=0
  if n==0:
   sum1=1
  else:
   m=n+1 # 因为 range 函数是左闭右开，所以用 m 来控制循环次数
  for i in range(1,m):
   sum2=1.0
   k=i+1 # 因为 range 函数是左闭右开，所以用 k 来控制循环次数
   for j in range(1,k):
      sum2=sum2*j
   sum1=sum1+1.0/sum2
  return sum1
print (f(0))   #输出结果 1
print (f(1))   #输出结果 2.0
print (f(2))   #输出结果 2.5
print (f(3))   #输出结果 2.6666666666666665
print (f(10))   #输出结果 2.7182818011463845
