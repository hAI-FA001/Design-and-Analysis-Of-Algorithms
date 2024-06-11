import random
import time
import matplotlib.pyplot as plt


def radix_sort(array):
    # to keep track of where original value ends up after sorting on a digit
    class DigitArray:
        def __init__(self, array, d, digit):
            digit_from_left = (d-1) - digit
            self.array = [{"original_index": idx, "value": int(str(i)[digit_from_left])} for idx, i in enumerate(array)]
            
        def __getitem__(self, i): return self.array[i]
        def __setitem__(self, i, item): self.array[i] = item
    
    def _stable_sort(array, n, digit, d, output_array):
        def _count_sort(array, n, k, B):
            C = [0]*(k+1)
            
            for j in range(0, n): C[array[j]["value"]] += 1
            for i in range(1, k+1): C[i] += C[i-1]
            
            for j in reversed(range(0, n)):
                B[C[array[j]["value"]] -1] = array[j]
                C[array[j]["value"]] -= 1
                
            return B
        
        cur_digits = DigitArray(array, d, digit)
        _count_sort(cur_digits, n, 9, B=output_array)
        for i in range(n): output_array[i] = array[output_array[i]["original_index"]]
    
    def _radix_sort(array, n, d):
        import copy
        
        output_array = copy.copy(array)
        for i in range(0, d): _stable_sort(copy.copy(output_array), n, i, d, output_array)
            
        return output_array
    
    return _radix_sort(array, len(array), len(str(array[0])))


n_start, n_end, step = 1, 1000, 10
times = []

for n in range(n_start, n_end + 1, step):
    avg_time = 0
    
    for _ in range(10):
        array = [random.randint(10_000, 99_999) for _ in range(n)]
    
        s = time.time()
        array = radix_sort(array)
        f = time.time()
    
        avg_time += (f - s)
    
    times.append(avg_time / 10)


plt.plot(range(n_start, n_end + 1, step), times)
plt.xlabel("Number of elements")
plt.ylabel("Total Time")
plt.show()
