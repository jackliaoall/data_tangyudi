def index(src,c):
   for i in range(len(src)):
      if src[i]==c:
         return i
   return -1

if __name__ == '__main__':
   i = index("abcdefg","e")
   print(i)
