class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set(nums)
        p = [n for n in s if n > 0]

        if len(p) > 0:
            return sum(p)
        else:
            return sorted(nums)[-1]