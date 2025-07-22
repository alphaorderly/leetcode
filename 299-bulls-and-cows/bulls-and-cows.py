class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        contain = Counter(secret)

        bull = 0
        cows = 0

        for sch, gch in zip(secret, guess):
            if sch == gch:
                bull += 1
                contain[sch] -= 1

        for sch, gch in zip(secret, guess):
            if sch != gch and contain[gch] > 0:
                cows += 1
                contain[gch] -= 1

        
        return f'{bull}A{cows}B'