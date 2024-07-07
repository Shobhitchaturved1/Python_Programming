class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=float("-inf")
        maxi,mini=prices[-1],prices[-1]
        for i in range(len(prices)-2,-1,-1):
            if prices[i]<maxi:
                ans=max(ans,maxi-prices[i])
            else:
                maxi=prices[i]
        return ans if ans!=float("-inf") else 0        