class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        target = set([i for i in range(1, k + 1)])
        ans = 0

        while True:
            x = nums.pop()
            if x in target:
                target.remove(x)

            ans += 1
            if len(target) == 0:
                return ans