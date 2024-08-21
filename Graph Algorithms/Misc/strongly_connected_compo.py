from ..Data_Structures.graph import Graph, Vertex
from ..Traversal.dfs import dfs

def scc(G: Graph):
    # use DFS to calculate finish times
    traversal = dfs(G)
    
    # for next DFS, consider vertices in order of finish times -> sort G.V a/c to finish time of v
    vertex_and_finish_times = {v.label: v.f for v in traversal}
    # create new vertices to avoid issues with state, e.g. v.color
    lbl_to_idx = {v.label: i for i, v in enumerate(G.V)}
    new_verts = [Vertex(l) for l in lbl_to_idx.keys()]
    G.V = sorted(new_verts, key=lambda v: vertex_and_finish_times[v.label], reverse=True)
    
    # create transpose of G, i.e. invert the edges
    adj_T = {}
    for u in G.Adj:
        new_u = new_verts[lbl_to_idx[u.label]]
        for v in G.Adj[u]:
            new_v = new_verts[lbl_to_idx[v.label]]
            adj_T[new_v] = adj_T.get(new_v, []) +  [new_u]
    G_T = Graph(new_verts, adj_T)

    # traverse transpose of G using DFS
    traversal = dfs(G_T)
    
    # store each subtree
    roots_to_children = {}
    for v in traversal:
        # record and traverse this path up to root node
        path = set()
        cur = v
        while cur.pi is not None:
            path.add(cur)
            cur = cur.pi
            
        roots_to_children[cur] = roots_to_children.get(cur, set()) | path
    
    return roots_to_children
        

lbls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertices = [Vertex(l) for l in lbls]
adj = {
    vertices[lbls.index('a')]: [vertices[lbls.index('b')]],
    vertices[lbls.index('b')]: [vertices[lbls.index('e')], vertices[lbls.index('f')], vertices[lbls.index('c')]],
    vertices[lbls.index('c')]: [vertices[lbls.index('g')], vertices[lbls.index('d')]],
    vertices[lbls.index('d')]: [vertices[lbls.index('c')]],
    vertices[lbls.index('e')]: [vertices[lbls.index('a')], vertices[lbls.index('f')]],
    vertices[lbls.index('f')]: [vertices[lbls.index('g')]],
    vertices[lbls.index('g')]: [vertices[lbls.index('f')], vertices[lbls.index('h')]],
    vertices[lbls.index('h')]: [vertices[lbls.index('h')]],
}

G = Graph(vertices, adj)

print('Adjecency List:')
for u in adj:
    vs = adj[u]
    print(f'- {u}: {' '.join([str(v) for v in vs])}')
        
        
sc_compos = scc(G)
print('Strongly Connected Components:')
for u in sc_compos:
    children = sc_compos[u]
    print(f'-', {u} | children)
