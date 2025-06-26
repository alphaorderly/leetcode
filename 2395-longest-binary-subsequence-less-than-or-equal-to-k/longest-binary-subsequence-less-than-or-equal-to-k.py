class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        value = 0
        count = 0

        N = len(s)

        for i in range(N - 1, -1, -1):
            position = N - i - 1

            if s[i] == '1':
                if value + (1 << position) <= k:
                    value += 1 << position
                    count += 1
            else:
                count += 1

        return count
