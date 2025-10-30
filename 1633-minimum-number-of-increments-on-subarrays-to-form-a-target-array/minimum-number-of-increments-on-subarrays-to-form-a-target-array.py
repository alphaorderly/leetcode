class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans, val = 0, 0

        for num in target:
            if val < num:
                ans += num - val
            val = num

        return ans