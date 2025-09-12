class Solution:
    def doesAliceWin(self, s: str) -> bool:

        vowel_count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for ch in s:
            if ch in vowels:
                vowel_count += 1

        if vowel_count == 0:
            return False

        return True