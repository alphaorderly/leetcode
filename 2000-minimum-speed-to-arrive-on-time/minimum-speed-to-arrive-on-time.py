class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def calc_hour(speed: int) -> int:
            ret = 0

            for i, d in enumerate(dist):
                if i < len(dist) - 1:
                    ret += math.ceil(d / speed)
                else:
                    ret += d / speed

            return ret

        left = 1
        right = 10 ** 9

        ans = -1

        while left <= right:
            mid = (left + right) // 2

            takes = calc_hour(mid)

            if takes > hour:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1

        return ans