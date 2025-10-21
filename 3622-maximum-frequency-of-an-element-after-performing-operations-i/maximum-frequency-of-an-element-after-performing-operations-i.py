class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        cntr = Counter(nums)
        N = len(nums)
        ans = 0

        space = [i for i in range(nums[0], nums[-1] + 1)]

        for i, v in enumerate(space):
            left_bound = bisect_left(nums, v - k)
            right_bound = bisect_right(nums, v + k)

            if right_bound == N or nums[right_bound] > v + k:
                right_bound -= 1

            ans = max(ans, cntr[v] + min(right_bound - left_bound + 1 - cntr[v], numOperations))

        return ans