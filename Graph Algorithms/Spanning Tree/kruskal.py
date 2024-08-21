from ..Traversal.dfs import Graph, Vertex
import random


# need to make a Disjoint-Set data structure for this algo

class SetObject:
    def __init__(self, member):
        self.member = member
        self.p = None
        self.rank = 0 # upper bound on height of the node
    
    def __repr__(self):
        return str(self.member)

class DisjointSetForests:
    def __init__(self):
        self.sets = {}
        
    def make_set(self, x):
        x.p = x
        x.rank = 0
    
    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))
    
    def link(self, x, y):
        # union-by-rank heuristic: make shorter tree point to longer tree
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            if x.rank == y.rank:
                y.rank += 1
    def find_set(self, x):
        if x != x.p:
            # path compression: make each node's parent point to root
            x.p = self.find_set(x.p)
        return x.p

def kruskal(G: Graph, w):
    dsf = DisjointSetForests()
    A = set()  # stores edges of the Minimum Spanning Tree
    
    # make each vertex into a set
    for v in G.V:
        s = SetObject(v)
        dsf.make_set(s)
        dsf.sets[v] = s
    
    # create a list of edges
    edges = []
    for u in G.V:
        for j, v in enumerate(G.Adj[u]):
            weight = w[u][j]
            edges.append((weight, (dsf.sets[u], dsf.sets[v])))  # append SetObject rather than vertex so it's easier later
    
    # sort based on weight
    edges.sort(key=lambda x: x[0])

    # keep merging set associated with vertices on edge (u, v)
    for e in edges:
        _, (u, v) = e
        if dsf.find_set(u) != dsf.find_set(v):
            A = A | {(u, v)}
            dsf.union(u, v)
    
    return A


vertices = [Vertex(f'V{i+1}') for i in range(5)]
adj = {v: random.sample(vertices, k=random.randint(1, len(vertices)))
    for v in vertices}
weights = {v: [random.randint(1, 10) for _ in range(len(adj[v]))]
    for v in vertices}
G = Graph(vertices, adj)

print('Adjecency List:')
for u in adj:
    vs = adj[u]
    ws = weights[u]
    print(f'- {u}: {', '.join([str(v) + f" ({w})" for v, w in zip(vs, ws)])}')

sets = kruskal(G, weights)
print('\nSets:')
for s in sets:
    print(f'- {s}')