class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}

        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                if not stack: # empty or not
                    return False
                else:
                    popped = stack.pop()
                    if ch != pairs[popped]:
                        return False


        return not stack