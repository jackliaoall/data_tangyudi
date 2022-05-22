# 将字符串编码，直接替换字符串
# dict 字符和次数的字典
# codes 赫夫曼编码
def toStrByte(src,dict,codes):
   # 编码字符串
   for kv in dict.items():
      src = src.replace(kv[0], codes[kv[0]])
   return src
