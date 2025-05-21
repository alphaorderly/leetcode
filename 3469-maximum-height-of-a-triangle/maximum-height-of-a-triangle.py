class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        i = 1

        a = b = 0

        while True:
            if i % 2 == 1:
                a += i
            else:
                b += i

            if (red >= a and blue >= b) or (blue >= a and red >= b):
                i += 1
            else:
                return i - 1
