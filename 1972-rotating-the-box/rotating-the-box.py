class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROW,COL=len(box),len(box[0])
        for r in range(ROW):
            i=COL-1
            for c in reversed(range(COL)):
                if box[r][c]=="#":
                    box[r][c],box[r][i]=box[r][i],box[r][c]
                    i-=1
                elif box[r][c]=="*":
                    i=c-1
        res=[]
        for c in range(COL):
            col=[]
            for r in reversed(range(ROW)):
                col.append(box[r][c])
            res.append(col)
        return res        
