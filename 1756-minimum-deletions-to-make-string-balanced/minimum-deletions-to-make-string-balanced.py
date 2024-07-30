class Solution:
    def minimumDeletions(self, s: str) -> int:
        counta=0
        res=len(s)
        for i in s:
            if i=="a":
                counta+=1
        countb=0
        for i in s:
            if i=="a":
                counta-=1
            res=min(res,counta+countb)
            if i=="b":
                countb+=1
        return res                    