class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr = defaultdict(set)

        for w in dictionary:
            self.abbr[(w[0], w[-1], len(w))].add(w)

    def isUnique(self, word: str) -> bool:
        if (word[0], word[-1], len(word)) not in self.abbr:
            return True

        if len(self.abbr[(word[0], word[-1], len(word))]) == 1 and word in self.abbr[(word[0], word[-1], len(word))]:
            return True

        return False

