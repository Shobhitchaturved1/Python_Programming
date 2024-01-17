class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans=0
        for i in range(n+1):
            if i%5==0:
                j=i
                while j%5==0 and j>=5:
                    ans+=1
                    j=j//5
        return ans        