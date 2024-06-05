class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length=len(board)
        board.reverse()
        def inttopos(num):
            r=(num-1)//length
            c=(num-1)%length
            if r%2:
                c=length-1-c
            return [r,c]    
        q=deque()
        visit=set()
        q.append([1,0]) #[square,move]
        while q:
            square,move=q.popleft()
            for i in range(1,7):
                nextsquare=square+i
                r,c=inttopos(nextsquare)
                if board[r][c]!=-1:
                    nextsquare=board[r][c]
                if nextsquare==length**2:
                    return move+1
                if nextsquare not in visit:
                    visit.add(nextsquare)
                    q.append([nextsquare,move+1])
        return -1                    