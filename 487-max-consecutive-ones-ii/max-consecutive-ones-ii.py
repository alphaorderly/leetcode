class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # 0을 한 번도 안 뒤집었을 때의 연속 1의 길이
        consecutive_ones_no_flip = 0
        
        # 0을 최대 한 번 뒤집었을 때의 연속 1의 길이
        consecutive_ones_one_flip = 0
        
        # 전체 최대 길이
        max_ans = 0

        for num in nums:
            if num == 1:
                # 1을 만나면 두 상태 모두 1씩 증가
                consecutive_ones_no_flip += 1
                consecutive_ones_one_flip += 1
            else:  # num == 0
                # 0을 만나면, "한 번 뒤집은 상태"는
                # "이전까지 안 뒤집은 상태"에서 현재 0을 뒤집은 것이 됨
                consecutive_ones_one_flip = consecutive_ones_no_flip + 1
                
                # "안 뒤집은 상태"는 0으로 리셋
                consecutive_ones_no_flip = 0
            
            # 매 스텝마다 "한 번 뒤집은 상태"의 값으로 최대값 갱신
            max_ans = max(max_ans, consecutive_ones_one_flip)

        return max_ans