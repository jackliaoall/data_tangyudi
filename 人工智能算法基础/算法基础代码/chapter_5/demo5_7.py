# 先左旋转再右旋转
def leftRightRotate(self, node):
   # 先将左子节点进行左旋转
   node.leftNode = self.leftRotate(node.leftNode)
   # 再将当前节点进行右旋转
   return self.rightRotate(node)
