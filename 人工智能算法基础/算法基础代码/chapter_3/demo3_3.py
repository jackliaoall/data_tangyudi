'''
在src中从start处向前找上一次字符c出现的位置
'''
def index(src, start,c):
   start-=1
   while start>=0:
      if src[start]==c:
         return start
      start-=1
   return -1

'''
比较两个字符串
'''
def compare(src, dst):
   #记录下标，从后向前比
   l1 = len(src) - 1
   l2 = len(dst) - 1
   #若最后的下标不同，说明长度不同，返回-2
   if l1 != l2:
      return (-2, None)
   #循环比较，从后向前比较
   while l1 >= 0:
      #若某个字符不同，返回该字符的下标及原字符串的不相同的字符
      if src[l1] != dst[l1]:
         return (l1, src[l1])
      l1 -= 1
   #完全相同，返回-3
   return (-3, None)

'''
获取好后缀位置
'''
def searchSuffix(src,suffix):
   i = 0
   l = len(suffix)
   #寻找最长后缀
   while i+l<len(src)-1:
      #找到最长后缀
      if src[i:i+l]==suffix:
         return i
      i+=1
   #若while循环未找到最长后缀
   for i in range(l):
      #判断是否以其他后缀开始
      if src.startswith(suffix[i:]):
         return 0
   #未找到任何后缀
   return -1

'''
bm算法
src原字符串
dst子串、搜索串
'''
def bm(src, dst):
   #目标串长度
   l = len(dst) - 1
   #原字符串长度
   start, end = 0, 0
   #每次循环从原字符串中取出子串长度的字符串进行比较
   while True:
      #计算取子串时结束位置
      end = start + len(dst)
      print(src[start:end])
      #取出子串并比较
      cr = compare(src[start:end], dst)
      #长度不同
      if cr[0] == -2:
         break
      #比较的两个字符串相同，直接返回下标
      if cr[0] == -3:
         return end - l
      #循环处理
      else:
         #获取不相同字符上一次出现的位置
         pos = index(dst, cr[0],cr[1])
         #最后一个字符就不相同
         if cr[0] == (len(dst) - 1):
            #不相同的字符在子串中
            if pos != -1:
               #向后移动坏字符位置-不相同字符在子串的位置
               start += cr[0] - pos
            # 不相同的字符不在子串中
            else:
               # 开始下标直接向后移动子串的长度位
               start += len(dst)
         #中间某个字符不同
         else:
            #坏字符规则
            step1 = cr[0] - pos
            #好后缀规则，获取后缀
            suffix = dst[cr[0]+1:]
            #获取后缀上次出现的位置
            suffixIndex = searchSuffix(dst,suffix)
            #计算移动的位数
            step2 = l - suffixIndex
            #加上两个规则的最大位数
            start += step1 if step1>step2 else step2
   #未找到，返回-1
   return -1

print(bm("here is a simple example", 'example'))
