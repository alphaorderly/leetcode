class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        if not nums:
            return 0

        events = []
        cntr = Counter(nums)

        for num in nums:
            start = num - k  # Removed max(0, ...) to handle negative numbers correctly
            end = num + k + 1
            events.append((start, 1))
            events.append((end, -1))

        events.sort()  # Sorts by position, then by delta (-1 before 1 for same position)
        nums.sort()  # Sort nums for sequential processing

        E = len(events)
        N = len(nums)

        num_index = 0
        event_index = 0
        ans = 0
        acc = 0  # Active count: number of ranges covering the current position

        while event_index < E:
            current_pos = events[event_index][0]

            while event_index < E and events[event_index][0] == current_pos:
                acc += events[event_index][1]
                event_index += 1

            if event_index >= E:
                break

            interval_start = events[event_index - 1][0]
            interval_end = events[event_index][0] - 1

            ans = max(ans, min(acc, numOperations))

            while (
                num_index < N
                and nums[num_index] >= interval_start
                and nums[num_index] <= interval_end
            ):
                count = cntr[nums[num_index]]
                others = acc - count
                ans = max(ans, count + min(others, numOperations))
                num_index += 1

        return ans
