class Node():
   def __init__(self,value):
      #节点数据
      self.value = value
      #next指针指向下一个节点
      self.next = None
   def __str__(self):
      return self.value
