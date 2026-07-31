class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            
            sum = int((left + right) / 2)
            
            if nums[sum] == target:
                return sum
            elif nums[sum] > target:
                right = sum - 1
            else:
                left = left + 1

        return -1 