'''
2-3树节点类
'''
class Node(object):
   def __init__(self, value):
      # 左值
      self.value1 = value
      # 右值
      self.value2 = None
      # 左子节点
      self.leftNode = None
      # 中间子节点
      self.middleNode = None
      # 右子节点
      self.rightNode = None

   # 判断是否是叶节点
   def isLeaf(self):
      return self.leftNode is None and self.middleNode is None and self.rightNode is None

   # 节点是否满了，默认情况下从左向右排列，即，如果是二节点，使用leftNode和middleNode指针
   def isFull(self):
      return self.value2 is not None

   # 根据给定的值获取子节点
   def getChild(self, value):
      # 给定的值比左值更小
      if value < self.value1:
         return self.leftNode
      # 右值为空
      elif self.value2 is None:
         return self.middleNode
      # 右值不为空且比右小
      elif value < self.value2:
         return self.middleNode
      # 比右值大
      else:
         return self.rightNode

'''
2-3树
'''
class Tree():
   def __init__(self,list):
      self.root = None
      for i in list:
         self.put(i)

   # 添加
   def put(self, value):
      # 根节点为空
      if self.root is None:
         self.root = Node(value)
      else:

         pvalue, pRef = self._put(self.root, value)
         if pvalue is not None:
            newnode = Node(pvalue)
            newnode.leftNode = self.root
            newnode.middleNode = pRef
            self.root = newnode

   # 从node处开始寻找位置并插入值
   def _put(self, node, value):
      # node是叶节点
      if node.isLeaf():
         return self._addtoNode(node, value, None)
      else:
         # 获取子节点
         child = node.getChild(value)
         # 递归处理
         pvalue, pRef = self._put(child, value)
         if pvalue is None:
            return None, None
         else:
            return self._addtoNode(node, pvalue, pRef)

   # 将值添加到该节点
   def _addtoNode(self, node, value, pRef):
      # 节点已满
      if node.isFull():
         return self._splitNode(node, value, pRef)
      else:
         # 给定值小于左值
         if value < node.value1:
            # 直接存入左值位置，原数据存为右值
            node.value2 = node.value1
            node.value1 = value
            # 将中间子节点换为右子节点，然后中间子节点设置为拆分出来的新节点
            if pRef is not None:
               node.rightNode = node.middleNode
               node.middleNode = pRef
         else:
            # 将给定值存为右值
            node.value2 = value
            # 新节点为右子节点
            if pRef is not None:
               node.rightNode = pRef
         return None, None

   # 向上拆分
   def _splitNode(self, node, value, pRef):
      # 创建新节点
      newnode = Node(None)
      # 若给定值小于左值
      if value < node.value1:
         # 取出左值
         pvalue = node.value1
         # 将给定值存为左值
         node.value1 = value
         # 将右值给新节点
         newnode.value1 = node.value2
         if pRef is not None:
            newnode.leftNode = node.middleNode
            newnode.middleNode = node.rightNode
            node.middleNode = pRef
      # 给定值小于右值
      elif value < node.value2:
         pvalue = value
         newnode.value1 = node.value2
         if pRef is not None:
            newnode.leftNode = pRef
            newnode.middleNode = node.rightNode
      # 给定值大于右值
      else:
         pvalue = node.value2
         newnode.value1 = value
         if pRef is not None:
            newnode.leftNode = node.rightNode
            newnode.middleNode = pRef
      node.value2 = None
      return pvalue, newnode

if __name__ == '__main__':
   list = [7,6,2,4,8,9,1,3,5]
   t1 = Tree(list)
   print(t1)
