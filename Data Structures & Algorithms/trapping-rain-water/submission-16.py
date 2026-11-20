class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        if n == 1 or n == 2:
            return 0
        l = [None] * n
        r = [None] * n
        l[0] = height[0]
        r[n - 1] = height[n - 1]
        rain = 0
        for i in range(1, n):
            l[i] = max(l[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            r[i] = max(r[i + 1], height[i])
        for i in range(0, n):
            rain += min(l[i], r[i]) - height[i]
        return rain