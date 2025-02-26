class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def division(divider: int) -> int:
            ret = 0

            for num in nums:
                ret += math.ceil(num / divider)

            return ret

        left = 1
        right = max(nums)

        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if division(mid) > threshold:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1

        return ans