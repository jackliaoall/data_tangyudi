'''
调整某一个子树最大顶堆
parent 需要调整为大顶堆的父节点索引
'''
def maxHeap(nums,size,parent):
   #获取parent的左子节点
   leftNode = 2*parent+1
   # 获取parent的右子节点
   rightNode = 2 * parent + 2
   #默认父节点最大
   max = parent
   #依次判断左子节点和右子节点，找到最大数的索引
   if leftNode<size and nums[max]<nums[leftNode]:
      max = leftNode
   if rightNode<size and nums[max]<nums[rightNode]:
      max = rightNode
   #若最大的在判断完以后不再是父节点，说明最大的节点是左子节点或右子节点
   #则需要交换位置
   if max!=parent:
      temp = nums[parent]
      nums[parent] = nums[max]
      nums[max] = temp
      #递归处理交换后的子树
      maxHeap(nums,size,max)

'''
堆排序
'''
def heapSort(nums):
   last = len(nums)-1
   #获取最后一个元素的父节点索引
   parent = last//2-1 if last%2==0 else last//2
   #从最后一个父节点向前依次调整
   while parent>=0:
      maxHeap(nums,len(nums),parent)
      parent-=1
   #遍历区间，i是需要调整为大顶堆的最后一个位置，依次减小
   i = last
   while i>0:
      #交换位置堆顶元素和堆中最后一个元素
      temp = nums[0]
      nums[0] = nums[i]
      nums[i] = temp
      #重新将第0个位置调为大顶堆,i-1是最后要调整的位置，所以i作为size直接传入。
      maxHeap(nums,i,0)
      i-=1
#待排序序列
list = [7,4,8,5,2,0,1,9,3,6]
#排序前
print(list)
#堆排序
heapSort(list)
#排序后
print(list)
