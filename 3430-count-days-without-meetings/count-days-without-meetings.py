class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        start = meetings[0][0]
        end = meetings[0][1]
        N = len(meetings)

        for i in range(1, N):
            node_start, node_end = meetings[i]

            if end >= node_start:
                end = max(end, node_end)
            else:
                days -= end - start + 1
                start = node_start
                end = node_end

        days -= end - start + 1

        return days