class Solution:
    def getSmallestString(self, s: str) -> str:
        N = len(s)

        s = list(s)

        for i in range(N - 1):
            if int(s[i]) % 2 == int(s[i + 1]) % 2:
                if int(s[i]) > int(s[i + 1]):
                    s[i], s[i + 1] = s[i + 1], s[i]
                    break

        return "".join(s)