#赫夫曼树的节点
class Node():
   def __init__(self,weigh,value=None,leftNode=None,rightNode=None):
      # 权值
      self.weigh = weigh
      # 节点的值，用于存储节点对应的字符
      self.value = value
      self.leftNode = leftNode
      self.rightNode = rightNode

# 生成赫夫曼树，返回根节点
# dict是字符及出现次数的字典
def getHuffmanTreeRoot(dict):
   nodes = []
   # 将字典中的键值对依次弹出并创建节点存入nodes中
   for kv in dict.items():
      # 弹了一个键值对
      # 创建节点，添加节点
      nodes.append(Node(kv[1],kv[0]))
   while len(nodes)>1:
      #排序
      nodes.sort(key=lambda x:x.weigh,reverse=True)
      #弹出两个权值最小节点
      n1 = nodes.pop()
      n2 = nodes.pop()
      n3 = Node(n1.weigh+n2.weigh,None,n1,n2)
      nodes.append(n3)
   return nodes[0]

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

# 将字符串编码，直接替换字符串
# dict 字符和次数的字典
# codes 赫夫曼编码
def toStrByte(src,dict,codes):
   # 编码字符串
   for kv in dict.items():
      src = src.replace(kv[0], codes[kv[0]])
   return src

# 将二进制字符串转为字符数组
def bitstring_to_bytes(s):
   v = int(s, 2)
   b = bytearray()
   while v:
      b.append(v & 0xff)
      v >>= 8
   return bytes(b[::-1])

# 将数字转为对应的8位的二进制的字符串，如6-->'00000110'
def numToBitStr(num):
   s = ''
   while num:
      num, j = num // 2, num % 2
      s += str(j)
   # 不足8位加0
   for x in range(8 - len(s)):
      s += '0'
   # 倒置
   s = s[::-1]
   return s

#将字符串的二进制补齐8的倍数位、标记添加位数、转为byte数组
def toByte(strByte):
   # 获取最后字节的二进制位数
   l = 8-len(strByte)%8
   # 添加8-l个0,例如最后字节有2个位，则添加8-2=6个0
   for i in range(l):
      strByte+='0'
   # 计算l的二进制字符串
   s = numToBitStr(l)
   #将生成的二进制添加到最后
   strByte+=s
   #转为byte数组
   return bitstring_to_bytes(strByte)

#压缩字符串
def zipString(src):
   dict = {}
   # 统计出现次数
   for c in src:
      dict[c] = src.count(c)
   # 生成赫夫曼树
   root = getHuffmanTreeRoot(dict)
   # 生成赫夫曼编码
   codes = getHuffmanCodes(root)
   # 编码为二进制的字符串
   strByte = toStrByte(src,dict,codes)
   # 返回字节数组和赫夫曼编码
   return (toByte(strByte),codes)

# 解压缩字符串，bytearray为压缩后的字节数组
def unzip(bytearray,codes):
   # 取出最后一位的数字
   count = bytearray[len(bytearray)-1]
   string = ''
   # 将传入的字节数组转为二进制的字符串
   for b in bytearray:
      string+=numToBitStr(b)
   # 后面的count+8不要了
   string = string[:len(string)-(count+8)]
   # 将赫夫曼编码的键值换一下，方便找出对应的字符，原来的键是字符，值是编码，换为键是编码，值是字符
   dict = {}
   for kv in codes.items():
      dict[kv[1]]=kv[0]
   s = ''
   # 遍历二进制字符串，还原原字符串
   i,j = 0,1
   while i+j<=len(string):
      # 取出编码
      code = string[i:i+j]
      # 编码存在
      if code in dict:
         s+=dict[code]
         i+=j
         j=1
      # 编码不存在,j+1后再一次循环判断
      else:
         j+=1
   return s

if __name__ == '__main__':
   src = 'can you can a can as a can canner can a can?'
   # 压缩字符串，获取字符数组和编码
   bs,codes = zipString(src)
   print(bs)
   # 解压缩
   string = unzip(bs,codes)
   print(string)
