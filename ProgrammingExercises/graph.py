class Graph:
    def __init__(self, n):
        self.n = n
        self.neighbors = [ [] for i in range(n) ]

    def add_edge(self, a, b):
        self.neighbors[a].append(b)
        self.neighbors[b].append(a)

    def __repr__(self):
        return "Graph " + repr(self.neighbors)

    def DFS(self, cur_vertex, visited_vertices):
        visited_vertices.append(cur_vertex)
        self.visited[cur_vertex] = True
        for x in self.neighbors[cur_vertex]:
            if not self.visited[x]:
                self.DFS(x, visited_vertices)

    def connected_components(self):
        self.visited = [ False for i in range(self.n) ]
        result = []
        for i in range(self.n):
            if not self.visited[i]:
                cc = []
                self.DFS(i, cc)
                result.append(cc)
        return result
