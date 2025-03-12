class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left = bisect_left(nums, 0)
        right = bisect_right(nums, 0)

        N = len(nums)

        pos = N - right
        neg = left

        return pos if pos > neg else neg