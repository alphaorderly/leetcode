class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        neg = 1

        if len(v2) > len(v1):
            v1, v2 = v2, v1
            neg *= -1


        for _ in range(len(v1) - len(v2)):
            v2.append(0)

        N = len(v1)

        for i in range(N):
            if v1[i] > v2[i]:
                return 1 * neg
            elif v1[i] < v2[i]:
                return -1 * neg

        return 0