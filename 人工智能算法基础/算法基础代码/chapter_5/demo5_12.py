#k-d树的节点
class Node():
   def __init__(self, point = None, split = None, leftNode = None, rightNode = None):
      #节点值
      self.point = point
      self.leftNode = leftNode
      self.rightNode = rightNode
      #划分维度，当前节点是通过哪一个维度来划分的
      self.split = split

   def __str__(self):
      return str(self.point)

class KDTree():
   def __init__(self,list):
      self.dimension = len(list[0])
      self.root = self.createKDTree(Node(),list,0)

   # 创建k-d树
   # n 层数
   def createKDTree(self,root,list,n):
      #获取长度
      length = len(list)
      if length == 0:
         return
      # 通过层数计算划分维度
      split = n%self.dimension
      #排序
      data_list = sorted(list, key = lambda x : x[split])
      #获取中间点
      point = data_list[length//2]
      #创建节点
      root = Node(point,split)
      #递归创建左子树
      root.leftNode = self.createKDTree(root.leftNode, data_list[0:int(length / 2)],n+1)
      #递归创建右子树
      root.rightNode = self.createKDTree(root.rightNode, data_list[int(length / 2) + 1 : length],n+1)
      return root

   #用于计算维度距离
   def computerDistance(self,pt1, pt2):
      sum = 0.0
      for i in range(len(pt1)):
         sum = sum + (pt1[i] - pt2[i]) ** 2
      return sum ** 0.5

   '''
   KNN算法
   query目标点
   k数量
   '''
   def KNN(self,query,k):
      # 存储最近的k个点
      node_K = []
      # k个点到目标点的距离
      node_dist = []
      # 存储回溯的父节点
      nodeList = []
      #从根节点出发
      temp_root = self.root
      while temp_root:
         #保存所有访问过的父节点
         nodeList.append(temp_root)
         # 计算距离
         dist = self.computerDistance(query,temp_root.point)
         # 若不足K个，直接添加
         if len(node_K) < k:
            node_dist.append(dist)
            node_K.append(temp_root.point)
         else :
            # 获取最大距离
            max_dist = max(node_dist)
            # 区距离小于已存储的最大距离
            if dist < max_dist:
               #获取最大距离的下标
               index = node_dist.index(max_dist)
               #删除
               del(node_K[index])
               del(node_dist[index])
               # 添加
               node_dist.append(dist)
               node_K.append(temp_root.point)
         split = temp_root.split
         #找到最靠近的叶子节点
         if query[split] <= temp_root.point[split]:
            temp_root = temp_root.leftNode
         else:
            temp_root = temp_root.rightNode
      #回溯访问父节点，另一个父节点的子节点中可能有更近的
      while nodeList:
         back_point = nodeList.pop()
         split = back_point.split
         max_dist = max(node_dist)
         #若满足进入该父节点的另外一个子节点的条件
         if len(node_K) < k or abs(query[split] - back_point.point[split]) < max_dist:
            #进入另外一个子节点
            if query[split] <= back_point.point[split]:
               temp_root = back_point.rightNode
            else:
               temp_root = back_point.leftNode
            # 若不为空
            if temp_root:
               nodeList.append(temp_root)
               #计算距离
               curDist = self.computerDistance(temp_root.point,query)
               # 若最大距离大于当前距离
               if max_dist > curDist and len(node_K) == k:
                  #删除原有的
                  index = node_dist.index(max_dist)
                  del(node_K[index])
                  del(node_dist[index])
                  #添加新的
                  node_dist.append(curDist)
                  node_K.append(temp_root.point)
               # 不足K个时直接添加
               elif len(node_K) < k:
                  node_dist.append(curDist)
                  node_K.append(temp_root.point)
      # 返回搜索到的点和距离
      return node_K+node_dist

list = [(3, 2), (7, 3), (4, 6), (5, 7), (8, 9), (11, 5), (12, 8), (13, 1), (14, 4), (14, 10)]
tree = KDTree(list)
r = tree.KNN((13,6),3)
print(r)
