'''
二分查找
nums 目标序列
value 要查找的目标值
'''
def binarySearch(nums,value):
   #初始化最低索引，中间索引，最高索引
   low,mid,high = 0,len(nums)//2,len(nums)-1
   #循环处理
   while low<high:
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
      mid = (high-low)//2+low

list = [0,1,2,3,4,5,6,7,8,9,10]
print(binarySearch(list,5))
