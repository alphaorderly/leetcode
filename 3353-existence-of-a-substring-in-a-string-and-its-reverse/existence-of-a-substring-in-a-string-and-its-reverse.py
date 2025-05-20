class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        d = set()

        N = len(s)

        for i in range(N):
            if i == 0:
                d.add(s[:2])
            elif i == N - 1:
                x= s[-2:]
                if x[::-1] in d:
                    return True
            else:
                x = s[i - 1:i + 1]
                if x[::-1] in d:
                    return True

                d.add(s[i:i + 2])

        return False