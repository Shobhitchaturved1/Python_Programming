class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        steps=0
        dir=0
        direction=[[0,1],[1,0],[0,-1],[-1,0]] #e,s,w,n
        res=[[rStart,cStart]]
        while len(res)<rows*cols:
            if(dir==0 or dir==2):
                steps+=1
            for i in range(steps):
                rStart+=direction[dir][0]
                cStart+=direction[dir][1]    
                if 0<=rStart<rows and 0<=cStart<cols:
                    res.append([rStart,cStart])
            dir=(dir+1)%4
        return res           