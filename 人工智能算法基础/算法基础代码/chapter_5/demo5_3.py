'''
节点类
'''
class Node():
   def __init__(self,value):
      self.value = value
      self.leftNode = None
      self.rightNode = None
      self.leftType = 0
      self.rightType = 0

   def __str__(self):
      return str(self.value)

if __name__ == '__main__':
   #创建节点
   n1,n2,n3,n4,n5,n6,n7 = Node(1),Node(2),Node(3),Node(4),Node(5),Node(6),Node(7)
   #产生关系
   n1.leftNode = n2
   n1.rightNode = n3
   n2.leftNode = n4
   n2.rightNode = n5
   n3.leftNode = n6
   n3.rightNode = n7
   #线索化二叉树
   #改变标记
   n4.leftType,n4.rightType,n5.leftType,n5.rightType,n6.leftType,n6.rightType,n7.leftType,n7.rightType=1,1,1,1,1,1,1,1
   #4节点的右指针指向2节点
   n4.rightNode = n2
   #5节点的左指针指向2节点，右指针指向1节点
   n5.leftNode,n5.rightNode = n2,n1
   #6节点的左指针指向1节点，右指针指向3节点
   n6.leftNode, n6.rightNode = n1, n3
   #7节点的左指针指向n3
   n7.leftNode = n3
