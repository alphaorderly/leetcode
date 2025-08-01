from math import factorial as f

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return [[f(i) // (f(j) * f(i-j)) for j in range(i+1)] for i in range(numRows)]