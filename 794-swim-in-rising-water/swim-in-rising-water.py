class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N=len(grid)
        visit=set()
        minheap=[[grid[0][0],0,0]]#time,row,col
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while minheap:
            t,r,c=heapq.heappop(minheap)
            if r==N-1 and c==N-1:
                return t
            for dr,dc in directions:
                row,col=dr+r,dc+c
                if(0<=row<N and 0<=col<N and (row,col) not in visit):
                    visit.add((row,col))
                    heapq.heappush(minheap,[max(grid[row][col],t),row,col])        