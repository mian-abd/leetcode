class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False 
        for i in range(n -1):
            for j in range(i +1, n):
                if nums[i] == nums[j]:
                    return True        
        return False