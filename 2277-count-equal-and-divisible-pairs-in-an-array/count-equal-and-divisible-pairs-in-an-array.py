import math
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = 0

        gcd_counts = defaultdict(lambda: defaultdict(int)) 

        for j in range(N):
            val = nums[j]
            
            g_j = math.gcd(j, k)
            
            for stored_g_i, count in gcd_counts[val].items():
                if (stored_g_i * g_j) % k == 0:
                    ans += count
            
            gcd_counts[val][g_j] += 1
            
        return ans

