class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        check = '0' * len(bank[0])

        bank = [b for b in bank if b != check]

        N = len(bank)

        ans = 0

        for i in range(N - 1):
            ans += bank[i].count("1") * bank[i + 1].count("1")

        return ans