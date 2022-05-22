'''
kmp算法
src原字符串
dst子串
'''
def kmp(src, dst):
   #获取部分匹配表
   steps = getSteps(dst)
   #获取两个串的长度
   n = len(src)
   m = len(dst)
   #初始下标
   i, j = 0, 0
   while (i < n) and (j < m):
      #若相同，继续向后匹配
      if (src[i] == dst[j]):
         i += 1
         j += 1
      #根据部分匹配表决定j向后移动的位数
      elif (j != 0):
         j = steps[j - 1]
      else:
         i += 1
   #若相同，返回下标
   if (j == m):
      return i - j
   else:
      return -1

'''
生成部分匹配表
'''
def getSteps(dst):
   #index初始值为0，用于记录最长匹配长度
   index, m = 0, len(dst)
   #用于存储部分匹配表，默认值是0
   steps = [0] * m
   #从第1个字符开始向后遍历
   for i in range(1,m):
      #若当前遍历字符和index的字符样同,
      if (dst[i] == dst[index]):
         #index+1为当前的长度
         steps[i] = index + 1
         #然后index+1
         index += 1
      #若当前遍历字符和index的字符不相同，且index不为0
      elif (index != 0):
         #index的前一个值-1
         index = steps[index - 1]
      #字符不匹配，且index值为0，则当前匹配长度为0
      else:
         steps[i] = 0
   return steps

print(kmp('byte bye-by bye-bye','bye-byt'))
