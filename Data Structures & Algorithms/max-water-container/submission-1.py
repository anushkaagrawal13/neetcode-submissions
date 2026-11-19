class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0 or n == 1:
            return 0
        l = 0
        r = n - 1
        dist = n - 1
        maxArea = 0
        while l < r:
            lh = heights[l]; rh = heights[r]
            area = (lh if lh < rh else rh) * dist
            maxArea = max(area, maxArea)
            if lh < rh: 
                l += 1
                dist -= 1
            else:
                r -= 1
                dist -= 1
        return maxArea