class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = set(s)
        t_hash = set(t)
        if len(s) > len(t):
            for el in s_hash:
                if s.count(el) != t.count(el):
                    return False
            return True
        else:
            for el in t_hash:
                if t.count(el) != s.count(el):
                    return False
            return True

        