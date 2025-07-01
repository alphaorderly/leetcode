class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = None
        cnt = 0

        check = []

        for ch in word:
            if prev != ch:
                if prev is not None:
                    check.append((prev, cnt))
                prev = ch
                cnt = 1
            elif prev == ch:
                cnt += 1

        check.append((prev, cnt))

        ans = 1
        p = 0

        for _, v in check:
            if v > 1:
                ans += v - 1

        return ans