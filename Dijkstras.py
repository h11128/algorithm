from collections import defaultdict
# adjacency list
import sys
import math
import time

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.edge = {}

    def addEdge(self,u,v,w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.edge[u,v] = w
        self.edge[v,u] = w

    def Dijkstras(self,source):
        start_time = time.clock()
        g1 = Graph1()
        g1.distance = len(self.graph) *[math.inf]
        g1.distance[source] = 0
        g1.parent = len(self.graph) *[-1]
        g1.parent[source] = source
        g1.graph[source].append(source)
        g1.cost = defaultdict(list)
        g1.cost[source] = 0

        for i in range(1,len(self.graph)):
            g1.cost[i] = math.inf


        result = []
        while len(g1.graph) < len(g.graph):
            e = self.addvertice(g1)
            if e:
                result.append("%d, %d:%d\n"%(e[0],e[1],e[2]))
        print(result)
        print("--- %s seconds ---" % (time.clock() - start_time))
        return g1

    def addvertice(self,g1):
        # don't need to go through all g1 to update cost
        vj =  min(g1.cost, key = g1.cost.get)
        dist = g1.cost.pop(vj)
        if (vj,g1.parent[vj]) in self.edge:
            g1.addEdge(vj,g1.parent[vj],self.edge[vj,g1.parent[vj]])
            e = (vj,g1.parent[vj],self.edge[vj,g1.parent[vj]])
        else: e = False
        for i in self.graph[vj]:
            if i in g1.graph:
                continue
            if i in g1.cost and g1.distance[i] > g1.distance[vj] + self.edge[vj,i]:
                #print("with edge (%d,%d), g1.distance[%d] update from %f to %d"%(u,i,i,g1.distance[i],g1.distance[u] + self.edge[u,i]))
                g1.distance[i] = g1.distance[vj] + self.edge[vj,i]
                g1.parent[i] = vj
                g1.cost[i] = g1.distance[i]
        return e

class Graph1:
    def __init__(self):
        self.graph = defaultdict(list)
        self.edge = {}
    def addEdge(self,u,v,w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.edge[u,v] = w
        self.edge[v,u] = w

    def Dijkstras(self,source):
        start_time = time.clock()
        g1 = Graph1()
        g1.cost = len(self.graph) *[math.inf]
        g1.parent = len(self.graph) *[0]
        g1.cost[source] = 0
        g1.parent[source] = source
        g1.graph[source].append(source)
        result = []
        while len(g1.graph) < len(g.graph):
            e = self.addvertice(g1)
            result.append("%d, %d:%d\n"%(e[0],e[1],e[2]))
        print(result)
        print("--- %s seconds ---" % (time.clock() - start_time))
        return g1

    def addvertice(self,g1):
        min = math.inf
        e = (0,0,0,0)
        # go through all g1,update cost and find min
        for u in g1.graph:
            for i in self.graph[u]:
                if i in g1.graph:
                    continue
                if g1.cost[i] > g1.cost[u] + self.edge[u,i]:
                    #print("with edge (%d,%d), g1.cost[%d] update from %f to %d"%(u,i,i,g1.cost[i],g1.cost[u] + self.edge[u,i]))
                    g1.cost[i] = g1.cost[u] + self.edge[u,i]
                    g1.parent[i] = u
                if g1.cost[i] < min:
                    min = g1.cost[i]
                    e = [g1.parent[i],i,self.edge[g1.parent[i],i],min]
                    #print("now e is ",e)
        g1.addEdge(e[0],e[1],e[2])

        #print("add edge: ",e,"\n")

        return e




g = Graph()
g.addEdge(0,1,7)
g.addEdge(0,5,8)
g.addEdge(1,5,2)
g.addEdge(5,6,7)
g.addEdge(5,4,9)
g.addEdge(4,6,1)
g.addEdge(1,4,11)
g.addEdge(1,2,6)
g.addEdge(2,3,5)
g.addEdge(3,4,3)
g.addEdge(3,7,8)
g.addEdge(4,7,5)
g.addEdge(6,7,7)


g1 = g.Dijkstras(0)
print(g1.parent)
print(g1.graph)
