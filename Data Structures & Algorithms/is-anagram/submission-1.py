class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_str = ''.join(sorted(s))
        second_str = ''.join(sorted(t))

        if first_str == second_str:
            return True
        return False