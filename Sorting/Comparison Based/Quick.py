import random
import time
import matplotlib.pyplot as plt


def quick_sort(array):
    def _partition(array, s, e):
        pivot = array[e]
        i = s-1
        
        # moves all smaller elements to i+1 (makes left half)
        for j in range(s, e):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        # moves pivot to just after left half
        array[i+1], array[e] = array[e], array[i+1]
        
        return i+1
    
    def _quick_sort(array, s, e):
        if s < e:
            p = _partition(array, s, e)
            _quick_sort(array, s, p-1)
            _quick_sort(array, p+1, e)
            
    
    _quick_sort(array, 0, len(array)-1)
    return array


n_start, n_end, step = 1, 1000, 10
times = []

for n in range(n_start, n_end + 1, step):
    avg_time = 0
    
    for _ in range(10):
        array = [random.randint(1, 100) for _ in range(n)]
    
        s = time.time()
        array = quick_sort(array)
        f = time.time()
    
        avg_time += (f - s)
    
    times.append(avg_time / 10)


plt.plot(range(n_start, n_end + 1, step), times)
plt.xlabel("Number of elements")
plt.ylabel("Total Time")
plt.show()