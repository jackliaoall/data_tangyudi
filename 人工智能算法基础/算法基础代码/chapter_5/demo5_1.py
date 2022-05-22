'''
节点类
'''
class Node():
   def __init__(self,value):
      self.value = value
      self.leftNode = None
      self.rightNode = None

if __name__ == '__main__':
   #创建1节点
   n1 = Node(1)
   #创建3节点
   n3 = Node(3)
   #将3节点设置为1节点的右子节点
   n1.rightNode = n3
   #创建6节点和7节点
   n6 = Node(6)
   n7 = Node(7)
   #将3节点的左子节点设置为6节点
   n3.leftNode = n6
   #将3节点的右子节点设置为7节点
   n3.rightNode = n7
