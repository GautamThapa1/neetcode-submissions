class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        string = ""

        for ch in digits:
            string += str(ch)

        num = int(string) + 1
        string = str(num)

        final = []
        for ch in string:
            final.append(int(ch))

        return final