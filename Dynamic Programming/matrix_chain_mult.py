import numpy as np

def matrix_chain_mult_order(p, n):
    m = np.zeros((n, n))
    s = np.zeros((n, n), dtype=np.int64)
    
    # (n, n) matrix
    # first, solve diag+1, then diag+2 etc
    #           (1, 2), (1, 3), ..., (1, n)
    #                   (2, 3), ..., (2, n)
    #                           ..., (3, n)
    # 1st iter: (1, 2), (2, 3), (3, 4)
    # 2nd iter: (1, 3), (2, 4), (out of bounds)
    # 3rd iter: (1, 4), (out of bounds)
    # nth iter: (i, i + n)
    # and i goes from 1 to n - l, l goes from 2 to n
    
    for l in range(1, n):
        for i in range(0, n - (l - 1) -1):
            j = i + (l - 1) +1

            # solving (i, j)
            m[i, j] = np.inf
            
            # at (i, j) = (1, 4) = A1:A4
            # = min(
                # (A1:A3) x A4,
                # A1 x (A2:A4),
                # (A1:A2) x (A3:A4)
                # )
            for k in range(i, j):
                # NOTE: do NOT separate these into newlines (without the "cost +="),
                # else python will consider them as separate statements
                # (as unary + applied to some value, not part of "cost =" assignment)
                cost = m[i, k] # cost of subproblem Ai:k
                cost += m[k+1, j]  # cost of subproblem Ak+1:j
                cost += (p[i] * p[k+1] * p[j+1])  # cost of current problem Ai:k x Ak+1:j
                
                if cost < m[i, j]:
                    m[i, j]  = cost
                    s[i, j] = k
    
    return m, s

def print_parenthesis(s, i, j):
    if i == j:
        print(f"A_{i} ", end='')
    else:
        print("( ", end='')
        print_parenthesis(s, i, s[i, j])
        print_parenthesis(s, s[i, j]+1, j)
        print(")", end='')
n = 6
dims = [30, 35, 15, 5, 10, 20, 25]

costs, cuts = matrix_chain_mult_order(dims, n)

print("Cost Matrix:\n", costs)
print("Cuts Matrix:\n", cuts)

print("Order: ", end='')
print_parenthesis(cuts, 0, 5)