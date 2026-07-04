class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        input1 = sorted(s)
        input2 = sorted(t)
        if input1 != input2:
            return False
        return True
        