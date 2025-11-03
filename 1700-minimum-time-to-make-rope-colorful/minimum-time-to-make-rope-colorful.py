class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        curr = None

        ans = 0

        for i, v in enumerate(colors):
            if curr is None or colors[curr] != v:
                curr = i
            else:
                if neededTime[curr] < neededTime[i]:
                    ans += neededTime[curr]
                    curr = i
                else:
                    ans += neededTime[i]

        return ans

