from ..Data_Structures.graph import Vertex, Graph
from queue import PriorityQueue
import random


def prim(G: Graph, w, r: Vertex):
    for u in G.V:
        u.d = float('inf')
        u.pi = None
    r.d = 0
    
    Q = PriorityQueue()
    for u in G.V:
        Q.put(u)
    
    i = 0
    while not Q.empty():
        u = Q.get()
        
        for i, v in enumerate(G.Adj[u]):
            if v in Q.queue and w[u][i] < v.d:
                v.pi = u
                v.d = w[u][i]
                Q.put_nowait(v)
                
    edges = []
    for u in G.V:
        edges.append((u.pi, u))
             
    return edges


setattr(Vertex, "__lt__", lambda self, other: self.d < other.d)

vertices = [Vertex(f'V{i+1}') for i in range(5)]
adj = {v: random.sample(vertices[:i] + vertices[i+1:], k=random.randint(1, len(vertices[:i] + vertices[i+1:])))
    for i, v in enumerate(vertices)}
weights = {v: [random.randint(1, 10) for _ in range(len(adj[v]))]
    for v in vertices}
G = Graph(vertices, adj)

print('Adjecency List:')
for u in adj:
    vs = adj[u]
    ws = weights[u]
    print(f'- {u}: {', '.join([str(v) + f" ({w})" for v, w in zip(vs, ws)])}')

mst_edges =  prim(G, weights, vertices[0])
print('\nEdges chosen in MST:')
for e in mst_edges:
    print(f'- {e}')
