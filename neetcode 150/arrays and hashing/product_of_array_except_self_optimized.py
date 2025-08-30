class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = 1
        res = [1] * n

        for i in range(n):
            res[i] = pre
            pre = pre * nums[i]
           
        post = 1
        for i in range(n -1, -1, -1):
            res[i] = post * res[i]
            post = post * nums[i]
            
        return res