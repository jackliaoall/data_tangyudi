'''
朴素算法
src:原字符串
dst:目标子串
'''
def index(src,dst):
   #分别获取长度
   m = len(src)
   n = len(dst)
   #遍历下标到m-n+1,m-n+1后面不用再遍历了，因为长度不够了
   for i in range(m - n + 1):
      #若相同
      if src[i:i + n] == dst:
         #返回下标
         return i
   #未找到，返回-1
   return -1

src = "ps:str is short for string"
dst = "string"
print(index(src,dst))
