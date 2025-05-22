class Solution:
    def maxLength(self, nums: List[int]) -> int:
        window = deque()

        N = len(nums)

        def cd(l: List[int]) -> int:
            if len(l) == 1:
                return l[0]

            N = len(l)
            val = gcd(l[0], l[1])

            for i in range(1, N - 1):
                val = gcd(val, l[i + 1])

            return val

        def cm(l: List[int]) -> int:
            if len(l) == 1:
                return l[0]

            N = len(l)
            val = lcm(l[0], l[1])

            for i in range(1, N - 1):
                val = lcm(val, l[i + 1])

            return val

        cnt = 0
        ans = 0

        for right in range(N):
            window.append(nums[right])
            cnt += 1

            while len(window) > 1 and prod(window) != cd(window) * cm(window):
                window.popleft()
                cnt -= 1

            ans = max(ans, cnt)

        return ans
