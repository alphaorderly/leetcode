class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [0] * n

        count = 0
        dp[0] = 1

        new_count = 0

        for i in range(1, n):

            if i - delay >= 0:
                new_count = (new_count + dp[i - delay]) % MOD
            
            if i - forget >= 0:
                new_count = (new_count - dp[i - forget] + MOD) % MOD

            dp[i] = new_count

        ans = 0

        for i in range(n - forget, n):
            ans = (ans + dp[i]) % MOD

        return ans