'''
冒泡排序算法优化_2
'''
def bubbleSort(nums):
   r = range(0, len(nums) - 1)
   #外层for循环控制要比较的轮数,共需要执行"长度-1"次
   for i in range(0,len(nums)-1):
      #设置标记
      sorted = True
      #内层for循环控制每轮要比较的次数，共需要执行"长度-已执行的轮数-1"次
      for j in r:
         print("第%d轮第%d次"%(i+1,j+1),end="\t")
         #如果当前数字比后面一个数字大，则需要交换位置
         if nums[j]>nums[j+1]:
            print("%d和%d交换位置"%(nums[j],nums[j+1]),end="")
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
            #发生位置交换，说明排序未结束
            sorted = False
            #记录下最后一次交换的位置
            lastChange = j
         else:
            print("%d比%d小，不交换位置"%(nums[j],nums[j+1]),end="")
         print(nums)
      print("第%d轮排序结果:" % (i + 1), nums)
      #判断本轮是否有位置交换
      if sorted:
         return
      print("最后是交换位置是：",lastChange)
      #改变下一轮比较的范围
      r = range(0,lastChange)

#排序前的列表
nums = [1,3,2,4,5,6]
print("排序前：", nums)
#调用排序冒泡排序函数
bubbleSort(nums)
print("排序后：", nums)
