class Solution:
    def findLHS(self, nums: List[int]) -> int:
        check = defaultdict(int)
        for num in nums:
            check[num] += 1

        ans = 0

        for num in nums:
            if num - 1 in check:
                ans = max(ans, check[num] + check[num-1])
            if num + 1 in check:
                ans = max(ans, check[num] + check[num+1])

        return ans
