
def assembly_line(e1, a1, t1, x1, e2, a2, t2, x2):
    n = len(a1)
    f1, f2 = [0]*n, [0]*n
    f1[0], f2[0] = e1 + a1[0], e2 + a2[0]
    for i in range(1, n):
        # cost to reach "i"th point on one assembly line is min of:
        #   cost to reach "i-1"th point from beginning on *same line* + cost to reach "i"th point from "i-1"th point
        #   cost to reach "i-1"th point on the *other line* + cost of transferring to this line + cost to get to "i"th point from there
        
        f1[i] = min(
            f1[i-1],
            f2[i-1] + t2[i-1]
        ) + a1[i]
        
        f2[i] = min(
            f1[i-1] + t1[i-1],
            f2[i-1]
        ) + a2[i]
    print(f1)
    print(f2)
    isOnFirstLine = True
    path = []
    lines = []
    f1[n-1] += x1
    f2[n-1] += x2
    for i in range(n-1, -1, -1):
        if f1[i] < f2[i]:
            path.insert(0, '←' if isOnFirstLine else '↖')
            lines.insert(0, 'A1')
            isOnFirstLine = True
        else:
            path.insert(0, '←' if not isOnFirstLine else '↙')
            lines.insert(0, 'A2')
            isOnFirstLine = False
    return min(f1[n-1], f2[n-1]), path, lines

# entry costs
e1, e2 = 2, 4
# exit costs
x1, x2 = 3, 2
# cost of each point on both assembly lines
a1, a2 = [7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]
# cost of transferring b/w lines at each point
t1, t2 = [2, 3, 3, 4, 8], [7, 1, 2, 2, 1]

cost, path, lines = assembly_line(e1, a1, t1, x1, e2, a2, t2, x2)
print(f"Min Cost: {cost}")
print(f"Fastest way: {path}")
print(f"Which assembly lines to choose:")
for i in range(len(lines)):
    print(f"\t - At point {i+1}, choose {lines[i]}")
