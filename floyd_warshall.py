from collections import defaultdict
# adjacency list
import numpy as np

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.edges = {}
        self.len = 0
    def addEdge(self,u,v,w):
        self.graph[u].append(v)
        self.edges[u,v] = w
        if self.len < max(u,v):
            self.len = max(u,v) + 1

    def inialdist(self):
        dist = np.zeros((g.len,g.len),dtype=np.int32)
        dist.fill(100)
        for i in range(g.len):
            dist[i,i] = 0
        for i in range(self.len):
            for v in self.graph[i]:
                if self.edges[i,v]:
                    dist[i,v] = self.edges[i,v]
        return dist

    def floyd(self,dist):
        for k in range(self.len):
            for i in range(self.len):
                for j in range(self.len):
                    if dist[i,j]>dist[i][k]+dist[k][j]:
                        #print("update distance(%d,%d) to dist(%d,%d)+dist(%d,%d) = %d"%(i,j,i,k,k,j,dist[i][k]+dist[k][j]))
                        dist[i,j] = dist[i][k]+dist[k][j]

g = Graph()
g.addEdge(0,1,1)
g.addEdge(1,2,2)
g.addEdge(2,3,3)
g.addEdge(3,4,4)
g.addEdge(4,5,5)
g.addEdge(5,0,6)
print(g.graph)
print(g.edges)
dist = g.inialdist()
print(dist)
g.floyd(dist)
print(dist)
