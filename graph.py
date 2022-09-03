from collections import deque
from logging.config import valid_ident

# class Vertex:
#     def __init__(self, val):
#         self.val = val
#         self.pred = None

class Graph:
    def __init__(self, graph, repr):
        self.graph = graph
        self.repr = repr

    def BFS_iter(self, u):
        q = deque([u])
        visited = set([u])
        while q:
            u = q.popleft()
            print(u, end=' ')
            for v in self.graph[u]:
                if v not in visited:
                    q.append(v)
                    visited.add(v)
        print()

    def BFS_rec(self, q=None, visited=None, source=None):
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
        self.BFS_rec(q, visited)

    def DFS_iter(self, u):
        stack = [u]
        visited = set([u])
        while stack:
            u = stack.pop()
            print(u, end=' ')
            for v in reversed(self.graph[u]):
                if v not in visited:
                    stack.append(v)
                    visited.add(v)
        print()

    def DFS_rec(self, u, visited=None):
        if not visited:
            visited = set()
        visited.add(u)
        print(u, end=' ')
        for v in self.graph[u]:
            if v not in visited:
                self.DFS_rec(v, visited)

    def hasCycles(self):
        for u in range(len(self.graph)):
            visited = set([u])
            stack = [u]
            while stack:
                u = stack.pop()
                for v in self.graph[u]:
                    if v in visited:
                        print(f'{u} -> {v}')
                        return True
                    visited.add(v)
                    stack.append(v)
                visited.remove(u)
        return False

    def topologicalSort(self, force=False):
        if not force and self.hasCycles():
            print('The graph is not a DAG')
            return
        sorted_vertices = []
        visited = set()
        for u in range(len(self.graph)):
            if u in visited:
                continue
            visited.add(u)
            self._topologicalSort_rec(u, sorted_vertices, visited)
        return reversed(sorted_vertices)

    def _topologicalSort_rec(self, u, sorted_vertices, visited):
        for v in self.graph[u]:
            if v in visited:
                continue
            visited.add(v)
            self._topologicalSort_rec(v, sorted_vertices, visited)
        sorted_vertices.append(u)

    def stronglyConnectedComponents(self):
        top_sort = self.topologicalSort(force=True)
        transposed = self.getTransposition()
        scc = {}
        visited = set()
        for u in top_sort:
            if u in visited:
                continue
            scc[u] = self.getDFSTree(transposed, u, visited)
        return scc

    def getTransposition(self):
        n = len(self.graph)
        transposed = [[] for _ in range(n)]
        for u in range(n):
            for v in self.graph[u]:
                transposed[v].append(u)
        return transposed

    @staticmethod
    def getDFSTree(G, u, visited):
        tree = []
        stack = [u]
        visited.add(u)
        while stack:
            u = stack.pop()
            tree.append(u)
            for v in G[u]:
                if v not in visited:
                    stack.append(v)
                    visited.add(v)
        return tree


########################################################


# Searching
# my_graph.BFS_iter(0)
# my_graph.BFS_rec(source=0)
# my_graph.DFS_iter(0)
# my_graph.DFS_rec(0)

# Topological sort
# graph = [[1, 7], [2, 7], [5], [4], [5], [], [7], [], []]
# my_graph = Graph(graph, 'adj_list')
# cloths = {
#     0: 'pants',
#     1: 'trausers',
#     2: 'belt',
#     3: 'shirt',
#     4: 'tie',
#     5: 'jacket',
#     6: 'socks',
#     7: 'shoes',
#     8: 'watch'
# }
# top_sort = my_graph.topologicalSort()
# print([cloths[v] for v in top_sort])

# Strongly connected components
graph = [[1], [2, 4, 5], [3, 6], [2, 7], [0, 5], [6], [5, 7], [7]]
my_graph = Graph(graph, 'adj_list')
scc = my_graph.stronglyConnectedComponents()
print(scc)