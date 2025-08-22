class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row_sum = [sum(row) for row in grid]
        transposed = zip(*grid)
        col_sum = [sum(col) for col in transposed]

        r_left = 0
        r_right = len(row_sum) - 1

        c_left = 0
        c_right = len(col_sum) - 1

        while row_sum[r_left] == 0:
            r_left += 1

        while row_sum[r_right] == 0:
            r_right -= 1

        while col_sum[c_left] == 0:
            c_left += 1

        while col_sum[c_right] == 0:
            c_right -= 1

        return (c_right - c_left + 1) * (r_right - r_left + 1)
