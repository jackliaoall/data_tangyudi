'''
直接选择排序
'''
def selectSort(nums):
   #遍历列表，将第i个看成最小的数
   for i in range(0,len(nums)):
      #记录未排序中最小的数的下标，初始值是当前遍历的下标
      minIndex=i
      #循环向后找
      for j in range(i+1,len(nums)):
         #如果找到一个比已经记录的最小数下标的数还小的数
         if nums[j]<nums[minIndex]:
            #修改最小数的下标
            minIndex=j
      #若最小数下标不是当前遍历的下标，说明后面有更小的数
      if minIndex!=i:
         #交换位置
         temp = nums[minIndex]
         nums[minIndex]=nums[i]
         nums[i]=temp
#待排序序列
list = [3,5,1,8,6,9,7,0,2]
#选择排序
selectSort(list)
#输出排序后的结果
print(list)
