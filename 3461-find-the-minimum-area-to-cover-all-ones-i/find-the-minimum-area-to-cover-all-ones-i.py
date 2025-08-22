class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = [sum(r) for r in grid]
        cols = [sum(r) for r in list(zip(*grid))]

        rl = 0
        rr = len(rows) - 1

        cl = 0
        cr = len(cols) - 1

        while rows[rl] == 0:
            rl += 1

        while rows[rr] == 0:
            rr -= 1

        while cols[cl] == 0:
            cl += 1

        while cols[cr] == 0:
            cr -= 1

        return (rr - rl + 1) * (cr - cl + 1)