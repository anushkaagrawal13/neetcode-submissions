class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return(True)
        alnum = "".join([char for char in s if char.isalnum()])
        stripped = alnum.lower().strip()
        
        p1 = 0; p2 = len(stripped) - 1
        while p1 <= p2:
            if stripped[p1] != stripped[p2]:
                return(False)
            p1 += 1
            p2 -= 1
        return(True)