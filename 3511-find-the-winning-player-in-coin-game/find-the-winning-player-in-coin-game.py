class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        s = x
        t = y // 4

        m = min(s, t)

        return 'Alice' if m % 2 else 'Bob'