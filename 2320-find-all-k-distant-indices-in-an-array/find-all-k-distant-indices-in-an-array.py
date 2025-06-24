class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        N = len(nums)
        
        check = [0] * N

        for i, v in enumerate(nums):
            if v == key:
                check[max(0, i - k)] += 1

                if i + k + 1 < N:
                    check[i + k + 1] -= 1

        ans = []

        cnt = 0

        for i, v in enumerate(check):
            cnt += v

            if cnt > 0:
                ans.append(i)

        return ans