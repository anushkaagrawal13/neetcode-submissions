class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        slist = []; tlist = []
        for char in s:
            slist.append(char)
        for char in t:
            tlist.append(char)
        if sorted(slist) == sorted(tlist):
            return True
        return False