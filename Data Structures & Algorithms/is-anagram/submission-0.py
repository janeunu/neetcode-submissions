class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = sorted(s)
        hash2 = sorted(t)
        if hash1 == hash2:
            return True
        return False