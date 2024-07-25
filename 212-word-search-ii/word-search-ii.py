class TrieNode:
    def __init__(self):
        self.children={}
        self.isend=False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        ROW,COL=len(board),len(board[0])
        res=set()
        visit=set()
        for w in words:
            cur=root
            for c in w:
                if c not in cur.children:
                    cur.children[c]=TrieNode()
                cur=cur.children[c]
            cur.isend=True  
        def dfs(r,c,cur,word):
            if (0>r or r>=ROW or 0>c or c>=COL or
                 board[r][c] not in cur.children or
                 (r,c)  in visit):
                 return
            visit.add((r,c)) 
            cur=cur.children[board[r][c]]
            word+=board[r][c]    
            if cur.isend==True:
                res.add(word)
            dfs(r+1,c,cur,word)
            dfs(r-1,c,cur,word)
            dfs(r,c+1,cur,word)
            dfs(r,c-1,cur,word)
            visit.remove((r,c))
        for r in range(ROW):
            for c in range(COL):
                dfs(r,c,root,"")    
        return list(res)                
