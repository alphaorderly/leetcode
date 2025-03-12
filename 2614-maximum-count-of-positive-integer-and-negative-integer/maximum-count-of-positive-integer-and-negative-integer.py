class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        n = len(nums)
        
        # 각 숫자에 대해 리스트 전체를 다시 순회
        for i in range(n):
            for j in range(n):
                # i번째 숫자를 기준으로 확인
                if nums[i] > 0:
                    # j번째 숫자가 i번째와 동일한지 확인 (불필요한 연산)
                    if i == j:
                        pos += 1
                elif nums[i] < 0:
                    if i == j:
                        neg += 1
        
        return max(pos, neg)