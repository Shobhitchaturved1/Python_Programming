class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans=""
        for i in s:
            ans+=(str(ord(i)-ord("a")+1))       
        while k:
            cur=0
            for i in ans:
                cur+=int(i)
            k-=1    
            ans=str(cur)   
        return int(ans)    