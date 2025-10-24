class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def check(number: int) -> bool:
            s = str(number)

            c = Counter(s)

            for key, value in c.items():
                key = int(key)
                if key != value:
                    return False

            return True
        n += 1

        while True:
            if check(n):
                return n
            n += 1

        return ""