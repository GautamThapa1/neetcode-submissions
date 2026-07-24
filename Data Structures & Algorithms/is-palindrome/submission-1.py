class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # only keep num and alphabets, cleaning spaces, colons etc
        cleaned = ''.join(c.lower() for c in s if c.isalnum())

        i, j = 0, len(cleaned) -1

        while i < j:
            if cleaned[i] != cleaned[j]:
                return False
            i += 1
            j -= 1
        
        return True
