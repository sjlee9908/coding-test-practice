class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))