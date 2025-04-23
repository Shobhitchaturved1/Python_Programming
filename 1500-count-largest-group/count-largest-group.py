class Solution:
    def countLargestGroup(self, n: int) -> int:
        ans=[0]*(n+1)
        def digitsum(a):
            count=0
            for i in str(a):
                count+=int(i)
            return count
        for i in range(1,n+1):
            ans[digitsum(i)]+=1
        maxi=max(ans)
        res=0
        for i in ans:
            if i==maxi:
                res+=1
        return res           