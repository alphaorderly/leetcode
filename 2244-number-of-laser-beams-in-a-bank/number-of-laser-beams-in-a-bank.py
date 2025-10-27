class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        checker = "0" * len(bank[0])

        bank = [sum([int(x) for x in b]) for b in bank if b != checker]

        ans = 0

        for i in range(0, len(bank) - 1):
            ans += bank[i] * bank[i+1]

        return ans