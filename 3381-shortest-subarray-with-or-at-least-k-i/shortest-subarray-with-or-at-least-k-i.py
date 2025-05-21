from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        NUM_BITS = 32

        if k == 0:
            return 1

        bit_counts = [0] * NUM_BITS
        
        def get_window_or() -> int:
            current_or_val = 0
            for i in range(NUM_BITS):
                if bit_counts[i] > 0:
                    current_or_val |= (1 << i)
            return current_or_val

        n = len(nums)
        min_len_found = float('inf')
        left = 0

        for right in range(n):
            num_to_add = nums[right]
            for i in range(NUM_BITS):
                if (num_to_add >> i) & 1:
                    bit_counts[i] += 1
            
            while get_window_or() >= k and left <= right:
                current_len = right - left + 1
                min_len_found = min(min_len_found, current_len)
                
                num_to_remove = nums[left]
                for i in range(NUM_BITS):
                    if (num_to_remove >> i) & 1:
                        bit_counts[i] -= 1
                
                left += 1
        
        return min_len_found if min_len_found != float('inf') else -1