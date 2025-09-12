class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ROW = len(mat)
        COL = len(mat[0])

        left_side = [[0] * COL for _ in range(ROW)]

        for r in range(ROW):
            v = 0
            for c in range(COL):
                if mat[r][c]:
                    v += 1
                else:
                    v = 0

                left_side[r][c] = v

        ans = 0

        for r in range(ROW):
            for c in range(COL):

                if not left_side[r][c]:
                    continue

                ans += left_side[r][c]
                v = left_side[r][c]

                for tr in range(r - 1, -1, -1):
                    v = min(v, left_side[tr][c])
                    if v == 0:
                        break
                    ans += v

        return ans

                


        return 1