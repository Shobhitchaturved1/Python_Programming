class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x=0
        dp=defaultdict(int)
        def helper(idx,buyorsell,k):
            if (idx,buyorsell,k) in dp:
                return dp[(idx,buyorsell,k)]
            if idx>=len(prices) or k==0:
                return 0
            if(buyorsell==0):
                buy=helper(idx+1,1,k)-prices[idx]
                nobuy=helper(idx+1,0,k)
                x=max(buy,nobuy)
            else:
                sell=helper(idx+1,0,k-1)+prices[idx]
                nosell=helper(idx+1,1,k)
                x=max(sell,nosell)
            dp[(idx,buyorsell,k)]=x    
            return x
        return helper(0,0,2)            