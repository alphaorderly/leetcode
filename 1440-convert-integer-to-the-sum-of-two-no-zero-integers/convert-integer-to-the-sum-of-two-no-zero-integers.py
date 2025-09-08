class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        while True:
            a = random.randint(1, n - 1)
            b = n - a

            if str(a).count('0') == 0 and str(b).count('0') == 0:
                return [a, b]