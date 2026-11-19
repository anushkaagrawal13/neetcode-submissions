class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 2:
            return(nums[::-1])
        pref = [None] * n; suff = [None] * n; res = [None] * n
        pref[0] = 1
        suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return(res)