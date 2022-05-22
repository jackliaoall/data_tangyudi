'''
插入排序
'''
def insertSort(nums):
   #从第1个位置开始向后遍历
   for i in range(1,len(nums)):
      #将第i个数存入临时变量中
      temp = nums[i]
      #变量j用于记录和临时变量比较的位置，从i的前一个位置开始比较
      j = i-1
      #若j未超范围且第j个元素大于临时变量中的值
      while j>=0 and nums[j]>temp:
         #将第j个元素向后移动一个位置
         nums[j+1]=nums[j]
         #j-1，向前比较
         j-=1
      #将临时变量存入最后一个未移动的位置的后一个位置
      nums[j+1]=temp
#待排序的序列
list = [7,4,3,8,0,4,3,5,1,6]
#进行插入排序
insertSort(list)
#输出排序后的序列
print(list)
