class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        placement = defaultdict(list)
        N = len(source)

        for i, s in enumerate(source):
            placement[s].append(i)

        print(placement)

        ans = 1
        position = 0

        for ch in target:
            if ch not in placement:
                return -1

            current_index = bisect_left(placement[ch], position)

            if current_index >= len(placement[ch]):
                ans += 1
                position = 0
                current_index = bisect_left(placement[ch], position)

            position = placement[ch][current_index] + 1

        return ans