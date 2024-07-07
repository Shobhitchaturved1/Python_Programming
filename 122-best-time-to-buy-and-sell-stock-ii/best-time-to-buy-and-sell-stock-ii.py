class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell=prices[0],prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i-1]>prices[i]:
                profit+=sell-buy
                buy=prices[i]
                sell=prices[i]
            else:
                sell=prices[i]
        return profit+sell-buy          
