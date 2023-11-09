class Solution:
    def countHomogenous(self, s: str) -> int:
        ans=0
        arr=[]
        for i in range(len(s)):
            if(len(arr)!=0 and arr[-1]==s[i]):
                arr+=[s[i]]
                #ans+=factorial(len(arr))
            else:
                n=len(arr)
                if n:
                    ans+=(n*(n+1))//2
                    #print(ans)
                arr=[s[i]]   
            #ans+=1
            #print(ans)
        if(len(arr)):
            n=len(arr)
            ans+=(n*(n+1))//2
           # print(ans)    
        return ans%(10**9+7)    
        