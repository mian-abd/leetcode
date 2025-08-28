class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        best = 1
        curr = 1
        for c in range(1, len(nums)):
            if nums[c] == nums[c-1]:
                continue
            if nums[c] == nums[c-1] +1:
                curr += 1
            else:
                best = max(curr, best)
                curr = 1
        
        return max(best,curr)