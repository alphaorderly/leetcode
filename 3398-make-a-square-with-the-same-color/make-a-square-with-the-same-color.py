class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        arr = [
            [0, 0],
            [0, 0]
        ]

        for r in range(2):
            for c in range(2):
                for i in range(2):
                    for j in range(2):
                        arr[r][c] += 1 if grid[r + i][c + j] == 'W' else 0

        for r in range(2):
            for c in range(2):
                if arr[r][c] <= 1 or arr[r][c] >= 3:
                    return True

        return False