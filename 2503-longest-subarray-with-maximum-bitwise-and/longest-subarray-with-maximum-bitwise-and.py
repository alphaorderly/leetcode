class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mn, ma, mc = max(nums), 0, 0

        for num in nums:
            if num == mn:
                mc += 1
                ma = max(mc, ma)
            else:
                mc = 0

        return ma

