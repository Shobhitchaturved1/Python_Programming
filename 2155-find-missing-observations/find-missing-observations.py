class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m_sum=sum(rolls)
        #mean=(m_sum+n_sum)/(m+n)
        n_sum=mean*(len(rolls)+n)-m_sum
        if n_sum>n*6 or n_sum<n:
            return []
        ans=[(n_sum//n)-1]*n
        n_sum-=n*((n_sum//n)-1)
        while n_sum:
            for i in range(len(ans)):
                ans[i]+=1
                n_sum-=1
                if n_sum==0:
                    break
        return ans            
