# 左旋转
def leftRotate(self, node):
   # 获取当前节点的右子节点
   temp = node.right
   # 将右子节点的左子节点设为当前节点的右子节点
   node.right = temp.left
   # 将当前节点设为右子节点的左子节点
   temp.left = node
   # 修改节点的高度
   node.height = max(self.height(node.right), self.height(node.left)) + 1
   temp.height = max(self.height(temp.right), node.height) + 1
   return temp
