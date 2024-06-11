import random

def activity_selection(start_times, finish_times, n):
    selected = {0}
    k = 0
    
    for m in range(1, n):
        # select compatible activities
        if start_times[m] >= finish_times[k]:
            selected = selected.union({m})
            k = m
            
    return selected


start_times = [random.randint(1, 50) for _ in range(10)]
finish_times = [random.randint(start_times[i]+1, 100) for i in range(10)]

# assumption: activities are ordered by finish times
print(start_times, finish_times)
start_finish_times = sorted(zip(start_times, finish_times), key=lambda x: x[1])
start_times, finish_times = list(map(lambda x: x[0], start_finish_times)), list(map(lambda x: x[1], start_finish_times))
print(start_times, finish_times)

print(activity_selection(start_times, finish_times, len(start_times)))