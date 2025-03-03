class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxprofit=0
        for i in prices:
            cost=i-mini
            maxprofit=max(maxprofit,cost)
            mini=min(mini,i)
        return maxprofit    