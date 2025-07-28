class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0
        app = 0

        N = len(nums)

        maxOr = 0
        for num in nums:
            maxOr |= num

        def backtracking(last: int):
            nonlocal app, ans
            if last >= N:
                return

            for i in range(last, N):
                original_app = app
                app |= nums[i]
                if app == maxOr:
                    ans += 1
                backtracking(i + 1)
                app = original_app

        backtracking(0)

        return ans