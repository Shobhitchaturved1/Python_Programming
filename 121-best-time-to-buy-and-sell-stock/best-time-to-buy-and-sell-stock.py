class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_profit=0
        buy=sell=prices[0]
        for i in prices:
            if i<buy:
                buy=i
                sell=i
            else:
                sell=i
            mx_profit=max(mx_profit,sell-buy)
        return mx_profit        