class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open=0
        ans=0
        for i in s:
            if i=="(":
                open+=1
            else:
                if open:
                    open-=1
                else:
                    ans+=1
        return ans+open                    