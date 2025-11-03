class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack: List[int] = []
        ans = 0
        
        for i, c in enumerate(colors):
            if not stack or stack[-1][1] != c:
                stack.append((neededTime[i], c))
            else:
                if stack[-1][0] <= neededTime[i]:
                    ans += stack.pop()[0]
                    stack.append((neededTime[i], c))
                else:
                    ans += neededTime[i]

        return ans
