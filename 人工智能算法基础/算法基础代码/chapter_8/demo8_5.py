# 请自行下协numpy模块
import numpy as np

# 求已经确定的顶点集合与未选顶点集合中的最小边
def min_edge(select, candidate, graph):
    # 记录最小边权重
    min_weight = np.inf
    # 记录最小边
    v, u = 0, 0
    # 循环扫描已选顶点与未选顶点，寻找最小边
    for i in select:
        for j in candidate:
            # 如果存在比当前的最小边权重还小的边，则记录
            if min_weight > graph[i][j]:
                min_weight = graph[i][j]
                v, u = i, j
    # 返回记录的最小边的两个顶点
    return v, u


# prim算法
def prim(graph):
    # 顶点个数
    vertex_num = len(graph)
    # 存储已选顶点，初始化时可随机选择一个起点
    select = [0]
    # 存储未选顶点
    candidate = list(range(1, vertex_num))
    # 存储每次搜索到的最小生成树的边
    edge = []
    # 由于连接n个顶点需要n-1条边，故进行n-1次循环，以找到足够的边
    for i in range(1, vertex_num):
        # 调用函数寻找当前最小边
        v, u = min_edge(select, candidate, graph)
        # 添加到最小生成树边的集合中
        edge.append((v, u))
        # v是select中的顶点，u为candidate中的顶点，故将u加入candidate，以代表已经选择该顶点
        select.append(u)
        # 同时将u从candidate中删除
        candidate.remove(u)
    # 统计总权重
    sum = 0
    for x in edge:
        sum+=graph[x[0]][x[1]]
    return edge,sum

if __name__ == '__main__':
    # 为简单起见，这里的图以简单的嵌套列表来存储
    # 即索引0：A  1:B ……
    graph = [[np.inf, 3, 2, np.inf, np.inf, np.inf,5],
                  [3, np.inf, 3, 4, 8, 6,6],
                  [2, 3, np.inf, 6, np.inf, np.inf,np.inf],
                  [np.inf, 4, 6, np.inf, np.inf,9, np.inf],
                  [np.inf, 8, np.inf, np.inf, np.inf, 12],
                  [np.inf, 8, np.inf, np.inf, np.inf, 12,9],
                  [np.inf, 6, np.inf, 9, 12, np.inf,np.inf]]
    p = prim(graph)
