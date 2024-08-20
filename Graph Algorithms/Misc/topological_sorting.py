import random
from ..Traversal.dfs import dfs, Graph, Vertex

def topo_sort(G: Graph):
    traversal = dfs(G)
    return sorted(traversal, key=lambda x: int(x[x.index('to', x.index(')'))+3:].strip()), reverse=True)


# example from book
lbls = ['shirt', 'watch', 'undershorts', 'socks', 'pants', 'shoes', 'belt', 'tie', 'jacket']
vertices = [Vertex(l) for l in lbls]
adj = {
    vertices[lbls.index('undershorts')]: [vertices[lbls.index('pants')], vertices[lbls.index('shoes')]],
    vertices[lbls.index('pants')]: [vertices[lbls.index('shoes')], vertices[lbls.index('belt')]],
    vertices[lbls.index('socks')]: [vertices[lbls.index('shoes')]],
    vertices[lbls.index('shoes')]: [],
    vertices[lbls.index('belt')]: [vertices[lbls.index('jacket')]],
    vertices[lbls.index('shirt')]: [vertices[lbls.index('tie')], vertices[lbls.index('belt')]],
    vertices[lbls.index('tie')]: [vertices[lbls.index('jacket')]],
    vertices[lbls.index('jacket')]: [],
    vertices[lbls.index('watch')]: [],
}
G = Graph(vertices, adj)

print('Adjecency List:')
for u in adj:
    vs = adj[u]
    print(f'- {u.label}: {' '.join([v.label for v in vs])}')
    
topo_sorted = topo_sort(G)
print('\nSorted:\n-', '\n- '.join(topo_sorted))
