class Solution:
    def maxSum(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        s = set(nums)
        p = [n for n in s if n > 0]

        if len(p) > 0:
            return sum(p)
        else:
            return sorted(nums)[-1]