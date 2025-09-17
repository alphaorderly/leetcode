class UnionFind:
    def __init__(self, n: int):
        self.parent = [-1] * n
        self.rank = [0] * n

    def find(self, a: int) -> int:
        while self.parent[a] != -1:
            a = self.parent[a]

        return a

    def union(self, a: int, b: int) -> bool:
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return True

        if self.rank[a] > self.rank[b]:
            self.parent[b] = a
        elif self.rank[b] > self.rank[a]:
            self.parent[a] = b
        else:
            self.parent[a] = b
            self.rank[a] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        u = UnionFind(n)

        for a, b in edges:
            u.union(a, b)

        ans = set()

        for a in range(n):
            ans.add(u.find(a))

        return len(ans)