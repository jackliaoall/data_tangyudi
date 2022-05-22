#赫夫曼树的节点
class Node():
   def __init__(self,weigh,leftNode=None,rightNode=None):
      # 权值
      self.weigh = weigh
      self.leftNode = leftNode
      self.rightNode = rightNode

   def __str__(self):
      return str(self.weigh)

def getHuffmanTreeRoot(list):
   nodes = []
   # 全部转为节点
   for i in list:
      nodes.append(Node(i))
   # 只要节点数量超过1就循环
   while len(nodes)>1:
      # 排序，倒序排序可以直接pop出最小的两个元素
      nodes.sort(key=lambda x:x.weigh,reverse=True)
      # 弹出最小的两个元素 n1<n2
      n1 = nodes.pop()
      n2 = nodes.pop()
      # 创建根节点
      n3 = Node(n1.weigh+n2.weigh,n1,n2)
      #添加回原序列
      nodes.append(n3)
   return nodes[0]
if __name__ == '__main__':
   list = [13,10,23,6,76,18,3,52,80]
   root = getHuffmanTreeRoot(list)
   print(root)
