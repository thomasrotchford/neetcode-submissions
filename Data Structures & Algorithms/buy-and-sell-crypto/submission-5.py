class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]

        profit = 0

        for sell in prices:

            neWprofit = sell - buy

            profit = max(profit,neWprofit)

            buy = min(buy,sell)
        
        return profit