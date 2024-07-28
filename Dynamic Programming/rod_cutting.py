def rod_cutting(p, n):
    # intialize all subproblems solution with -ve infinity
    r = [0]*(n+1)
    record_cuts = [""]*(n+1)
        
    # loop over subproblem sizes
    for j in range(n):
        q = float('-inf')
        # try all cuts
        cuts = ""
        for i in range(j+1):  # j+1 because it must run at least 1 iteration
            # q = max(q, p[i] + r[j - i])
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                cuts = f"Cut {i+1}"
                # add "+" only if we have a cut at "j-i"
                cuts += (" + " if record_cuts[j - i] else "")
                cuts += f"{record_cuts[j - i]}"
        # memoize
        r[j+1] = q  # j runs from 0 to n-1, update the problem from 1 to n
        record_cuts[j+1] = cuts
        
    return r[n], record_cuts[n]

prices = [1, 5, 8, 0, 0, 17, 18]
problem_size = 7

optimal_value, cuts = rod_cutting(prices, problem_size)
print(f"Achieved {optimal_value} with {cuts}")