class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        ref = 0

        for num in target:
            if ref < num:
                ans += num - ref
            ref = num

        return ans