class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        N = len(s)

        ans = ""

        for i, ch in enumerate(s):
            ans = ans + s[(i + k) % N]

        return ans