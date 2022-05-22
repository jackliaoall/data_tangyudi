#k-d树的节点
class Node():
   def __init__(self, point = None, split = None, leftNode = None, rightNode = None):
      #节点值
      self.point = point
      self.leftNode = leftNode
      self.rightNode = rightNode
      #划分维度，当前节点是通过哪一个维度来划分的
      self.split = split

   def __str__(self):
      return str(self.point)

class KDTree():
   def __init__(self,list):
      self.dimension = len(list[0])
      self.root = self.createKDTree(Node(),list,0)

   # 创建k-d树
   # n 层数
   def createKDTree(self,root,list,n):
      #获取长度
      length = len(list)
      if length == 0:
         return
      # 通过层数计算划分维度
      split = n%self.dimension
      #排序
      data_list = sorted(list, key = lambda x : x[split])
      #获取中间点
      point = data_list[length//2]
      #创建节点
      root = Node(point,split)
      #递归创建左子树
      root.leftNode = self.createKDTree(root.leftNode, data_list[0:int(length / 2)],n+1)
      #递归创建右子树
      root.rightNode = self.createKDTree(root.rightNode, data_list[int(length / 2) + 1 : length],n+1)
      return root
