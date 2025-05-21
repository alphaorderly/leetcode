class Solution:
    def minChanges(self, n: int, k: int) -> int:
        nn = [0] * 32

        kk = [0] * 32

        for i in range(32):
            if n & (2 ** i):
                nn[i] = 1

            if k & (2 ** i):
                kk[i] = 1

        ans = 0

        for i in range(32):
            if nn[i] == 0 and kk[i] == 1:
                return -1
            elif nn[i] == 1 and kk[i] == 0:
                ans += 1

        return ans