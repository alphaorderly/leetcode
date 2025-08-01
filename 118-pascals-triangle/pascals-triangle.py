class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        ans = [
            [1], [1, 1]
        ]

        for row in range(2, numRows):
            app = []
            for col in range(row + 1):
                if col == 0 or col == row:
                    app.append(1)
                else:
                    app.append(ans[row - 1][col - 1] + ans[row - 1][col])
            ans.append(app)

        return ans
