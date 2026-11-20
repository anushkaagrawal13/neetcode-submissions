class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        maxSell = [None] * n
        maxSell[n - 1] = prices[n - 1]
        maxProfit = 0
        for i in range(n - 2, -1, -1):
            maxSell[i] = max(maxSell[i + 1], prices[i])
        for i in range(0, n):
            profit = maxSell[i] - prices[i]
            maxProfit = max(profit, maxProfit)
        return maxProfit
