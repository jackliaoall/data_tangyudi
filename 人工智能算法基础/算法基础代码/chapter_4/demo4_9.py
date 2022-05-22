class Node():
   def __init__(self,value):
      #节点数据
      self.value = value
      #next指针指向下一个节点
      self.next = None
   def __str__(self):
      return self.value

   # 遍历节点
   def each(self):
      # node默认指向当前节点
      node = self
      # 循环遍历
      while node is not None:
         # 打印节点
         print(node)
         # 取出下一个节点
         node = node.next

#将传入的列表转为单向循环链表
def toRecycleSingleList(strs):
   #记录上一个节点
   pre = None
   #遍历列表
   for i in range(len(strs)):
      #创建节点
      node = Node(strs[i])
      #pre不为None，说明不是第0次
      if pre!=None:
         #将上一个节点的下一个节点指向当节点
         pre.next = node
      else:
         #是第0次，存储head节点
         head = node
      #将上一个节点替换为当前节点
      pre = node
      #最后一个节点
      if i == len(strs)-1:
         #将最后一个节点的下一个节点指向head节点
         node.next = head
   return head

def countAndKill(node):
   i = 1
   #存储父节点
   parent = None
   #存储当前节点，用于遍历
   cur = node
   #下一个节点的下一个节点不是自己，说明还有超过2个节点，继续循环
   while cur.next.next is not cur:
      #输出数数情况
      print(f'{cur.value}数{i}')
      #若数到3
      if i==3:
         #父节点的下一个节点指向当前节点的下一个节点，当前节点被删除
         parent.next = cur.next
         #输出
         print(f'{cur.value}被杀死')
      i+=1
      #将父节点修改为当前节点
      parent = cur
      #将当前节点修改为下一个节点继续下一次循环
      cur = cur.next
      if i==4:
         i=1
   #输出最后剩下的两个节点
   print(cur,cur.next)
if __name__ == '__main__':
   nums = []
   #生成1-41的列表
   for i in range(41):
      nums.append(f"{i+1}")
   #转为循环链表
   head = toRecycleSingleList(nums)
   #开始游戏
   countAndKill(head)
