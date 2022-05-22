'''
快速排序
nums:待排序列表
start-end:待排序区间
'''
def quickSort(nums,start,end):
   #如果开始位置和结束位置相同，说明只有一个数，不需要排序
   if start < end:
      #取出标准数
      standard = nums[start]
      #记录下左右下标
      low = start
      high = end
      #两下标未重合，就循环
      while low<high:
         #右下标向左寻找小于标准数的数,使用大于判断，循环结束，表示找到了小于标准数的数
         while low<high and nums[high]>=standard:
            high-=1
         #将寻找到的数存入左下标所在位置
         nums[low]=nums[high]
         #左下标向右寻找大于标准数的数
         while low<high and nums[low]<standard:
            low+=1
         #将寻找到的数存入右下标所在位置
         nums[high]=nums[low]
      #将标准数存入两下标重合处
      nums[low]=standard
      #递归处理小于等于标准数部分
      quickSort(nums,start,low)
      #递归处理大于标准数部分
      quickSort(nums,low+1,end)
#待排序列表
list = [6,7,4,8,3,1,5,2]
#快速排序
quickSort(list,0,len(list)-1)
#输出结果
print(list)
