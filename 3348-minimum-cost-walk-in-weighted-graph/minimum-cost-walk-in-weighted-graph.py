class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.precalc = [131071] * n
        self.rank = [1] * n

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, a: int, b: int, w: int):
        a_parent = self.find(a)
        b_parent = self.find(b)

        if a_parent == b_parent:
            self.precalc[a_parent] &= w
        else:
            if self.rank[a_parent] >= self.rank[b_parent]:
                self.parent[a_parent] = b_parent
                self.rank[b_parent] += self.rank[a_parent] + 1
                self.precalc[b_parent] &= w & self.precalc[a_parent]
            else:
                self.parent[b_parent] = a_parent
                self.rank[a_parent] += self.rank[b_parent] + 1
                self.precalc[a_parent] &= w & self.precalc[b_parent]

    def check(self, a: int, b: int):
        a_parent = self.find(a)
        b_parent = self.find(b)

        if a_parent != b_parent:
            return -1
        else:
            return self.precalc[a_parent]


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        x = UnionFind(n)

        ans = []

        for a, b, w in edges:
            x.union(a, b, w)

        for a, b in query:
            ans.append(x.check(a, b))

        return ans