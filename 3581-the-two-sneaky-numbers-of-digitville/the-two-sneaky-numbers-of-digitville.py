class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cntr = collections.Counter(nums)

        return [i for i, v in cntr.items() if v > 1]