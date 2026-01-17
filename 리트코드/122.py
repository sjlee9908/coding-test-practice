class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        tv = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                tv += prices[i] - prices[i-1]
        return tv