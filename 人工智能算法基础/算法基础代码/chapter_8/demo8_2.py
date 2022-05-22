'''
顶点
'''
class Vertex:
   def __init__(self,value):
      # 顶点值（关键字）
      self.value = value

'''
邻接链表存储的图结构
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
