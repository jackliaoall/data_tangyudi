'''
节点类
'''
class Node():
   def __init__(self,value):
      self.value = value
      self.leftNode = None
      self.rightNode = None

   def __str__(self):
      return str(self.value)

'''
二叉树类
'''
class BinaryTree():
   def __init__(self,node):
      self.root = node

   #前序遍历
   def frontIterate(self):
      self.front(self.root)

   #前序遍历的递归方法
   def front(self,node):
      #结束递归条件
      if node is None:
         return
      #当前节点值
      print(node,end = '\t')
      #左子树递归
      self.front(node.leftNode)
      #右子树递归
      self.front(node.rightNode)

   #中序遍历
   def midIterate(self):
      self.mid(self.root)

   #中序遍历的递归方法
   def mid(self,node):
      #结束递归条件
      if node is None:
         return
      #左子树递归
      self.mid(node.leftNode)
      #当前节点值
      print(node,end = '\t')
      #右子树递归
      self.mid(node.rightNode)

   #后序遍历
   def lastIterate(self):
      self.last(self.root)

   #后序遍历的递归方法
   def last(self,node):
      #结束递归条件
      if node is None:
         return
      #左子树递归
      self.last(node.leftNode)
      #右子树递归
      self.last(node.rightNode)
      # 当前节点值
      print(node,end = '\t')

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
   #创建树
   t1 = BinaryTree(n1)
   #前序遍历
   t1.frontIterate()
   #中序遍历
   t1.midIterate()
   #后序遍历
   t1.lastIterate()
