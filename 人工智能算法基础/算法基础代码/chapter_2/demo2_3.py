'''
插值查找
nums 目标序列
value 要查找的目标值
'''
def insertSearch(nums,value):
   #初始化最低索引，最高索引
   low,high = 0,len(nums)-1
   #计算中间索引
   mid = low+int((value-nums[low])/(nums[high]-nums[low])*(high-low))
   count = 1
   #循环处理
   while low<high:
      print(f'第{count}次查找')
      count+=1
      #若相同，返回下标值
      if nums[mid]==value:
         return mid
      #中间元素大于目标值，序列为升序。
      elif nums[mid]>value:
         #将中间索引-1设置为最高索引，下次查找左边
         high = mid-1
      # 中间元素小于目标值，序列为升序。
      else:
         # 将中间索引+1设置为最低索引，下次查找右边
         low = mid+1
      #重新计算中间索引
      mid = low+int((value-nums[low])/(nums[high]-nums[low])*(high-low))

list = [0,1,12,45,66,67,69,73,79,89,92,100]
print(insertSearch(list,1))
