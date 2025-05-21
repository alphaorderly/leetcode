class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans = 0

        N = len(colors)

        for i in range(N):
            if colors[i] != colors[(i - 1 + N) % N] and colors[i] != colors[(i + 1) % N]:
                ans += 1

        return ans