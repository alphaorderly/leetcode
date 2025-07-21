class Solution:
    def makeFancyString(self, s: str) -> str:
        acc = []
        cnt = 0
        prev = None

        for ch in s:
            if prev is None:
                prev = ch
                cnt = 1
            elif prev != ch:
                acc.append((prev, cnt))
                prev = ch
                cnt = 1
            else:
                cnt += 1

        if cnt > 0:
            acc.append((prev, cnt))

        ans = ''.join([ch * min(n, 2) for ch, n in acc])

        return ans