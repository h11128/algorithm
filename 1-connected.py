from collections import defaultdict
# adjacency list
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.len = 0
        self.lst = []
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.len = v + 1
    def dfs(self,v,visited):
        visited[v] = 1
        for i in self.graph[v]:
            if visited[i] == 0:
                self.dfs(i,visited)
        self.lst.append(v)

    def isallpath(self):
        visited = [0]*(self.len)
        for v in range(self.len):
            if visited[v] == 0:
                self.dfs(v,visited)
        lst = self.lst
        print(lst)
        for i in range(len(lst)-1):
            if not lst[i+1] in self.graph[lst[i]]:
                if not lst[i] in self.graph[lst[i+1]]:
                    print("point",lst[i],"is not connected to point",lst[i+1])
                    print("Not a all path graph")
                    break

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(2,3)
g.addEdge(4,0)
g.addEdge(3,4)
g.addEdge(1,4)
print(g.graph)

g.isallpath()
