from ..Data_Structures.graph import color, Vertex, Graph
import random


def bfs(G: Graph, s: Vertex):
    # no need for this as this is done in Vertex.__init__
    # for u in G.V - {s}:
    #     u.color = color.WHITE
    #     u.d = float('inf')
    #     u.pi = None
    
    # starting vertex
    s.color = color.GRAY
    s.d = 0
    s.pi = None
    
    # queue
    Q = [s]
    # record the path
    traversal = []
    while len(Q) != 0:
        u = Q.pop(0)
        traversal.append((u.pi.label if u.pi is not None else None, u.label))
        
        # for each neighbor
        for v in G.Adj[u]:
            # check if it isn't traversed
            if v.color == color.WHITE:
                # mark as visited
                v.color = color.GRAY
                v.d = s.d + 1
                v.pi = s
                
                Q.append(v)
                
        # mark as completed (all neighbors have been traversed)
        u.color = color.BLACK
    
    return traversal


vertices = [Vertex(f'V{i+1}') for i in range(5)]
adj = {v: random.sample(vertices, k=random.randint(1, len(vertices)))
       for v in vertices}
G = Graph(vertices, adj)

print('Adjecency List:')
for u in adj:
    vs = adj[u]
    print(f'- {u.label}: {' '.join([v.label for v in vs])}')

traversal = bfs(G, vertices[0])
print('\nTraversal order: ', traversal)
