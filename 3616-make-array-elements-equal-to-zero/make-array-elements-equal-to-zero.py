class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans = 0

        N = len(nums)

        prefix_sum = [0] * N
        suffix_sum = [0] * N

        for i in range(N):
            if i == 0:
                prefix_sum[i] = nums[i]
            else:
                prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        for i in range(N - 1, -1, -1):
            if i == N - 1:
                suffix_sum[i] = nums[i]
            else:
                suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        for index, num in enumerate(nums):
            if num == 0:
                if abs(prefix_sum[index] - suffix_sum[index]) == 1:
                    ans += 1
                elif prefix_sum[index] == suffix_sum[index]:
                    ans += 2

        return  ans