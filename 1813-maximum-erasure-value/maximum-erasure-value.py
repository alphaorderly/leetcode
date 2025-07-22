class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = set()
        ans = window_size = left = 0

        for right, value in enumerate(nums):
            while value in window and left < right:
                window.remove(nums[left])
                window_size -= nums[left]
                left += 1

            window.add(value)
            window_size += value

            ans = max(ans, window_size)

        return ans

