from enum import Enum
import random


class Color(Enum):
    WHITE=0
    GRAY=1
    BLACK=2

class Vertex:
    def __init__(self, label):
        self.label = label
        self.color = color.WHITE
        self.d = float('inf')
        self.f = float('inf')
        self.pi = None
    
    def __repr__(self):
        return self.label

class Graph:
    def __init__(self, vertices, adj):
        self.V = vertices
        self.Adj = adj


def dfs(G: Graph):
    def dfs_visit(G: Graph, u: Vertex):
        # use these variables from outer scope
        nonlocal time, traversal
        
        # start time (time when "u" was first visited)
        time += 1
        u.d = time
        # mark as visited
        u.color = color.GRAY
        
        # for each neighbor
        for v in G.Adj[u]:
            # check if it's not visited
            if v.color == color.WHITE:
                # set parent to "u"
                v.pi = u
                dfs_visit(G, v)
        
        # finish time (time when entire subtree rooted at "u" was visited)
        time += 1
        u.f = time
        u.color = color.BLACK
        
        # record the info
        traversal.append(u)
    
    traversal = []
    time = 0
    # for each vertex
    for u in G.V:
        # check if it isn't visited
        if u.color == color.WHITE:
            dfs_visit(G, u)
    
    # return the traversal, sorted in order of start time
    return sorted(traversal, key=lambda v: v.d)


color = Enum('Color', ['WHITE', 'GRAY', 'BLACK'])

if __name__ == '__main__':
    vertices = [Vertex(f'V{i+1}') for i in range(5)]
    adj = {v: random.sample(vertices, k=random.randint(1, len(vertices)))
        for v in vertices}
    G = Graph(vertices, adj)

    print('Adjecency List:')
    for u in adj:
        vs = adj[u]
        print(f'- {u}: {' '.join([str(v) for v in vs])}')

    traversal = dfs(G)
    print('\nTraversal order:')
    for v in traversal:
        print(f'- Visited ({v.pi if v.pi is not None else None}, {v}) at {v.d} to {v.f}')
