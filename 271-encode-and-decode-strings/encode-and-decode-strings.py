class Codec:
    def encode(self, strs: List[str]) -> str:
        return 'ㅁ'.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split('ㅁ')
