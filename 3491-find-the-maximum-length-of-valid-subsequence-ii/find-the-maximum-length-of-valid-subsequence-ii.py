class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [defaultdict(int) for _ in range(k)]

        max_len = 0

        for num in nums:
            rem = num % k
            for s in range(k):
                prev_rem = (s - rem + k) % k
                dp[s][rem] = dp[s][prev_rem] + 1
                max_len = max(max_len, dp[s][rem])

        return max_len