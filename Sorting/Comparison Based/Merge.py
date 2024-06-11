import random
import time
import matplotlib.pyplot as plt


def merge_sort(array):
    from math import floor
    
    def _merge(array, s, m, e):
        n_left = m - s + 1
        n_right = e - m
        
        L = [0] * n_left
        R = [0] * n_right
        
        for i in range(n_left): L[i] = array[s + i]
        for j in range(n_right): R[j] = array[m+1 + j]
        
        i=0
        j=0
        k=s
        
        while i < n_left and j < n_right:
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        
        # for any remaining elements
        while i < n_left:
            array[k] = L[i]
            i += 1
            k += 1
        while j < n_right:
            array[k] = R[j]
            j += 1
            k += 1
        
    
    def _merge_sort(array, s, e):
        if s >= e: return
        
        m = floor((s + e) / 2)
        
        _merge_sort(array, s, m)
        _merge_sort(array, m+1, e)
        
        _merge(array, s, m, e)
            
    
    _merge_sort(array, 0, len(array)-1)
    return array


n_start, n_end, step = 1, 1000, 10
times = []

for n in range(n_start, n_end + 1, step):
    avg_time = 0
    
    for _ in range(10):
        array = [random.randint(1, 100) for _ in range(n)]
    
        s = time.time()
        array = merge_sort(array)
        f = time.time()
    
        avg_time += (f - s)
    
    times.append(avg_time / 10)


plt.plot(range(n_start, n_end + 1, step), times)
plt.xlabel("Number of elements")
plt.ylabel("Total Time")
plt.show()