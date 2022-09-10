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
            for v, w in self.graph[u]:
                if v in tree_nodes:
                    continue
                heapq.heappush(q, (w, u, v))
            w, u, v = heapq.heappop(q)
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
        q = [(0, s)]
        distances = len(self.graph) * [float('inf')]
        distances[s] = 0
        predecesors = len(self.graph) * [None]
        while q:
            _, u = heapq.heappop(q)
            for v, w in self.graph[u]:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    predecesors[v] = u
                    heapq.heappush(q, (distances[u] + w, v))
        return distances, predecesors

    @classmethod
    def print_path(cls, u, pred):
        if pred[u] is None:
            print(u, end='')
            return
        cls.print_path(pred[u], pred)
        print(' ->', u, end='')

    def floyd_warshal(self):
        n = len(self.graph)
        if self.repr == 'adj_list':
            D = self.getAdjMat()
        else:
            D = self.graph

        P = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if 0 < D[i][j] < float('inf'):
                    P[i][j] = i 

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if D[i][k] + D[k][j] < D[i][j]:
                        D[i][j] = D[i][k] + D[k][j]
                        P[i][j] = P[k][j]
        return D, P

    def getAdjMat(self):
        n = len(self.graph)
        mat = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j, w in self.graph[i]:
                mat[i][j] = w
        return mat

    def print_path_from(self, u, v, pred_mat):
        pred = pred_mat[u]
        self.print_path(v, pred)
        print()

    def edmonds_karp(self, s, t): # Ford-Fulkerson
        res_net = self.getResNet()
        while True:
            aug_path, c_min = self.getAugPath(res_net, s, t)
            if not aug_path:
                f = 0
                for u in res_net[s]:
                    if u is None:
                        continue
                    f += u[0]
                return f
            for i in range(len(aug_path) - 1):
                u = aug_path[i]
                v = aug_path[i+1]
                res_net[u][v][0] += c_min
                res_net[u][v][1] -= c_min
                res_net[v][u][1] += c_min
        
    def getResNet(self):
        n = len(self.graph)
        mat = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            mat[i][i] = (0, 0)
        for i in range(n):
            for j, w in self.graph[i]:
                mat[i][j] = [0, w]
                if not mat[j][i]:
                    mat[j][i] = [0, 0]
        return mat

    @staticmethod
    def getAugPath(res_net, s, t):
        q = deque([s])
        seen = set([s])
        pred = len(res_net) * [None]
        c_min = float('inf')
        while q:
            u = q.popleft()
            for v, vertex in enumerate(res_net[u]):
                if vertex is None or vertex[1] == 0 or v in seen:
                    continue
                _, c = vertex
                c_min = min(c_min, c)
                q.append(v)
                seen.add(v)
                pred[v] = u

        path = [t]
        u = pred[t]
        while u != s:
            if u is None:
                return None, None
            path.append(u)
            u = pred[u]
        path.append(s)
        path.reverse()
        return path, c_min


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
# sum = 0
# for edge1 in mst1:
#     sum += edge1[2]
#     print(edge1[0]+1, '->', edge1[1]+1, edge1[2])
# print('tree weight:', sum)
# sum = 0
# for edge2 in mst2:
#     sum += edge2[2]
#     print(edge2[0]+1, '->', edge2[1]+1, edge2[2])
# print('tree weight:', sum)

# Shortest path
# graph = [[(1, 6), (3, 7)], [(2, 5), (3, 8), (4, 4)], [(1, 2)], [(4, 9), (2, 3)], [(2, 7), (0, 2)]]
# my_graph = Graph(graph, 'adj_list')
# dist, pred = my_graph.bellman_ford(0)
# print(dist)
# my_graph.print_path(4, pred)
# print()
# dist, pred = my_graph.dijkstra(0)
# print(dist)
# my_graph.print_path(4, pred)
# print()
# dist, pred = my_graph.floyd_warshal()
# for row in dist:
#     print(row)
# my_graph.print_path_from(0, 4, pred)

# Maximum flow
g = [[(1, 16), (3, 13)], [(2, 12)], [(3, 9), (5, 20)], [(1, 4), (4, 14)], [(2, 7), (5, 4)], []]
my_graph = Graph(g, 'adj_list')
max_flow = my_graph.edmonds_karp(0, 5)
print(max_flow)