class Node():
   def __init__(self,value):
      #节点数据
      self.value = value
      #next指针指向下一个节点
      self.next = None
   def __str__(self):
      return self.value
   #遍历节点
   def each(self):
      #node默认指向当前节点
      node = self
      #循环遍历
      while node is not None:
         #打印节点
         print(node)
         #取出下一个节点
         node = node.next

if __name__ == '__main__':
    n1 = Node("aa")
    n2 = Node("bb")
    n3 = Node("cc")
    n4 = Node("dd")
    n5 = Node("ee")
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
   #从遍历n1节点开始向后遍历
    n1.each()
