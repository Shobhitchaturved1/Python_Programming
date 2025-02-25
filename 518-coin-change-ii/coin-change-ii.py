class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}
        def dfs(idx,a):
            if (idx,a) in cache:
                return cache[(idx,a)]
            if a==amount:
                return 1
            if a>amount:
                return 0
            if idx==len(coins):
                return 0
            cache[(idx,a)]=dfs(idx,a+coins[idx])+dfs(idx+1,a)            
            return cache[(idx,a)]
        return dfs(0,0)    