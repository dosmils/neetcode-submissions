class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            s = 'ñ'
            return s
        s = 'é'.join(i for i in strs)
        return s

    def decode(self, s: str) -> List[str]:
        if s == 'ñ':
            return []
        m = s.split('é')
        return m
