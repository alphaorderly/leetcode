class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)

        back = [0] * N
        back[-1] = nums[-1]

        for i in range(N - 2, -1, -1):
            back[i] = max(back[i + 1], nums[i])

        forward = [0] * N
        forward[0] = nums[0]

        for i in range(1, N):
            forward[i] = max(forward[i - 1], nums[i])

        ans = 0

        for i in range(1, N - 1):
            x = (forward[i - 1] - nums[i]) * back[i + 1]

            ans = max(ans, x)

        return ans