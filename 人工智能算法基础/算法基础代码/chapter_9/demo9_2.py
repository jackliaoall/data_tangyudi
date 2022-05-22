def method(n):
   print(n)
   # 递归条件
   if n>0:
      method(n-1)

if __name__ == '__main__':
   method(10)
