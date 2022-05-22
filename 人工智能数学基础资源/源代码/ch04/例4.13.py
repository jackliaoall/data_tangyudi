def fsin(x): # 自定义函数 fsin(x)
   m=20
   sum=0.0
   for i in range(1,m+1):
      n=2*i-1
      temp1,temp2,temp3=1,1,1
      for j in range(1,i):
        temp1=-temp1
      for j in range(1,n+1):
        temp2=temp2*x
        temp3=temp3*j
      sum=sum+temp1*temp2/temp3
   return sum
#调用 sumpy 库中 sin 函数和自定义的 f x sin ( ) ，验证结果。

from numpy import *
for x in range (-20,20):
    print (sin(x))
    print (fsin(x))
    