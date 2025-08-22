class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        largest = 0

        ROW = len(mat)
        COL = len(mat[0])

        colIndex = [0] * ROW
        rowIndex = 0

        notchange = 0
        changed = False

        while True:
            changed = False
            while largest > mat[rowIndex][colIndex[rowIndex]]:
                colIndex[rowIndex] += 1
                changed = True
                if colIndex[rowIndex] >= COL:
                    return -1

            if not changed:
                notchange += 1
            else:
                notchange = 0

            if notchange > ROW:
                return mat[rowIndex][colIndex[rowIndex]]

            if largest < mat[rowIndex][colIndex[rowIndex]]:
                largest = mat[rowIndex][colIndex[rowIndex]]

            rowIndex = (rowIndex + 1) % ROW