'''
生成一个最后一个数大于num的斐波那契数列
'''
def fib(num):
   list = [1,1,2]
   a,b,c = 1,1,2
   while c<num:
      a = b
      b = c
      c = a + b
      list.append(c)
   return list
'''
斐波那契查找
nums 目标序列
value 要查找的目标值
'''
def fibonacciSearch(nums,value):
   #初始化最低索引，最高索引
   low,high = 0,len(nums)-1
   #初始化
   f = fib(high)
   #初始区间为最后一个区间
   block = len(f)-1
   #计算中间索引
   mid = low + f[block-1] - 1
   #循环处理
   while low<high:
      #若相同，返回下标值
      if nums[mid]==value:
         return mid
      #中间元素大于目标值，序列为升序。
      elif nums[mid]>value:
         #将中间索引-1设置为最高索引，下次查找左边
         high = mid-1
         #减少一个区间
         block -= 1
      # 中间元素小于目标值，序列为升序。
      else:
         # 将中间索引+1设置为最低索引，下次查找右边
         low = mid+1
         #减少两个区间
         block -= 2
      #重新计算中间索引
      mid = low + f[block-1] - 1

list = [1,3,4,7,8,12,19,20,24,27,31,36,40,51,55,67,70]
print(fibonacciSearch(list,19))
