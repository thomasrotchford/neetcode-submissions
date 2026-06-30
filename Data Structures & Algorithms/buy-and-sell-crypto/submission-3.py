class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        sol=0
        buy=prices[0]

        for sell in prices:
            
            profit=sell-buy

            sol=max(profit,sol)

            buy=min(sell,buy)

            
        return sol