import random
from functools import reduce

def fractional_knapsack(items, w_max):
    sorted_by_value_per_weight = sorted(items, key=lambda x: x[1] / x[2], reverse=True)
    
    selected = []
    cur_weight = 0
    for item_no, value, weight in sorted_by_value_per_weight:
        # need: cur_weight + fraction * weight <= w_max
        # rearrange: fraction <= (w_max - cur_weight) / weight
        # also fraction <= 1
        remaining_weight = max(0, w_max - cur_weight)
        fraction = min(1, remaining_weight / weight)
        
        if fraction > 0:
            selected.append((item_no, fraction))
            cur_weight += fraction * weight
    
    return selected

items = [(i, random.randint(1, 100), random.randint(1, 100)) for i in range(10)]
w_max = 10

print(items)
solution = fractional_knapsack(items, w_max)
print(solution)
print("Total weight: ", reduce(lambda total, entry: total + (entry[1] * items[entry[0]][2]), solution, 0.0))
