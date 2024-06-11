import random
import time
import matplotlib.pyplot as plt


def heap_sort(array):
    from math import floor, ceil
    
    class HeapArray:
        def __init__(self, array):
            self.array = array
            
            self.left = lambda index: 2*index
            self.right = lambda index: 2*index + 1
            
            self.heap_size = len(array)
            
        def __getitem__(self, i): return self.array[i]
        def __setitem__(self, i, item): self.array[i] = item
    
    def _max_heapify(array: HeapArray, i):
        l = array.left(i)
        r = array.right(i)
        
        if l < array.heap_size and array[l] > array[i]:
            largest = l
        else:
            largest = i
        if r < array.heap_size and array[r] > array[largest]:
            largest = r
        
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            _max_heapify(array, largest)
        
        
    def _build_max_heap(array: HeapArray, n):
        array.heap_size = n
        for i in reversed(range(0, floor(n / 2))): _max_heapify(array, i)
        
    def _heap_sort(array: HeapArray, n):
        _build_max_heap(array, n)
        
        for i in reversed(range(1, n)):
            array[0], array[i] = array[i], array[0]
            array.heap_size -= 1
            _max_heapify(array, 0)

    
    heap_array = HeapArray(array)
    _heap_sort(heap_array, len(array))
    
    return array


n_start, n_end, step = 1, 1000, 10
times = []

for n in range(n_start, n_end + 1, step):
    avg_time = 0
    
    for _ in range(10):
        array = [random.randint(1, 100) for _ in range(n)]
    
        s = time.time()
        array = heap_sort(array)
        f = time.time()
    
        avg_time += (f - s)
    
    times.append(avg_time / 10)


plt.plot(range(n_start, n_end + 1, step), times)
plt.xlabel("Number of elements")
plt.ylabel("Total Time")
plt.show()