class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        
        d_n = [nums[i*3:i*3+3] for i in range(len(nums) // 3)]

        for d in d_n:
            if d[2] - d[0] > k:
                return []

        return d_n