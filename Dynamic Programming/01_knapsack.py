import numpy as np

def knapsack_01(W, it_w, it_b):
    n = len(it_b)
    benefit_memo = np.array([[0 for _ in range(W+1)] for _ in range(n+1)])
    path = np.array([['(0, 0)' for _ in range(W+1)] for _ in range(n+1)])
    
    # for each item
    for i in range(1, n+1):
        # for each knapsack capacity
        for w in range(1, W+1):
            wi = it_w[i-1]  # current item's weight
            # if current weight fits in the capacity
            if wi <= w:
                bi = it_b[i-1]  # current item's benefit
                total_benefit = bi + benefit_memo[i-1, w - wi]
                # if adding this item yields more benefit
                if total_benefit > benefit_memo[i-1, w]:
                    # add it
                    benefit_memo[i, w] = total_benefit
                    path[i, w] = f'({i-1}, {w-wi})'
                else:
                    # don't add it
                    benefit_memo[i, w] = benefit_memo[i-1, w]
                    path[i, w] = f'({i-1}, {w})'
            else:
                # can't add it
                benefit_memo[i, w] = benefit_memo[i-1, w]
                path[i, w] = f'({i-1}, {w})'
    
    which_items = set()
    i, w = n, W
    while i > 0 or w > 0:
        prev_w = w
        which_subprob_next = path[i, w]
        
        i, w = which_subprob_next.strip('()').split(',')
        i, w = int(i.strip()), int(w.strip())
        
        # this means we didn't pick this item
        if prev_w == w:
            continue
        
        # add current item
        which_items.add(i)
    
    return benefit_memo[n, W], which_items


max_capacity = 5
item_weights, item_benefit_values = [2, 3, 4, 5], [3, 4, 5, 6]

max_benefit, items = knapsack_01(max_capacity, item_weights, item_benefit_values)
print(f"Max benefit: {max_benefit}")
print(f"Items to pick: {items}")
