class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res,i = 0,0
        if len(nums) == 3:
            res = nums[i] + nums[i+1] + nums[i+2]
            if res == 0:
                return [nums]
            else:
                return []
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i -1]:
                continue
            
            l, r = i+1, len(nums) -1
            while l <r:
                tes = a + nums[l] + nums[r]
                if tes > 0:
                    r-=1
                elif tes < 0:
                    l +=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
        return res