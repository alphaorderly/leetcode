class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        directions = [
            [-1, -1],
            [-1, 1],
            [1, 1],
            [1, -1]
        ]

        ROW = len(grid)
        COL = len(grid[0])

        def check(r: int, c: int) -> int:
            if 0 <= r < ROW and 0 <= c < COL:
                return True
            return False

        @cache
        def dp(r: int, c: int, target: int, direction: int, changed: bool):
            if not check(r, c):
                return 0
            if grid[r][c] != target:
                return 0

            ans = dp(r + directions[direction][0], c + directions[direction][1], 2 - target, direction, changed) + 1
            if not changed:
                direction = (direction + 1) % 4
                ans = max(ans, dp(r + directions[direction][0], c + directions[direction][1], 2 - target, direction, True) + 1)

            return ans

        ans = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    for d in range(4):
                        to = directions[d]
                        tr = r + to[0]
                        tc = c + to[1]

                        ans = max(ans, dp(tr, tc, 2, d, False) + 1)
   

        return ans

        return 1

