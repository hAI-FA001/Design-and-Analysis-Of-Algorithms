from queue import PriorityQueue
import random


def huffman(counts):
    class HuffmanNode:
        def __init__(self,  letter='', freq=0):
            self.left = None
            self.right = None
            self.letter = letter
            self.freq = freq
        
        def __eq__(self, value): return self.freq == value.freq
        def __le__(self,value): return self == value or self.freq < value.freq
        
        def __str__(self):
            return f"[ {self.left} <- {self.letter} {self.freq} -> {self.right} ]".replace('None', '/')
    
    n = len(counts)
    q = PriorityQueue()
    
    for letter, freq in counts: q.put((freq, HuffmanNode(letter, freq)))
    
    # it's important that this is range(n-1) and not range(n)
    for _ in range(n-1):
        z = HuffmanNode()
        
        x_freq, x = q.get()
        y_freq, y = q.get()
        
        z.left = x
        z.right = y
        z.freq = x_freq + y_freq
        
        q.put((z.freq, z))
        
        
    return q.get()[1]  # root node


counts = [(letter, random.randint(1, 100))
          for letter in [chr(random.randint(65, 90))
                         for _ in range(5)
                         ]
          ]

print(counts)
solution = huffman(counts)
print(solution)