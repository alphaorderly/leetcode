class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N = len(nums)

        def to_bin(n: int) -> List[int]:
            ans = []

            while n:
                ans.append(n % 2)
                n //= 2

            return ans

        max_or = defaultdict(int)

        for num in nums:
            binary = to_bin(num)
            for i, v in enumerate(binary):
                max_or[i] += v

        max_or_value = 0

        for k, v in max_or.items():
            if v > 0:
                max_or_value += 2 ** k
        i_max_or = [0] * N

        i_max_or[0] = max_or_value

        for i in range(N - 1):
            binary = to_bin(nums[i])

            for k, v in enumerate(binary):
                max_or[k] -= v
                if max_or[k] == 0:
                    max_or_value -= 2 ** k * v

            i_max_or[i + 1] = max_or_value

        window = defaultdict(int)
        window_value = 0
        right = 0

        ans = []

        for left, left_value in enumerate(nums):
            if left == N - 1:
                break

            while right < N and window_value != i_max_or[left]:
                binary = to_bin(nums[right])
                for k, v in enumerate(binary):
                    if v == 0:
                        continue

                    if window[k] == 0:
                        window_value += 2 ** k

                    window[k] += 1

                right += 1

                if window_value == i_max_or[left]:
                    break

            ans.append(max(right - left, 1))

            left_binary = to_bin(nums[left])

            for k, v in enumerate(left_binary):
                if v == 0:
                    continue

                window[k] -= 1
                if window[k] == 0:
                    window_value -= 2 ** k

        ans.append(1)

        return ans
