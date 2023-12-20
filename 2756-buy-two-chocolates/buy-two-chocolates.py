class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sum=0
        prices.sort()
        if(len(prices)>=2):
            if (prices[0]+prices[1]<=money):
                return money-(prices[0]+prices[1])
        return money        