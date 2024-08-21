from enum import Enum

class Color(Enum):
    WHITE=0
    GRAY=1
    BLACK=2

class Vertex:
    def __init__(self, label):
        self.label = label
        self.color = color.WHITE
        self.d = float('inf')
        self.f = float('inf')
        self.pi = None
    
    def __repr__(self):
        return self.label

class Graph:
    def __init__(self, vertices, adj):
        self.V = vertices
        self.Adj = adj


color = Enum('Color', ['WHITE', 'GRAY', 'BLACK'])