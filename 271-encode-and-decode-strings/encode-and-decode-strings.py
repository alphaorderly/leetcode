from urllib.parse import quote, unquote

class Codec:
    def encode(self, strs: List[str]) -> str:
        return ' '.join([quote(s) for s in strs])

    def decode(self, s: str) -> List[str]:
        return [unquote(i) for i in s.split(' ')]
