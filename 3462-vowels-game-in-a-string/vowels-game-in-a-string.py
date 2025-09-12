vowels = {'a', 'e', 'i', 'o', 'u'}

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for v in vowels:
            if v in s:
                return True

        return False