class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW,COL=len(image),len(image[0])
        visit=set()
        oldcolor=image[sr][sc]
        def dfs(r,c):
            if (0>r or r==ROW or c<0 or c==COL or image[r][c]!=oldcolor or (r,c) in visit):
                return
            visit.add((r,c))
            image[r][c]=color
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        dfs(sr,sc)
        return image            