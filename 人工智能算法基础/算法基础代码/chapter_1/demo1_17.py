'''
基数排序
'''
def radixSort(nums):
   #获取最大长度
   maxlen = len(str(max(nums)))
   #创建嵌套列表作为队列
   queues = [[] for i in range(0,10)]
   #根据最大长度遍历轮数
   for x in range(1,maxlen+1):
      #遍历所有数
      for num in nums:
         #获取相应位上的数,作为队列的下标
         #str(num)将数字转为字符串
         #str(num)[-x]取出个位，十位，百位 x从1开始增加，-x的值为-1、-2、-3
         #int(str(num)[-x])将取出的字符转为数字
         try:
            queueIndex = int(str(num)[-x])
         #若出异常，说明位数不足，则高位一定为0
         except:
            queueIndex = 0
         #将数字追回到列表中
         queues[queueIndex].append(num)
      #清空列表
      nums.clear()
      #遍历所有队列
      for queue in queues:
         #一次添加所有队列中的元素到原列表中
         nums.extend(queue)
         #清空队列列表
         queue.clear()
#待排序
list = [4,23,12,198,347,11,64,5,49,30,406,92,46,7,58,88,732,996,247,55]
#排序前
print(list)
#基数排序
radixSort(list)
#排序后
print(list)
