import random
import time
import matplotlib.pyplot as plt

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_val = array[i]
        min_idx = i
        for j in range(i, n):
            if min_val > array[j]:
                min_val = array[j]
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    
    return array


n_start, n_end, step = 1, 1000, 10
times = []

for n in range(n_start, n_end + 1, step):
    avg_time = 0
    
    for _ in range(10):
        array = [random.randint(1, 100) for _ in range(n)]
    
        s = time.time()
        array = selection_sort(array)
        f = time.time()
    
        avg_time += (f - s)
    
    times.append(avg_time / 10)


plt.plot(range(n_start, n_end + 1, step), times)
plt.xlabel("Number of elements")
plt.ylabel("Total Time")
plt.show()