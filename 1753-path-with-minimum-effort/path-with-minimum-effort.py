class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROW,COL=len(heights),len(heights[0])
        minHeap=[[0,0,0]] #[diff,r,c]
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        visit=set()
        while minHeap:
            diff,r,c=heapq.heappop(minHeap)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if (r,c)==(ROW-1,COL-1):
                return diff   
            for dr,dc in directions:
                nr,nc=dr+r,c+dc
                if(nr<0 or nr==ROW or 
                   nc<0 or nc==COL or
                   (nr,nc) in visit):
                   continue
                newdiff=max(diff,abs(heights[r][c]-heights[nr][nc]))   
                heapq.heappush(minHeap,[newdiff,nr,nc])       