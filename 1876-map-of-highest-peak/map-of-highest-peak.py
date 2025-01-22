class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROW,COL=len(isWater),len(isWater[0])
        q=deque()
        visit=set()
        for r in range(ROW):
            for c in range(COL):
                if isWater[r][c]==1:
                    q.append([r,c]) 
                    visit.add((r,c))  
        direction=[[1,0],[-1,0],[0,1],[0,-1]] 
        height=0                    
        while q:
            for i in range(len(q)):
                row,col=q.popleft()
                isWater[row][col]=height
                for dr,dc in direction:
                    r,c=dr+row,dc+col
                    if min(r,c)<0 or r==ROW or c==COL or (r,c) in visit:
                        continue
                    q.append([r,c])
                    visit.add((r,c))
            height+=1
        return isWater                