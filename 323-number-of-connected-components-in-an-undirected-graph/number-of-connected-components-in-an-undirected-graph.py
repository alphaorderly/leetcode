class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        check = [False] * n
        q = deque()

        ans = 0

        for i in range(n):
            if check[i]:
                continue

            ans += 1

            q.append(i)

            while q:
                n = q.popleft()
                check[n] = True

                for to in graph[n]:
                    if not check[to]:
                        q.append(to)

        return ans

