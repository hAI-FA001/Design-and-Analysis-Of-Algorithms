from ..Data_Structures.graph import Vertex, Graph
import random

def bellman_ford(G: Graph, w, s: Vertex):
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
    for _ in range(0, len(G.V)-1):
        for (u, v) in G.E:
            relax(u, v, w)

    for (u, v) in G.E:
        if v.d > u.d + w[u][v]:
            return False
    
    return True


vertices = [Vertex(f'V{i+1}') for i in range(5)]
E = {(u, random.choice(vertices[:i] + vertices[i+1:])) for i, u in enumerate(vertices) for _ in range(random.randint(0, len(vertices)-1))}
weights = {}
for (u, v) in E:
    if u not in weights:
        weights[u] = {}
    weights[u][v] = random.randint(1, 10)
    
G = Graph(vertices, None)
setattr(G, "E", E)

print('Adjecency List:')
for (u, v) in E:
    print(f'- ({u}, {v}, {weights[u][v]})')

if bellman_ford(G, weights, vertices[0]):
    print("\nShortest Paths w/ Bellman-Ford:")
    for u in G.V:
        print(f"- ({u.pi}, {u}, {u.d})")
else:
    print("\nThere is a negative-weight cycle.")