class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # only keep num and alphabets, cleaning spaces, colons etc
        cleaned = ''.join(c.lower() for c in s if c.isalnum())

        is_pal = True
        
        for i, j in zip(cleaned, reversed(cleaned)):
            if i != j:
                is_pal = False
                break
        
        return is_pal