class Solution:
    def minOperations(self, nums: List[int]) -> int:
        prev = None

        ans = 0

        for num in nums:
            if prev is None:
                prev = num
            elif prev != num:
                ans += 1
                prev = num

        return ans