class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROW = len(matrix)
        self.COL = len(matrix[0])

        self.partial = [
            [0] * self.COL for _ in range(self.ROW)
        ]

        self.partial[0][0] = matrix[0][0]

        for r in range(1, self.ROW):
            self.partial[r][0] = self.partial[r - 1][0] + matrix[r][0]

        for c in range(1, self.COL):
            self.partial[0][c] = self.partial[0][c - 1] + matrix[0][c]

        for r in range(1, self.ROW):
            for c in range(1, self.COL):
                self.partial[r][c] = self.partial[r - 1][c] + self.partial[r][c - 1] + matrix[r][c] - self.partial[r - 1][c - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        position = self.partial[row2][col2]

        if row1 > 0:
            position -= self.partial[row1 - 1][col2]

        if col1 > 0:
            position -= self.partial[row2][col1 - 1]

        if row1 > 0 and col1 > 0:
            position += self.partial[row1 - 1][col1 - 1]

        return position
