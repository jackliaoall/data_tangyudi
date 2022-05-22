'''
拓扑排序
'''
def topSort(graph):
   # 创建入度字典
   inDegrees = {}
   for u in graph:
      inDegrees[u]=0
   # 获取每个节点的入度
   for u in graph:
      for v in graph[u]:
         inDegrees[v] += 1
   # 使用列表作为队列并将入度为0的添加到队列中
   q = []
   for u in graph:
      if inDegrees[u]==0:
         q.append(u)
   res = []
   # 当队列中有元素时执行
   while q:
      # 从队列首部取出元素
      u = q.pop(0)
      # 将取出的元素存入结果中
      res.append(u)
      # 移除与取出元素相关的指向，即将所有与取出元素相关的元素的入度减少1
      for v in graph[u]:
         inDegrees[v] -= 1
         # 若被移除指向的元素入度为0，则添加到队列中
         if inDegrees[v] == 0:
            q.append(v)
   return res
if __name__ == '__main__':
   # 定义图结构
   graph = {
      "A": ["B", "F", "G"],
      "B": [],
      "C": ["A", "D"],
      "D": ["F"],
      "E": [],
      "F": ["E"],
      "G": ["E", "J"],
      "H": ["G"],
      "I": ["H"],
      "J": ["K", "L", "M"],
      "K": [],
      "L": ["M"],
      "M": []
   }
   top = topSort(graph)
   print(top)
