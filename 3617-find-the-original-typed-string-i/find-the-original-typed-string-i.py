class Solution:
    def possibleStringCount(self, word: str) -> int:
        x = []

        prev = None
        cnt = 0

        for ch in word:
            if prev is None:
                prev = ch
                cnt = 1
            elif prev != ch:
                x.append([prev, cnt])
                prev = ch
                cnt = 1
            else:
                cnt += 1

        x.append([prev, cnt])

        ans = 0

        for _, c in x:
            ans += c - 1

        return ans + 1