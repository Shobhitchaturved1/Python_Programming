class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        ans=0
        res=0
        for r in range(k):
            if blocks[r]=="W":
                ans+=1
        r=k
        res=ans       
        while r<len(blocks):
            if blocks[l]=="W":
                ans-=1
            if blocks[r]=="W":
                ans+=1
            l+=1
            r+=1
            res=min(res,ans)
        return res                    