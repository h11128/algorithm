from collections import defaultdict
# adjacency list
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def dfs(self,v,visited):
        visited[v] = 1
        for i in self.graph[v]:
            if visited[i] == 0:
                self.dfs(i,visited)

    def mainfunction(self):
        visited = [0]*(len(self.graph))
        for v in range(len(self.graph)):
            if visited[v] ==0:
                self.dfs(v,visited)

g = Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(3,4)

g.mainfunction()
print(g.graph)
