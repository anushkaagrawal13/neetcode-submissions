class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in set("([{"):
                stack.append(c)
            if c in set(")]}"):
                if not stack:
                    return False
                first = stack.pop()
                if first == "(" and c != ")":
                    return False
                elif first == "{" and c != "}":
                    return False
                elif first == "[" and c != "]":
                    return False
        if stack:
            return False
        return True
