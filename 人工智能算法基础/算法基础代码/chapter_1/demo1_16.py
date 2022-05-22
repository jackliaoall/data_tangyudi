'''
归并操作
'''
def merge(left,right):
   #记录下标
   r, l=0, 0
   #新列表
   temp=[]
   #循环归并
   while l<len(left) and r<len(right):
      #若左边列表中的数更小
      if left[l] <= right[r]:
         #将左边列表中的数存入新列表中
         temp.append(left[l])
         #下标+1
         l += 1
      #右边列表中的数更小
      else:
         # 将右边列表中的数存入新列表中
         temp.append(right[r])
         # 下标+1
         r += 1
   #处理多余的数据
   temp += left[l:]
   temp += right[r:]
   return temp
'''
归并排序
'''
def mergeSort(nums):
   #结束递归条件，若只有一个数，不再递归
   if len(nums) <= 1:
      return nums
   #将列表分为两部分
   num = len(nums) // 2
   #左边部分
   left = mergeSort(nums[:num])
   #右边部分
   right = mergeSort(nums[num:])
   #递归处理
   return merge(left, right)
#待排序序列
list = [7,4,8,5,2,0,1,9,3,6]
#排序前
print(list)
#堆排序
list = mergeSort(list)
#排序后
print(list)
