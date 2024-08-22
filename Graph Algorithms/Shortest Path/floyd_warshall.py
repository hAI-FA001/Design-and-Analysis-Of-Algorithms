from ..Data_Structures.graph import Vertex
import numpy as np
import random


def floyd_warshall(W, n, Pi_0):
    D = np.zeros((n+1, n, n))
    Pi = np.zeros((n+1, n, n))
    D[0] = np.array(W)
    Pi[0] = Pi_0
    
    for k in range(1, n+1):
        for i in range(0, n):
            for j in range(0, n):
                vert_k = k-1
                prev_dist = D[k-1, i, j]
                # use vertex "k" as intermediate vertex
                # i.e. go from vertex i to k, then k to j
                dist_via_vertex_k = D[k-1, i, vert_k] + D[k-1, vert_k, j]
    
                if dist_via_vertex_k < prev_dist:
                    D[k, i, j] = dist_via_vertex_k
                    Pi[k, i, j] = vert_k
                else:
                    D[k, i, j] = prev_dist
                    Pi[k, i, j] = Pi[k-1, i, j]
    
    return D[n], Pi[n]


# my funcs to calculate entire path and path cost
def get_verts_in_path(Pi_n, from_, to):
    def calc_path(from_, to):
        if from_ == to:
            return from_, to
        
        from_, to = np.int8(from_), np.int8(to)
        intermediate = Pi_n[from_, to]
        if np.isnan(intermediate):
            return None, None
        
        if intermediate in [from_, to]:
            return from_, to
        
        left_from, left_to = calc_path(from_, intermediate)
        right_from, right_to = calc_path(intermediate, to)
        
        return (left_from, left_to), (right_from, right_to)
    
    def unpack_tuples(tuples):
        if None in tuples:
            return []
        if type(tuples[0]) in [np.int8, int]:
            return [i for i in tuples]
        else:
            l = []
            for t in tuples:
                l.extend(unpack_tuples(t))
            return l
    
    edges = calc_path(from_, to)
    verts_list = unpack_tuples(edges)
    if len(verts_list) == 0:
        return []
    
    unique_verts = [verts_list[0]]
    for i in range(1, len(verts_list)):
        u = verts_list[i-1]
        v = verts_list[i]
        if v != u:
            unique_verts.append(v)
    
    return unique_verts


def get_total_cost(W, verts):
    total_cost = 0
    for i in range(len(verts)-1):
        from_ = verts[i]
        to = verts[i+1]
        total_cost += W[from_, to]
        
    return total_cost


n = 5
vertices = [Vertex(f'V{i+1}') for i in range(n)]
W = np.zeros((n, n))
Pi = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        # for diagonal (vertex i to itself), distance is 0
        # for non-diagonal, choose a random weight with 70% chance, choose infinity (no edge) with 30% chance
        W[i, j] = 0 if i == j else random.randint(1, 30) if random.randint(1, 10) < 7 else float('inf')
        does_i_to_j_exist = W[i, j] != float('inf')
        # parent matrix: if edge (i, j) exists and vertex i & j aren't same, then parent is vertex i
        Pi[i, j] = i if does_i_to_j_exist and i != j else None


print("Matrix W:")
print(W)
print("\nMatrix Pi:")
print(Pi)

print("\nFloyd-Warshall:")
D_n, Pi_n = floyd_warshall(W, n, Pi)
print("Matrix D[n]:")
print(D_n)
print("\nMatrix Pi[n]:")
print(Pi_n)

print("\n\nAll-Pair Shortest Paths:")
for i in range(n):
    for j in range(n):
        if i == j: continue
        
        path = get_verts_in_path(Pi_n, i, j)
        if len(path) == 0:
            path = f"No path from {i} to {j}"
            total_cost = float('inf')
            cost_in_matrix = D_n[i, j]    
        else:    
            total_cost = get_total_cost(W, path)
            cost_in_matrix = D_n[i, j]
        
        print(f"{str(path):20}\tCost: {total_cost:20}\tActual: {cost_in_matrix:20}\tMatch? {total_cost == cost_in_matrix}")
