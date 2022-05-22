'''
邻接矩阵存储的图
'''
class Graph:
   # 创建图结构
   def __init__(self,v):
      self.v = v
      # 邻接矩阵
      self.adjMatrix=[]
      # 初始化邻接矩阵
      for x in v:
         m = []
         for y in v:
            if x==y:
               m.append(1)
            else:
               m.append(0)
         self.adjMatrix.append(m)

   # 添加邻接关系
   def addEdge(self,v1,v2):
      index1 = self.v.index(v1)
      index2 = self.v.index(v2)
      self.adjMatrix[index1][index2] = 1
      self.adjMatrix[index2][index1] = 1

if __name__ == '__main__':
   v = ['a','b','c','d','e','f']
   g = Graph(v)
   g.addEdge('a', 'b')
   g.addEdge('b', 'c')
   g.addEdge('b', 'd')
   g.addEdge('b', 'e')
   g.addEdge('d', 'e')
   g.addEdge('a', 'f')
