class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minima = float('inf')
        maxima = -float('inf')

        acc = 0
        ans = 0

        for index, num in enumerate(nums):
            acc += num
            if index == 0:
                ans = abs(acc)
            else:
                ans = max(ans, abs(acc), abs(acc - minima), abs(acc - maxima))
            minima = min(minima, acc)
            maxima = max(maxima, acc)

        return ans
        