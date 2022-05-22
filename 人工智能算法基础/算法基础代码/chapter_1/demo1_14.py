'''
希尔排序
'''
def shellSort(nums):
   #初始步长
   step = len(nums)//2
   #遍历所有步长
   while step>0:
      #---以下是插入排序的步骤，只是只需要排本组内的元素---
      #从每一组的第2个元素开始遍历，所以初始值为第1组的第2个元素，即step值。
      #本例中共10个元素，步长为10//2=5
      #即第0个元素7和第5个元素0为第一组。则第1组中的第2个元素为下标为5个元素0
      for i in range(step,len(nums)):
         #临时变量用于存储第i个数
         temp = nums[i]
         #从本组中的前一个位置开始比较，下标为i-step
         j = i - step
         #遍历本组中前面所有的元素，若本组中前面的元素更大
         while j>=0 and nums[j]>temp:
            #前面的元素向后移动一个步长
            nums[j+step] = nums[j]
            #改变下标，遍历本组中的前一个元素
            j-=step
         #上面的循环结束以后，说明有一个更小的数，则将临时变量存入j的组中的后一个元素，即j+step
         nums[j+step] = temp
      #改变步长的值
      step//=2
#待排序序列
list = [7,4,8,5,2,0,1,9,3,6]
#输出待排序序列
print(list)
#排序
shellSort(list)
#输出排序后序列
print(list)
