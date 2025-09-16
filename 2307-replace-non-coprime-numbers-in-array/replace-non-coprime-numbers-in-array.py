class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s = []

        for num in nums:
            if not s:
                s.append(num)
                continue

            while s:
                g = gcd(s[-1], num)
                if g > 1:
                    v = s.pop()
                    num = v * num // g
                else:
                    break

            s.append(num)

        return s