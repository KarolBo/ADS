from collections import deque
import heapq
from multiprocessing import heap

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

    def kruskal_mst(self):
        n = len(self.graph)
        tree_sets = [set([u]) for u in range(n)]
        mst = []
        edges = set()
        for u in range(n):
            for v, w in self.graph[u]:
                if (v, u, w) not in edges:
                    edges.add( (u, v, w) )
        edges = list(edges)
        edges.sort(key=lambda x: x[2])
        for u, v, w in edges:
            if tree_sets[u] != tree_sets[v]:
                union = tree_sets[u].union(tree_sets[v])
                for x in union:
                    tree_sets[x] = union
                mst.append((u, v, w))
        return mst

    def prim_mst(self):
        q = []
        tree_nodes = set()
        mst = []
        u = 0
        while len(mst) < len(self.graph) - 1:
            for i, (v, w) in enumerate(self.graph[u]):
                if v in tree_nodes:
                    continue
                heapq.heappush(q, (w, i, u, v))
            w, i, u, v = heapq.heappop(q)
            if v in tree_nodes:
                continue
            mst.append((u, v, w))
            tree_nodes.add(u)
            tree_nodes.add(v)
            u = v
        return mst

    def bellman_ford(self, s):
        n = len(self.graph)
        distances = n * [float('inf')]
        predecesors = n * [None]
        distances[s] = 0
        edges = []
        for u in range(n):
            for v, w in self.graph[u]:
                edges.append((u, v, w))
                
        for _ in range(n-1):
            for u, v, w in edges:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    predecesors[v] = u

        # check for negative cycles
        for u, v, w in edges:
            if distances[u] + w < distances[v]:
                print('negative cycle detected')
                return None, None
        return distances, predecesors

    def dijkstra(self, s):
        q = [(0, 0, s)]
        distances = len(self.graph) * [float('inf')]
        distances[s] = 0
        predecesors = len(self.graph) * [None]
        while q:
            _, _, u = heapq.heappop(q)
            for i, (v, w) in enumerate(self.graph[u]):
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    predecesors[v] = u
                    heapq.heappush(q, (distances[u] + w, i, v))
        return distances, predecesors

    @classmethod
    def print_path(cls, u, pred):
        if pred[u] is None:
            print(u, end='')
            return
        cls.print_path(pred[u], pred)
        print(' ->', u, end='')

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
# graph = [[1], [2, 4, 5], [3, 6], [2, 7], [0, 5], [6], [5, 7], [7]]
# my_graph = Graph(graph, 'adj_list')
# scc = my_graph.stronglyConnectedComponents()
# print(scc)

# Minimum spanning tree
# graph = [[(1, 4), (7, 8)], 
#          [(0, 4), (2, 8), (7, 11)], 
#          [(1, 8), (8, 2), (5, 4), (3, 7)], 
#          [(2, 7), (4, 9), (5, 14)], 
#          [(3, 9), (5, 10)], 
#          [(6, 2), (2, 4), (3, 14), (4, 10)], 
#          [(7, 1), (8, 6), (5, 2)], 
#          [(0, 8), (1, 11), (8, 7), (6, 1)], 
#          [(7, 7), (2, 2), (6, 6)]]
# my_graph = Graph(graph, 'adj_list')
# mst1 = my_graph.kruskal_mst()
# mst2 = my_graph.prim_mst()
# for edge1 in mst1:
#     print(edge1[0]+1, '->', edge1[1]+1, edge1[2])
# print()
# for edge2 in mst2:
#     print(edge2[0]+1, '->', edge2[1]+1, edge2[2])

# Shortest path
graph = [[(1, 6), (3, 7)], [(2, 5), (3, 8), (4, 4)], [(1, 2)], [(4, 9), (2, 3)], [(2, 7), (0, 2)]]
my_graph = Graph(graph, 'adj_list')
dist, pred = my_graph.bellman_ford(0)
print(dist)
my_graph.print_path(4, pred)
print()
dist, pred = my_graph.dijkstra(0)
print(dist)
my_graph.print_path(4, pred)