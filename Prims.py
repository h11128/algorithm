from collections import defaultdict
# adjacency list
import sys
import math
import time

class Graph1:
    def __init__(self):
        self.graph = defaultdict(list)
        self.edge = {}
    def addEdge(self,u,v,w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.edge[u,v] = w
        self.edge[v,u] = w

    def Prims(self):
        start_time = time.clock()
        g1 = Graph1()
        g1.cost = len(self.graph) *[math.inf]
        g1.graph[0].append(0)
        result = []
        while len(g1.graph) < len(g.graph):
            e = self.addvertice(g1)
            result.append("%d, %d:%d\n"%(e[0],e[1],e[2]))
        print(result)
        print("--- %s seconds ---" % (time.clock() - start_time))
        return g1

    def addvertice(self,g1):
        min = math.inf
        e = (0,0,0)
        for u in g1.graph:
            g1.cost[u] = 0
            for i in self.graph[u]:
                if i in g1.graph:
                    continue
                if g1.cost[i] > g1.cost[u] + self.edge[u,i]:
                    #print("with edge (%d,%d), g1.cost[%d] update from %f to %d"%(u,i,i,g1.cost[i],g1.cost[u] + self.edge[u,i]))
                    g1.cost[i] = g1.cost[u] + self.edge[u,i]
                if g1.cost[i] < min:
                    min = g1.cost[i]
                    e = [u,i,self.edge[u,i]]

        print("add edge: ",e)
        g1.addEdge(e[0],e[1],e[2])
        return e




g = Graph1()
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


g1 = g.Prims()
