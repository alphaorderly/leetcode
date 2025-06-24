class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        ans = 0

        for i in range(N - 2):
            for j in range(i + 2, N):
                limit = target - nums[i] - nums[j]
                place = bisect_left(nums, limit)
                upper_bound = min(j, place)

                if upper_bound > i+1:
                    ans += upper_bound - (i + 1)

        return ans