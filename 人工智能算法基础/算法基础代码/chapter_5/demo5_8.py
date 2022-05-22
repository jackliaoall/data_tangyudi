# 先右旋转再左旋转
def rightLeftRotate(self, node):
   # 先将右子节点进行右旋转
   node.rightNode = self.rightRotate(node.rightNode)
   # 再奖当前节点进行左旋转
   return self.leftRotate(node)
