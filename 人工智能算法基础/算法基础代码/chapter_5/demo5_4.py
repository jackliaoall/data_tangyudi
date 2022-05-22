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
二叉查找树类
'''
class BSTree():
   #根据传入的列表创建二叉树
   def __init__(self,data):
      if data == []:
         return
      #初始化根节点
      self.root = Node(data[0])
      #循环插入节点
      for i in data[1:]:
         self.add(i)

   #插入节点
   def add(self,value):
      #temp默认指向根节点
      temp = self.root
      #循环找位置
      while True:
         #若比temp更大且右子节点不为空，则temp指向右子节点
         if value > temp.value and temp.rightNode is not None:
            temp = temp.rightNode
         #若比temp更小且左子节点不为空，则temp指向左子节点
         elif value < temp.value and temp.leftNode is not None:
            temp = temp.leftNode
         #若比temp更大且右子节点为空，则插入为右子节点，循环结束
         elif value > temp.value and temp.rightNode is None:
            temp.rightNode = Node(value)
            break
         # 若比temp更小且左子节点为空，则插入为左子节点，循环结束
         elif value < temp.value and temp.leftNode is None:
            temp.leftNode = Node(value)
            break

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

if __name__ == '__main__':
   t1 = BSTree([6,3,1,8,9,7,2,5])
   t1.midIterate()
