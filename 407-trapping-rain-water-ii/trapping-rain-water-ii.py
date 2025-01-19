class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROW,COL=len(heightMap),len(heightMap[0])
        minheap=[]
        for r in range(ROW):
            for c in range(COL):
                if r in [0,ROW-1] or c in [0,COL-1]:
                    heappush(minheap,(heightMap[r][c],r,c))
                    heightMap[r][c]=-1
        res=0
        max_h=-1            
        while minheap:
            h,r,c=heappop(minheap)
            max_h=max(max_h,h)
            res+=max_h-h
            nei=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for dr,dc in nei:
                if (min(dr,dc)<0 or dr>=ROW or dc>=COL or heightMap[dr][dc]==-1):
                    continue
                heappush(minheap,(heightMap[dr][dc],dr,dc))
                heightMap[dr][dc]=-1
        return res        