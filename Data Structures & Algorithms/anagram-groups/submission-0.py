class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in result:
                result[key] = [] # creates index for each word
            result[key].append(s)
        return list(result.values()) 