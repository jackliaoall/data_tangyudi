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
