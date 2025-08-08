class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1

        probability = [
            [100, 0],
            [75, 25],
            [50, 50],
            [25, 75]
        ]

        cache = {}

        def dp(a: int, b: int) -> int:
            if a <= 0 and b <= 0:
                return 0.5
            
            if a <= 0:
                return 1

            if b <= 0:
                return 0

            if (a, b) in cache:
                return cache[(a, b)]

            ans = 0

            for am, bm in probability:
                ans += dp(a - am, b - bm)

            cache[(a, b)] = ans / 4

            return ans / 4

        return dp(n, n) 