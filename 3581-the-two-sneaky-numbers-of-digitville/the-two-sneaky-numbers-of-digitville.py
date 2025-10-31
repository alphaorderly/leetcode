class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        check = set()

        for num in nums:
            if num in check:
                ans.append(num)
            else:
                check.add(num)

        return ans