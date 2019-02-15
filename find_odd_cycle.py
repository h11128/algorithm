from collections import defaultdict
# adjacency list
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.s = []
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def dfs(self,v,visited):
        self.s.append(v)
        if visited[v] == 0:
            visited[v] = 1
        for i in self.graph[v]:
            if visited[i] == 0:
                visited[i] = -visited[v]
                print("visited[",i,"]=","-visited[",v,"]=",visited[i])
                print(visited)
                self.dfs(i,visited)
            if visited[i] == visited[v]:
                print ("Find odd-cycle")
            if self.s[0] == self.s[i] and v!= self.s[i+1] and len(self.s)>1:
                print("cycle:",self.s)
                self.s = []
    def dfs2(self,v,visited,parent):
        visited[v] = 1
        for i in self.graph[v]:
            if visited[i] == 0:
                if self.dfs2(i,visited,v):
                    return True
            elif i != parent and visited[i] == visited[v] :
                return True
        return False
    def isCyclic(self):
        visited = [0]*(self.num)
        for v in range(self.num):
            if visited[v] ==0:
                if self.dfs2(v,visited,-1):
                    return True
        return False
    def dfs1(self,v,visited):
        visited[v] = 1
        print(visited)
        for i in self.graph[v]:
            if visited[i] == 0:
                self.dfs1(i,visited)

            if visited[i] == visited[v]:
                return ("Find odd-cycle")

    def blank(self):
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

g.blank()
print(g.graph)
