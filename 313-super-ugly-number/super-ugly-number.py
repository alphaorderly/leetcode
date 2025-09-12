class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ans = [1]
        h = [(v, i) for i, v in enumerate(primes)]
        P = len(primes)
        indices = [0] * P

        heapify(h)

        while len(ans) < n:
            v, i = heappop(h)

            if v != ans[-1]:
                ans.append(v)

            indices[i] += 1

            heappush(h, (ans[indices[i]] * primes[i], i))

        return ans[-1]
