class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        # r = len(numbers) - 1
        while l<len(numbers):
            for r in range(len(numbers)-1,l-1, -1):
                if numbers[r] + numbers[l] == target:
                    return l+1,r+1
            
            l += 1