class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        N = len(points)

        maxR = max(points, key=lambda k: k[1])[1]

        points = [(c, maxR - r) for c, r in points]

        points.sort()

        print(points)

        ans = 0

        for i in range(N - 1):
            y = float('inf')
            for j in range(i + 1, N):
                if points[i][1] <= points[j][1] and y > points[j][1]:
                    ans += 1
                    y = points[j][1]

        return ans
