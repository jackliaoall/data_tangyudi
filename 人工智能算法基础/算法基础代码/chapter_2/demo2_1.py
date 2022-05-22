'''
线性查找
nums 目标序列
value 要查找的目标值
'''
def lineSearch(nums,value):
   #遍历所有下标
   for i in range(0,len(nums)):
      #若值匹配
      if nums[i]==value:
         #返回下标
         return i
   #若遍历完未找到匹配元素，返回-1
   return -1
