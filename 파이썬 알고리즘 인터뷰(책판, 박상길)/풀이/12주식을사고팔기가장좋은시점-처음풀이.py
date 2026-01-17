class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if sorted(prices, reverse=True) == prices:
            return 0

        min_value1 = min(prices[:-1])
        max_value1 = max(prices[prices.index(min_value1):])
        v1 = max_value1 - min_value1

        max_value2 = max(prices[1:])
        min_value2 = min(prices[:prices[1:].index(max_value2)+1])

        v2 = max_value2-min_value2
        print(v1, v2)

        if v1 < v2:
            return v2
        else:
            return v1

