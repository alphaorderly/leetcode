class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        left = [[0] * 3 for _ in range(n)]
        right = [[0] * 3 for _ in range(n)]

        num, mask, count = 0, 0, 0
        for i in range(n - 1):
            # Mask the character at s[i]
            binary = 1 << (ord(s[i]) - ord("a"))

            # check there is already this character in the mask
            if not (mask & binary):
                # Add new character
                count += 1
                # There is still space in the current segment
                if count <= k:
                    mask |= binary
                # Or else need to create a new segment
                else:
                    num += 1
                    mask = binary
                    count = 1

            left[i + 1] = [num, mask, count]

        # Same process from the right side
        num, mask, count = 0, 0, 0
        for i in range(n - 1, 0, -1):
            binary = 1 << (ord(s[i]) - ord("a"))
            if not (mask & binary):
                count += 1
                if count <= k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1
            right[i - 1] = [num, mask, count]   

        max_val = 0
        for i in range(n):
            # Start from the baseline: completed segments on the left + right, and
            # +2 for the two *current* open segments that touch position i (left part and right part).
            seg = left[i][0] + right[i][0] + 2

            # Union of distinct letters currently used by the left and right open segments.
            tot_mask = left[i][1] | right[i][1]
            tot_count = bin(tot_mask).count("1")

            # Case 1) Both sides are already "full" (k distinct each).
            # If there exists at least one unused letter overall (tot_count < 26),
            # we can change s[i] to a brand-new letter, which *forces* an extra cut,
            # yielding one more partition.
            if left[i][2] == k and right[i][2] == k and tot_count < 26:
                seg += 1

            # Case 2) Otherwise, if we can pick a replacement for s[i] so that the combined
            # distinct count of left+right (including this replacement) is <= k,
            # the two open segments can merge into a single segment, so we *reduce* one partition.
            elif min(tot_count + 1, 26) <= k:
                seg -= 1

            # Keep the best possible answer over all i.
            max_val = max(max_val, seg)

        return max_val
