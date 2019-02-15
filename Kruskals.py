from collections import defaultdict
# adjacency list
import heapq
import re
import sys
import time

class Graph:
    def __init__(self):
        self.heap = []
        self.graph = defaultdict(list)

    def addEdge(self,u,v,w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.num = len(self.graph)
        heapq.heappush(self.heap, (w,[u,v]))

    def connected(self,v,visited,u):
        if (not u in self.graph) or (not v in self.graph):
            return False
        visited[v] = 1
        for i in self.graph[v]:
            if i == u:
                return True
            if visited[i] == 0:
                if self.connected(i,visited,u):
                    return True
        return False

    def addTreeEdge(self,u,v,w):
        visited = [0]*(self.num)
        if self.connected(u,visited,v):
            return False
        else:
            self.graph[u].append(v)
            self.graph[v].append(u)
            return True

    def removemin(self):
        return (heapq.heappop(self.heap))


def Kruskals(g):
    start_time = time.clock()
    g1 = Graph()
    g1.num = g.num
    result = []
    while(len(g.heap) != 0 and len(g1.graph) < g1.num ):
        e = g.removemin()
        if g1.addTreeEdge(e[1][0],e[1][1],e[0]):
            #print("add edge (v%d,v%d) = %d to MST"%(e[1][0],e[1][1],e[0]))
            result.append("%d, %d:%d\n"%(e[1][0],e[1][1],e[0]))
    return g1
    print("--- %s seconds ---" % (time.clock() - start_time))


g = Graph()
g.addEdge(0,1,814)
g.addEdge(0,2,735)
g.addEdge(1,2,702)
g.addEdge(0,3,818)
g.addEdge(1,3,885)
g.addEdge(2,3,153)
g.addEdge(0,4,818)
g.addEdge(1,4,353)
g.addEdge(2,4,507)
g.addEdge(3,4,55)

g1 = Kruskals(g)
print(g1.graph)
