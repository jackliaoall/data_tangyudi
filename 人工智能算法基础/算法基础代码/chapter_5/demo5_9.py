#节点类
class Node():
   def __init__(self, value):
      #节点值
      self.value = value
      #左子节点
      self.leftNode = None
      #右子节点
      self.rightNode = None
      #当前节点的高度
      self.height = 0

#平衡二叉树
class AVLTree():
   def __init__(self):
      self.root = None

   #获取节点的高度
   def height(self, node):
      if node is None:
         return -1
      else:
         return node.height

   # 右旋转
   def rightRotate(self, node):
      # 获取左子节点
      temp = node.leftNode
      # 将左子节点的右子节点给当前节点的左节点
      node.leftNode = temp.rightNode
      # 将当前节点设置为左子节点的右子节点
      temp.rightNode = node
      # 修改节点的高度
      node.height = max(self.height(node.right), self.height(node.left)) + 1
      temp.height = max(self.height(temp.left), node.height) + 1
      return temp

   #左旋转
   def leftRotate(self, node):
      #获取当前节点的右子节点
      temp = node.rightNode
      #将右子节点的左子节点设为当前节点的右子节点
      node.rightNode = temp.leftNode
      #将当前节点设为右子节点的左子节点
      temp.leftNode = node
      #修改节点的高度
      node.height = max(self.height(node.right), self.height(node.left)) + 1
      temp.height = max(self.height(temp.right), node.height) + 1
      return temp

   #先左旋转再右旋转
   def leftRightRotate(self, node):
      #先将左子节点进行左旋转
      node.leftNode = self.leftRotate(node.leftNode)
      #再将当前节点进行右旋转
      return self.rightRotate(node)

   #先右旋转再左旋转
   def rightLeftRotate(self, node):
      #先将右子节点进行右旋转
      node.rightNode = self.rightRotate(node.rightNode)
      #再奖当前节点进行左旋转
      return self.leftRotate(node)

   # 添加节点
   def add(self, value):
      #若根节点不存在
      if not self.root:
         #添加为根节点
         self.root = Node(value)
      #向树中添加节点
      else:
         self.root = self._add(value, self.root)

   #添加节点
   def _add(self, value, node):
      #若传入的value小于node
      if value < node.value:
         #向左递归添加
         node.left = self._add(value, node.left)
         #若不平衡
         if (self.height(node.left) - self.height(node.right)) == 2:
            #向左添加后引起不平衡需要右旋转
            if value < node.left.value:
               #单次右旋转
               node = self.rightRotate(node)
            else:
               #先左旋转，再右旋转
               node = self.leftRightRotate(node)
      #若大于node的value
      elif value > node.value:
         #向右递归添加
         node.right = self._add(value, node.right)
         if (self.height(node.right) - self.height(node.left)) == 2:
            #向右添加引起的不平衡需要向左旋转
            if value < node.right.value:
               #单次左旋转
               node = self.leftRotate(node)
            else:
               #先右旋转后再左旋转
               node = self.rightLeftRotate(node)
      #重新计算高度
      node.height = max(self.height(node.right), self.height(node.left)) + 1
      return node
