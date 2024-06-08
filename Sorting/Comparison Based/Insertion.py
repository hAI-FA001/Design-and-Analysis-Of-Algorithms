import random
import time
import matplotlib.pyplot as plt

def insertion_sort(array):
    n = len(array)
    for i in range(n):
        cur = array[i]
        j = i-1
        while j > -1 and cur < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = cur
                
    return array


n_start, n_end, step = 1, 1000, 10
times = []

for n in range(n_start, n_end + 1, step):
    avg_time = 0
    
    for _ in range(10):
        array = [random.randint(1, 100) for _ in range(n)]
    
        s = time.time()
        array = insertion_sort(array)
        f = time.time()
    
        avg_time += (f - s)
    
    times.append(avg_time / 10)


plt.plot(range(n_start, n_end + 1, step), times)
plt.xlabel("Number of elements")
plt.ylabel("Total Time")
plt.show()