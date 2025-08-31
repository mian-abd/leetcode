class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        mini, final, base, result = 0,0,0,0
        for i in range(len(height) -1):
            r = len(height) -1
            while l< r:
                mini = min(height[l], height[r])
                base = r - l
                result = base*mini
                if final < result:
                    final = result
                r -= 1
            l += 1
        return final