import numpy as np


def edit_dist(x, y):
    # DP approach solves it in "reverse"/"mirrored", so need to reverse these strings first
    x, y = x[::-1], y[::-1]
    
    # cost for Copy, Replace, Delete, Insert, Twiddle, Kill
    Qc, Qr, Qd, Qi, Qt, Qk = 1, 2, 3, 3, 1, 1
    
    m, n = len(x), len(y)
    memo = np.array([[0 for _ in range(n+1)] for _ in range(m+1)])
    ops = np.array([[' '*7 for _ in range(n+1)] for _ in range(m+1)])

    # first col means transform X into empty string (can only perform deletes)
    for i in range(1, m+1):
        cd = Qd + memo[i-1, 0]
        ck = Qk + memo[0, 0]
        memo[i, 0] = min(cd, ck)
        ops[i, 0] = 'delete' if memo[i, 0] == cd else 'kill'
    # first row means transform emptry string into Y (can only perform inserts)
    for j in range(1, n+1):
        memo[0, j] = Qi + memo[0, j-1]
        ops[0, j] = 'insert'
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            # if current chars are equal
            can_copy = x[i-1] == y[j-1]
            # if (X and Y have at least 2 chars) and (not out of bounds) and (twiddle condition satisfied)
            can_twiddle = (m > 1 and n > 1) and (i-1 < m and j-1 < n and i-2 >= 0 and j-2 >= 0) and (x[i-1] == y[j-2] and x[i-2] == y[j-1])
            can_kill = False
            
            # calculate costs
            cc = Qc + memo[i-1, j-1] if can_copy else float('inf')
            cr = Qr + memo[i-1, j-1]
            cd = Qd + memo[i-1, j]
            ci = Qi + memo[i, j-1]
            ck = Qk + memo[0, j] if can_kill else float('inf')
            ct = Qt + memo[i-2, j-2] if can_twiddle else float('inf')
            # use min  for min edit distance
            cost = min(cc, cr, cd, ci, ck, ct)
            
            memo[i, j] = cost

            # find out which operation was performed
            op = ''
            if cost == cc:
                op = 'copy'
            elif cost == cr:
                op = 'replace'
            elif cost == cd:
                op = 'delete'
            elif cost == ci:
                op = 'insert'
            elif cost == ck:
                op = 'kill'
            elif cost == ct:
                op = 'twiddle'
            
            ops[i, j] = op

    # extract edit steps from ops via backtracking
    i, j = m, n
    operations = ''
    while i > 0 or j > 0:
        op = ops[i, j]
        operations += op + ' '
        
        # adjust indices according to operation
        if op in ['copy', 'replace']:
            i -= 1
            j -= 1
        elif op == 'delete':
            i -= 1
        elif op == 'insert':
            j -= 1
        elif op == 'kill':
            i = 0
            break # kill must be the final operation if performed
        elif op == 'twiddle':
            i -= 2
            j -= 2
    
    operations = ', '.join(operations.split(' ')).strip(', ')
    
    return memo[m, n], operations

x = 'Eidt this Distance'
y = 'Edit Distance'
print(f"Transforming {x} into {y}")

dist, ops = edit_dist(x, y)
print(f"Distance: {dist}")
print(f"Sequence of Operations: {ops}")
print(f"Carrying out operations:")

z = list(x)
ops = ops.split(',')
i = 0
j = 0
print(f'{''.join(z)}\n -> ', end='')
for num_op, op in enumerate(ops):
    op = op.strip()
    
    if op in ['copy', 'replace']:
        z[i] = y[j]
        i += 1
        j += 1
    elif op == 'delete':
        z = z[:i] + z[i+1:]
    elif op == 'insert':
        z.insert(i, y[j])
        i += 1
        j += 1
    elif op == 'kill':
        z = z[:i]
        i = len(x)+1
    elif op == 'twiddle':
        z[i], z[i+1] = z[i+1], z[i]
        i += 2
        j += 2

    print(f'({op}) {''.join(z)}')
    if num_op != len(ops)-1:
        print(' -> ', end='')
