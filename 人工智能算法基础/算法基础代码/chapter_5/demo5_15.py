# 根据传入的赫夫曼树生成赫夫曼编码
def getHuffmanCodes(root):
   return __getHuffmanCodes(root,'')

def __getHuffmanCodes(root,code):
   #结束递归条件
   if root is None:
      return
   #用于存储结果的字典
   dict = {}
   # 在原来的code的基础上加上0后向左递归
   c1 = code+'0'
   d1 = __getHuffmanCodes(root.leftNode,c1)
   if d1:
      # 把递归生成的编码存入dict中
      dict.update(d1)
   c2 = code+'1'
   # 在原来的code的基础上加上1后向右递归
   d2 = __getHuffmanCodes(root.rightNode,c2)
   if d2:
      dict.update(d2)
   # 如果是叶节点
   if root.leftNode is None and root.rightNode is None:
      # 将code存入dict中
      dict[root.value] = code
   return dict
