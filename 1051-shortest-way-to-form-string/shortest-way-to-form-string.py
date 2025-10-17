from collections import defaultdict
from bisect import bisect_left

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if not target:
            return 0

        placement = defaultdict(list)
        for i, s in enumerate(source):
            placement[s].append(i)

        ans, position = 1, 0
        for ch in target:
            if ch not in placement:
                return -1

            idxs = placement[ch]
            j = bisect_left(idxs, position)
            if j == len(idxs):
                ans += 1          # 새 라운드 시작
                position = 0
                j = bisect_left(idxs, position)

            position = idxs[j] + 1

        return ans
