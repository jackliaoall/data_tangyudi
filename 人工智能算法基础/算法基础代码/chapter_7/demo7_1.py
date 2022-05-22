# 散列算法
def hash(src):
   PRIME = 31
   x = PRIME
   for i in src:
      x*=ord(i)
   return x

# 二次验证
def equals(s1,s2):
   for i in range(len(s1)):
      if s1[i]!=s2[i]:
         return False
   return True

# Robin-Karp 算法
def RKsearch(src,dst):
   # 遍历下标
   for i in range(len(src)-len(dst)+1):
      # 若散列值相同
      if hash(dst)==hash(src[i:i+len(dst)]):
         # 二次验证
         if equals(dst,src[i:i+len(dst)]):
            return i
   return -1

if __name__ == '__main__':
   i = RKsearch("abcdefg","def")
   print(i)
