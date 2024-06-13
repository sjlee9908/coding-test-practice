class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i,v in enumerate(prices):
            if i == len(prices)-1:
                break
            if v < prices[i+1]:
                profit += (prices[i+1]-v)

        return profit

print(Solution.maxProfit("asd", [7,1,5,3,6,4]))