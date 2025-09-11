class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {}

        for i, c in enumerate(s):
            if c.lower() in {'a', 'e', 'i', 'o', 'u'}:
                vowels[i] = c

        vi = list(vowels.items())

        vi.sort(key=lambda i: ord(i[1]))

        ans = ""

        vowelIndex = 0

        for i, c in enumerate(s):
            if c.lower() not in {'a', 'e', 'i', 'o', 'u'}:
                ans = ans + c
            else:
                ans = ans + vi[vowelIndex][1]
                vowelIndex += 1

        return ans
