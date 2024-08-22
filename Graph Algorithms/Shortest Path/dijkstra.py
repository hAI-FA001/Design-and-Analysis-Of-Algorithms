from ..Data_Structures.graph import Vertex, Graph
import random
from queue import PriorityQueue

def dijkstra(G: Graph, w, s: Vertex):
    def initialize_single_source(G: Graph, s: Vertex):
        for v in G.V:
            v.d = float('inf')
            v.pi = None
        s.d = 0
        
    def relax(u: Vertex, v: Vertex, w):
        if v.d > u.d + w[u][v]:
            v.d = u.d + w[u][v]
            v.pi = u
    
    initialize_single_source(G, s)
    
    S = set()
    Q = PriorityQueue()
    
    for u in G.V:
        Q.put(u)
    
    while not Q.empty():
        u = Q.get()
        S = S | {u}
        
        if u not in G.Adj:
            continue
        
        for v in G.Adj[u]:
            before = v.d
            relax(u, v, w)
            if before != v.d:
                Q.put_nowait(v)
    
    return True


setattr(Vertex, "__lt__", lambda self, other: self.d < other.d)

vertices = [Vertex(f'V{i+1}') for i in range(5)]
adj = {u: random.sample(vertices[:i] + vertices[i+1:], k=random.randint(1, len(vertices)-1)) 
       # add edges to this vertex with 70% chance + always add an edge for V1
       for i, u in enumerate(vertices) if random.randint(1, 10) <= 7 or i == 0}

weights = {}
for u in adj:
    weights[u] = {}
    for v in adj[u]:
        weights[u][v] = random.randint(1, 10)

G = Graph(vertices, adj)


print('Adjecency List:')
for u in adj:
    for v in adj[u]:
        print(f'- ({u}, {v}, {weights[u][v]})')


print("\nShortest Paths w/ Dijkstra:")
dijkstra(G, weights, vertices[0])
for u in G.V:
    print(f"- ({u.pi}, {u}, {u.d})")
