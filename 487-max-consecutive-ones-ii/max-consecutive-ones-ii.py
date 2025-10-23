class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        N = len(nums)

        cache = {}

        def dp(index: int, flipped: bool) -> int:
            if index == N:
                return 0

            if nums[index] == 0:
                if flipped:
                    return 0

                if (index, flipped) in cache:
                    return cache[(index, flipped)]

                flip = dp(index + 1, True) + 1

                cache[(index, flipped)] = flip

                return flip

            if (index, flipped) in cache:
                return cache[(index, flipped)]

            value = dp(index + 1, flipped) + 1

            cache[(index, flipped)] = value

            return dp(index + 1, flipped) + 1

        ans = 0

        for i in range(N):
            ans = max(ans, dp(i, False))

        return ans