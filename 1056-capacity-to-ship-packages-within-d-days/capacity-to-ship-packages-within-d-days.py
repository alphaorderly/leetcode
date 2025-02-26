class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def d(ship: int) -> int:
            acc = 0
            day = 1

            for w in weights:
                if acc + w > ship:
                    acc = w
                    day += 1
                else:
                    acc += w

            return day

        left = max(weights)
        right = sum(weights)

        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if d(mid) > days:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1

        return ans
