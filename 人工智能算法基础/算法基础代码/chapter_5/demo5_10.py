from enum import Enum

#颜色枚举类
class ColorEnum(Enum):
   RED = "red"
   BLACK = "black"

#节点类
class Node():
   def __init__(self,value):
      self.value = value
      self.leftNode = None
      self.rightNode = None
      #添加parent指针方便向上检查，查找叔叔节点等
      self.parent = None
      #新节点默认为红色
      self.color = ColorEnum.RED

#红黑树
class RBTree():
   # 创建红黑树
   def __init__(self,nums):
      self.root = None
      # 循环添加节点
      for i in nums:
         node = Node(i)
         self.add(node)

   #左旋转
   def leftRotate(self, node):
      # 获取node的右子节点为temp
      temp = node.rightNode
      # 将temp的左子节点设置为node的右子节点
      node.rightNode = temp.leftNode
      # 将temp的左子节点的父节点设置为node
      temp.leftNode.parent = node
      # 将node的父节点设置为temp的父节点
      temp.parent = node.parent
      # 如果node的父节点是空
      if node.parent is None:
         # 将temp设置为根节点
         self.root = temp
      # 如果node是他父节点的左子节点
      elif node == node.parent.leftNode:
         #将temp设置为node的父节点的左子节点
         node.parent.leftNode = temp
      else:
         #否则将temp设置为node的父节点的右子节点
         node.parent.rightNode = temp
      #将node设置为temp的左子节点
      temp.leftNode = node
      # 将node的父节点设为temp
      node.parent = temp

   #右旋转
   def rightRotate(self, node):
      # 获取node的左子节点为temp
      temp = node.leftNode
      # 将temp的右子节点设置为node的左子节点
      node.leftNode = temp.rightNode
      # 将temp的右子节点的父节点设置为node
      temp.rightNode.parent = node
      # 将node的父节点设置为temp的父节点
      node.parent = temp.parent
      # 如果node的父节点为空
      if node.parent is None:
         # 将temp设置为根节点
         self.root = temp
      # 如果node是他父节点的左子节点
      elif node == node.parent.leftNode:
         # 将temp设置为node的父节点的左子节点
         node.parent.leftNode = temp
      else:
         # 将temp设置为node父节点的右子节点
         node.parent.rightNode = temp
      # 将node设置为temp的右子节点
      temp.rightNode = node
      # 将temp设置为node的父节点
      node.parent = temp

   #插入新节点
   def add(self, newNode):
      #用于存储找到的新节点位置的父节点
      newNodeParent = self.root
      #用于遍历节点，从根节点开始遍历
      temp = self.root
      #遍历节点，直到找到空节点
      while temp:
         #修改新节点的父节点的位置为temp
         newNodeParent = temp
         #向下找
         if newNode.value < temp.value:
            temp = temp.leftNode
         else:
            temp = temp.rightNode
      # 将新节点的父节点设置为newNodeParent
      newNode.parent = newNodeParent
      #若新节点的父节点为空，说明root是空的
      if newNodeParent is None:
         #新节点设置为根节点
         self.root = newNode
         #将新节点设置为黑色后结束
         newNode.color = ColorEnum.BLACK
         return
      #根据新节点的值和父节点的值的大小决定位置
      elif newNode.value < newNodeParent.value:
         newNodeParent.leftNode = newNode
      else:
         newNodeParent.rightNode = newNode
      # 插入节点后可能会引起不平衡，需要调整为平衡状态
      self.fixup(newNode)  # 调整二叉树，使其重新为红黑树

   #添加节点后重调整为平衡红黑树
   def fixup(self, node):
      #node最开始指向新节点，所以一定为红色
      #若node的父节点也是红色才需要调整
      while node.parent.color == ColorEnum.RED:
         # 父亲是左子节点
         if node.parent.parent.leftNode == node.parent:
            # 找到叔叔节点
            uncle = node.parent.parent.rightNode
            # 如果叔叔节点是红色
            if uncle.color == ColorEnum.RED:
               # 将node的父节点设置为黑色
               node.parent.color = ColorEnum.BLACK
               # 将node的叔叔节点设置为黑色
               uncle.color = ColorEnum.BLACK
               # 将node的爷爷节点设置为红色
               node.parent.parent.color = ColorEnum.RED
               # 将node的爷爷节点设置为当前节点后向上调整
               node = node.parent.parent
            #叔叔是黑色，且为左右情况，父节点是左子节点，自己是右子节点
            elif uncle.color == ColorEnum.BLACK and node == node.parent.rightNode:
               # 调整为父节点
               node = node.parent
               # 向左旋转，成为左左情况
               self.leftRotate(node)
            # 如果叔叔是黑色，且当前节点是左孩子，即为左左情况
            else:
               # 父亲设置为黑色
               node.parent.color = ColorEnum.BLACK
               # 爷爷设置为红色
               node.parent.parent.color = ColorEnum.RED
               # 将爷爷向右旋转
               self.rightRotate(node.parent.parent)
         # 否则父亲是右子节点，左右对称处理
         else:
            # 获取叔叔节点
            uncle = node.parent.parent.leftNode
            #如果叔叔是红色
            if uncle.color == ColorEnum.RED:
               #父亲变黑
               node.parent.color = ColorEnum.BLACK
               #叔叔变黑
               uncle.color = ColorEnum.BLACK
               #爷爷变红
               node.parent.parent.color = ColorEnum.RED
               #向上检查
               node = node.parent.parent
            # 叔叔是黑色，当前节点是父节点的左孩子，即为右左情况
            elif uncle.color == ColorEnum.BLACK and node == node.parent.leftNode:
               # 调整为父节点
               node = node.parent
               # 向右旋转，成为右右情况
               self.rightRotate(node)
            # # 如果叔叔是黑色，且当前节点是右孩子，即为右右情况
            else:
               #父亲变黑
               node.parent.color = ColorEnum.BLACK
               #爷爷变红
               node.parent.parent.color = ColorEnum.RED
               #爷爷向左转
               self.leftRotate(node.parent.parent)
