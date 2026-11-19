class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sortnums = sorted(list(set(nums)))
        run = []
        runlen = 0
        curlen = 0
        cur = []
        print(sortnums)
        for num in sortnums:
            if not cur:
                cur.append(num)
                curlen = 1
            else:
                if num == cur[-1] + 1:
                    cur.append(num)
                    curlen += 1
                else:
                    cur = [num]
                    curlen = 1
            if curlen > runlen:
                runlen = curlen
                run = cur
        return runlen