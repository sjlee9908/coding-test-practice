class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0

        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                result += prices[i+1]-prices[i]

        return result

print(Solution.maxProfit("asd", [7,1,5,3,6,4]))