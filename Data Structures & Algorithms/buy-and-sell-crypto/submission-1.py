class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy=prices[0]
        profit=0

        for sell in prices:

            #max of current profit and previous profit
            profit=max(profit,sell-buy)
            
            #min of r and l
            buy=min(buy,sell)

        return profit