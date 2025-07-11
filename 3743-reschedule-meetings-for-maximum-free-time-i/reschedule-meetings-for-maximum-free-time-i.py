class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        last_end = 0
        time = []

        for s, e in zip(startTime, endTime):
            time.append(s - last_end)
            last_end = e

        if eventTime > last_end:
            time.append(eventTime - last_end)

        N = len(time)

        ans = window = sum(time[:min(k + 1, N)])

        for i in range(k + 1, N):
            window += time[i] - time[i - k - 1]
            ans = max(ans, window)

        return ans

