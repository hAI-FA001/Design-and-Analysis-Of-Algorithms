import random
import time
import matplotlib.pyplot as plt


def count_sort(array):
    def _count_sort(array, n, k):
        B = [0]*n
        C = [0]*(k+1)
        
        for j in range(0, n): C[array[j]] += 1
        for i in range(1, k+1): C[i] += C[i-1]
        
        for j in reversed(range(0, n)):
            B[C[array[j]] -1] = array[j]
            C[array[j]] -= 1
            
        return B
    
    return _count_sort(array, len(array), max(array))


n_start, n_end, step = 1, 1000, 10
times = []

for n in range(n_start, n_end + 1, step):
    avg_time = 0
    
    for _ in range(10):
        array = [random.randint(1, 100) for _ in range(n)]
    
        s = time.time()
        array = count_sort(array)
        f = time.time()
    
        avg_time += (f - s)
    
    times.append(avg_time / 10)


plt.plot(range(n_start, n_end + 1, step), times)
plt.xlabel("Number of elements")
plt.ylabel("Total Time")
plt.show()
