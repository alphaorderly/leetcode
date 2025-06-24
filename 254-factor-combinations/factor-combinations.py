from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        # 결과를 저장할 ans를 set으로 초기화하여 중복을 방지합니다.
        ans = set()
        app = []

        def backtracking(v: int, last: int):
            if v == 1:
                if len(app) > 1:
                    ans.add(tuple(app))
                return 

            if len(app) > 0:
                 ans.add(tuple(app + [v]))


            for div in range(last, int(v**0.5) + 1):
                if v % div != 0:
                    continue

                app.append(div)
                backtracking(v // div, div)
                app.pop()


        backtracking(n, 2)

        return [list(item) for item in ans]