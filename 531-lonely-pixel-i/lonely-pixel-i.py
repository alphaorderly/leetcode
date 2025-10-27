class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        R = len(picture)
        C = len(picture[0])

        rows = [0] * R
        cols = [0] * C

        for r in range(R):
            for c in range(C):
                if picture[r][c] == 'B':
                    rows[r] += 1
                    cols[c] += 1

        ans = 0

        for r in range(R):
            for c in range(C):
                if picture[r][c] == 'B' and rows[r] == 1 and cols[c] == 1:
                    ans += 1

        return ans