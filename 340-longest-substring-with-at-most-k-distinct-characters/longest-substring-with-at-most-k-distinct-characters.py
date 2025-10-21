class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window = defaultdict(int)

        left, ans, size = 0, 0, 0

        for right, value in enumerate(s):
            window[value] += 1
            size += 1

            while left <= right and len(window.keys()) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
                size -= 1

            ans = max(ans, size)

        return ans
