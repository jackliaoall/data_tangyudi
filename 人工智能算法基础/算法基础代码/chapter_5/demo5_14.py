#赫夫曼树的节点
class Node():
   def __init__(self,weigh,value=None,leftNode=None,rightNode=None):
      # 权值
      self.weigh = weigh
      # 节点的值，用于存储节点对应的字符
      self.value = value
      self.leftNode = leftNode
      self.rightNode = rightNode
