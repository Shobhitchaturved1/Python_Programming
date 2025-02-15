class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans=0
        def check(num,remsum):
            if remsum<0:
                return False
            if num=="" and remsum==0:
                return True
            x=False
            for i in range(len(num)):
                curr=num[0:i+1]
                val=int(curr)
                x=x or check(num[i+1:],remsum-val)
            return x        
        for i in range(1,n+1):
            if check(str(i*i),i):
                ans+=i*i
        return ans        