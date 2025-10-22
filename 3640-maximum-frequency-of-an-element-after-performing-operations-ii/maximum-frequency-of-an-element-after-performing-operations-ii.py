class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        events = []

        cntr = Counter(nums)

        for num in nums:
            start = max(0, num - k)
            end = num + k + 1

            events.append((start, 1))
            events.append((end, -1))

        E = len(events)
        N = len(nums)

        events.sort()
        nums.sort()

        num_index = 0
        event_index = 0

        ans = 0

        acc = 0

        while event_index < E:
            current_event_time = events[event_index][0]

            while event_index < E and events[event_index][0] == current_event_time:
                acc += events[event_index][1]
                event_index += 1

            if event_index >= E:
                break

            event_start = events[event_index - 1][0]
            event_end = events[event_index][0] - 1

            ans = max(ans, min(acc, numOperations))

            while num_index < N and nums[num_index] >= event_start and nums[num_index] <= event_end:
                count = cntr[nums[num_index]]
                left = acc - count
                ans = max(ans, count + min(left, numOperations))
                num_index += 1

        return ans