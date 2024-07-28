import numpy as np

def lcs(X, Y, m, n):
    c = np.zeros((m+1, n+1))
    b = np.zeros((m, n), dtype=np.object_)
    b[:, :] = 'N/A'
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            # current characters are equal
            if X[i-1] == Y[j-1]:
                c[i, j] = c[i-1, j-1] + 1
                b[i-1, j-1] = '↖'
            # moving up has lower cost
            elif c[i-1, j] >= c[i, j-1]:
                c[i, j] = c[i-1, j]
                b[i-1, j-1] = '↑'
            # moving left has lower cost
            else:
                c[i, j] = c[i, j-1]
                b[i-1, j-1] = '←'
    
    return c, b

def print_lcs(b, X, i, j):
    # check if this would be out of bounds
    if i == -1 or j == -1:
        return
    
    if b[i, j] == '↖':
        print_lcs(b, X, i-1, j-1)
        print(X[i], end='')
    elif b[i, j] == '↑':
        print_lcs(b, X, i-1, j)
    else:
        print_lcs(b, X, i, j-1)

s1 = "Hellow"
s2 = "'ello"

cost, backtrack = lcs(s1, s2, len(s1), len(s2))

print("Length matrix:\n", cost)
print("Backtracking matrix:\n", backtrack)

print("Longest Common Subsequence: ", end='')
print_lcs(backtrack, s1, len(s1)-1, len(s2)-1)
