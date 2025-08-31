class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        mini, base, area, res =0,0,0,0
        while l<r:
            mini = min(height[l], height[r])
            base = r - l
            area = base*mini
            res = max(area, res)
            if height[l] < height[r]:
                l +=1
            else:
                r -= 1
        return res