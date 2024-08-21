class SetObject:
    def __init__(self, member):
        self.member = member
        self.p = None
        self.rank = 0 # upper bound on height of the node
    
    def __repr__(self):
        return str(self.member)

class DisjointSetForests:
    def __init__(self):
        self.sets = {}
        
    def make_set(self, x):
        x.p = x
        x.rank = 0
    
    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))
    
    def link(self, x, y):
        # union-by-rank heuristic: make shorter tree point to longer tree
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            if x.rank == y.rank:
                y.rank += 1
    def find_set(self, x):
        if x != x.p:
            # path compression: make each node's parent point to root
            x.p = self.find_set(x.p)
        return x.p

