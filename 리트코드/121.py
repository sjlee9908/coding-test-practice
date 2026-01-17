import heapq
import sys


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        profit_list = [sys.maxsize]

        for i in range(1, len(prices)):

            if profit + (prices[i] - prices[i - 1]) > 0:
                heapq.heappush(profit_list, -profit)
                profit += (prices[i] - prices[i - 1])

            else:
                heapq.heappush(profit_list, -profit)
                if i != len(prices) - 1:
                    profit = 0

        return max(profit, -heapq.nsmallest(1, profit_list)[0])


print(Solution.maxProfit(None, prices=[7, 1, 5, 3, 6, 4]))
