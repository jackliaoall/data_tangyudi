'''
顶点
'''
class Vertex:
   def __init__(self,value):
      # 顶点值（关键字）
      self.value = value
      # 标记访问状态
      self.visited = False

   def __str__(self):
      return self.value

'''
图
'''
class Graph:
   # 传入顶点集v创建图结构
   def __init__(self,v):
      self.v = v
      # 邻接链表，用于存储邻接关系
      self.e = {}
      # 初始化邻接链表
      for i in v:
         self.e[i]=[]

   # 添加边
   def addEdge(self,v1,v2):
      # 获取顶点
      vertex1 = self.getV(v1)
      vertex2 = self.getV(v2)
      # 添加边
      self.e[vertex1].append(vertex2)
      self.e[vertex2].append(vertex1)

   # 根据关键字获取顶点
   def getV(self,value):
      for i in v:
         if value == i.value:
            return i

   # 深搜
   def dfs(self,v):
      # 若未访问过
      if not v.visited:
         print(v)
         v.visited = True
      # 获取当前节点所有的邻接节点
      chain = self.e.get(v)
      for v1 in chain:
         # 若未访问过，则递归
         if not v1.visited:
            self.dfs(v1)

   # 广搜
   def bfs(self,v):
      # 访问当前节点
      if not v.visited:
         print(v)
         v.visited = True
      # 获取所有邻接节点
      chain = self.e.get(v)
      flag = False
      # 访问所有邻接节点
      for v1 in chain:
         if not v1.visited:
            print(v1)
            v1.visited = True
            # 只要有一个未访问的，就需要递归。若全都访问过了，flag默认为False，不需要继续递归
            flag = True
      if flag:
         # 递归搜索
         for v1 in chain:
            self.bfs(v1)

if __name__ == '__main__':
   # 顶点集
   v = [Vertex('a'), Vertex('b'), Vertex('c'), Vertex('d'), Vertex('e'), Vertex('f')]
   # 创建图
   g = Graph(v)
   # 添加邻接关系
   g.addEdge('a','b')
   g.addEdge('b','c')
   g.addEdge('b','d')
   g.addEdge('b','e')
   g.addEdge('d','e')
   g.addEdge('a','f')
   # 深搜
   # g.dfs(g.getV('a'))
   g.bfs(g.getV('a'))
