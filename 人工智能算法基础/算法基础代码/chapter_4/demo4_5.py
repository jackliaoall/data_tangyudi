'''
双向循环链表
'''
class Node():
   def __init__(self,value):
      #节点数据
      self.value = value
      #next指针指向下一个节点
      self.next = None
      # pre指针指向下一个节点
      self.pre = None
   def __str__(self):
      return self.value

   # 遍历节点
   def eachAfter(self):
      # node默认指向当前节点
      node = self
      # 循环遍历
      while node is not None:
         # 打印节点
         print(node)
         # 取出下一个节点
         node = node.next

   # 遍历节点
   def eachBefore(self):
      # node默认指向当前节点
      node = self
      # 循环遍历
      while node is not None:
         # 打印节点
         print(node)
         # 取出上一个节点
         node = node.pre

#将传入的列表转为单向循环链表
def toRecycleList(strs):
   #记录上一个节点
   pre = None
   #遍历列表
   for i in range(len(strs)):
      #创建节点
      node = Node(strs[i])
      #pre不为None，说明不是第0次
      if pre!=None:
         #将上一个节点的下一个节点指向当节点
         pre.next = node
         node.pre = pre
      else:
         #是第0次，存储head节点
         head = node
      #将上一个节点替换为当前节点
      pre = node
      #最后一个节点
      if i == len(strs)-1:
         #将最后一个节点的下一个节点指向head节点
         node.next = head
         #head节点的上一个指向最后一个节点
         head.pre = node
   return head
if __name__ == '__main__':
   head = toRecycleList(['aa','bb','cc','dd','ee'])
   #因为是循环链表，所以会无限循环
   # head.eachAfter()
   head.eachBefore()
