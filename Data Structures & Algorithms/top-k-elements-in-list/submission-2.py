class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        sol = []

        # count the frequency
        for i in nums:
            if i not in result:
                result[i] = 0
            result[i] += 1
        
        # creating frequency and number pair
        frq = []
        for key, value in result.items():
            frq.append([value, key])
        frq.sort(reverse=True)

        for i in range(k):
            sol.append(frq[i][1])
        return sol
            
