#右旋转
def rightRotate(self,node):
   #获取左子节点
   temp = node.leftNode
   # 将左子节点的右子节点给当前节点的左节点
   node.leftNode = temp.rightNode
   # 将当前节点设置为左子节点的右子节点
   temp.rightNode = node
   #修改节点的高度
   node.height = max(self.height(node.right), self.height(node.left)) + 1
   temp.height = max(self.height(temp.left), node.height) + 1
   return temp
