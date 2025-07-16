class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_count = 0
        odd_count = 0

        for i, num in enumerate(nums):
            if num % 2:
                odd_count += 1
            else:
                even_count += 1

        last_even = 0
        last_odd = 0

        for num in nums:
            if num % 2:
                last_odd = max(last_odd, last_even + 1)
            else:
                last_even = max(last_even, last_odd + 1)

        return max(even_count, odd_count, last_even, last_odd)