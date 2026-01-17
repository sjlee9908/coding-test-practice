import sys

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = sys.maxsize  #시스템상의 최대값으로 설정

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)

        return profit

sol = Solution()
print(sol.maxProfit([2,4,1]))