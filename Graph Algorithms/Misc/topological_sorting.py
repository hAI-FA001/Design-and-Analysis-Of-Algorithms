from ..Data_Structures.graph import Graph, Vertex
from ..Traversal.dfs import dfs


def topo_sort(G: Graph):
    traversal = dfs(G)
    return sorted(traversal, key=lambda v: v.f, reverse=True)


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
    print(f'- {u}: {' '.join([str(v) for v in vs])}')
    
topo_sorted = topo_sort(G)
print('\nSorted:')
for v in topo_sorted:
    print(f'- {f'({v.pi if v.pi is not None else None}, {v})':20}| {v.d} to {v.f}')
