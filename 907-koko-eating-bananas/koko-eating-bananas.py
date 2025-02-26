class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def koko(eating: int) -> int:
            return sum(math.ceil(p / eating) for p in piles)

        left = 1
        right = max(piles)

        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if koko(mid) <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans