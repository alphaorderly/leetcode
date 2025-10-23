class Solution:
    def hasSameDigits(self, s: str) -> bool:

        def number(c: str):
            return ord(c) - ord('0')

        while len(s) != 2:
            N = len(s)
            ns = ""

            for i in range(N - 1):
                ns = ns + chr(((number(s[i]) + number(s[i + 1])) % 10) + ord('0'))

            s = ns

        return s[0] == s[1]