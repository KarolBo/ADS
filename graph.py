from collections import deque

# class Vertex:
#     def __init__(self, val):
#         self.val = val
#         self.pred = None

class Graph:
    def __init__(self, graph, repr):
        self.graph = graph
        self.repr = repr

    def DFS_iter(self, u):
        q = deque([u])
        visited = set()
        while q:
            u = q.popleft()
            visited.add(u)
            print(u, end=' ')
            for v in self.graph[u]:
                if v not in visited:
                    q.append(v)
        print()

    def DFS_rec(self, q=None, visited=None, source=None):
        if visited is None:
            visited = set()
        if not q:
            if source is not None:
                q = deque([source])
            else:
                print()
                return
        u = q.popleft()
        visited.add(u)
        print(u, end=' ')
        for v in self.graph[u]:
            if v not in visited:
                q.append(v)
        self.DFS_rec(q, visited)


########################################################

graph = [[2], [3], [1, 4], [0, 4, 5], [], []]
my_graph = Graph(graph, 'adj_list')
my_graph.DFS_iter(0)
my_graph.DFS_rec(source=0)