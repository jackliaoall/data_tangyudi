class Node():
   def __init__(self,value):
      #节点数据
      self.value = value
      #next指针指向下一个节点
      self.next = None
      #pre指针指向上一下节点
      self.pre = None
   def __str__(self):
      return self.value

   #添加下一个节点
   def nextNode(self,nextNode):
      #当前节点指向下一个节点
      self.next = nextNode
      #传入的下一个节点的上一个节点指向当前节点
      nextNode.pre = self
      #返回下一个节点
      return nextNode

   #向后遍历节点
   def eachAfter(self):
      #node默认指向当前节点
      node = self
      #循环遍历
      while node is not None:
         #打印节点
         print(node)
         #取出下一个节点
         node = node.next
   #向前遍历节点
   def eachPre(self):
      node = self
      while node is not None:
         print(node)
         node = node.pre

if __name__ == '__main__':
   n1 = Node("aa")
   n2 = Node("bb")
   n3 = Node("cc")
   n4 = Node("dd")
   n5 = Node("ee")
   #依次添加节点
   n1.nextNode(n2).nextNode(n3).nextNode(n4).nextNode(n5)
   #向后遍历节点
   n3.eachAfter()
   #向前遍历节点
   n3.eachPre()
