class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        cntr = Counter(s)

        odd_chars = [k for k, v in cntr.items() if v % 2 != 0]

        if len(odd_chars) > 1:
            return []

        center = odd_chars[0] if odd_chars else ''

        chars = []

        for k, v in cntr.items():
            chars.extend([k] * (v // 2)) 

        perm = list(permutations(chars, len(chars)))

        ans = set()

        for p in perm:
            x = ''.join(p) + center + ''.join(reversed(p))

            ans.add(x)

        return [i for i in ans]