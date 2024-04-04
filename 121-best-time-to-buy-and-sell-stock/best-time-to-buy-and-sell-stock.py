class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        i=0
        j=1
        while i<len(prices) and j<len(prices):
            if prices[i]<prices[j]:
                ans=prices[j]-prices[i]
                profit=max(profit,ans)
                j+=1
            else:
                i=j
                j+=1
        return profit                