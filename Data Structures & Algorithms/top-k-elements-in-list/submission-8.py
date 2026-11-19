from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = defaultdict(int)
        for num in nums:
            numdict[num] = numdict[num] + 1 if numdict[num] is not None else 1
        return sorted(numdict, key=numdict.get)[::-1][:k]