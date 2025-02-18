class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashmap=defaultdict(int)
        ans=0
        for row in grid:
            hashmap[tuple(row)]+=1    
        for c in range(len(grid)):
            a=[]
            for r in range(len(grid)):    
                a.append(grid[r][c])
            ans+=hashmap[tuple(a)]      
        return ans    