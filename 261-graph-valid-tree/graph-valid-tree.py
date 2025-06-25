class Union:
    def __init__(self, n: int):
        self.parent = [-1] * n
        self.rank = [0] * n
        self.n = n
        self.count = n - 1

    def find(self, a: int) -> int:
        while self.parent[a] != -1:
            a = self.parent[a]

        return a

    def union(self, a: int, b: int):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return

        if self.rank[a] > self.rank[b]:
            self.parent[b] = a
            self.rank[b] = self.rank[a]
        elif self.rank[a] < self.rank[b]:
            self.parent[a] = b
            self.rank[a] = self.rank[b]
        else:
            self.parent[a] = b
            self.rank[b] = self.rank[a] + 1

        self.count -= 1

    def same_parent(self):
        x = self.find(0)

        for i in range(1, self.n):
            if self.find(i) != x:
                return False

        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        u = Union(n)

        for a, b in edges:
            if u.find(a) == u.find(b):
                return False
            else:
                u.union(a, b)

        return u.count == 0