class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []
        app = []

        N = len(word)

        def backtracking(index: int) -> None:
            if index >= N:
                a = ''.join(app)
                ans.append(a)
                return

            app.append(word[index])
            backtracking(index + 1)
            app.pop()

            for i in range(index, N):
                app.append(str(i - index + 1))
                if i + 1 < N:
                    app.append(word[i + 1])
                backtracking(i + 2)
                if i + 1 < N:
                    app.pop()
                app.pop()

        backtracking(0)

        return ans
