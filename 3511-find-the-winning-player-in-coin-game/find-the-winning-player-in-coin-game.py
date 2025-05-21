class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        turn = 'Bob'
        
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4

            turn = 'Bob' if turn == 'Alice' else 'Alice'

        return turn
