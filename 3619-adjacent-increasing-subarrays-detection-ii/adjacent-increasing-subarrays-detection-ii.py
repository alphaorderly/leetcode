class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                dp[i] += dp[i - 1]

        ans = 0

        for i in range(1, len(nums)):
            # From single increasing sequence
            # Simply cut large increaseing in half
            if dp[i] >= 2:
                ans = max(ans, dp[i] // 2)
            # From another increasing sequence
            # Frontal end should be in list and larger than backward one
            if i - dp[i] >= 0 and dp[i - dp[i]] >= dp[i]:
                ans = max(ans, dp[i])

        return ans