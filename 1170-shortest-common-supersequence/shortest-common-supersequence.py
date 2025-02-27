class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp=[[0]*(len(str2)+1) for _ in range(len(str1)+1)]
        for i in range(len(str1)-1,-1,-1):
            for j in range(len(str2)-1,-1,-1):
                if str1[i]==str2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:    
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        ans=""
        i,j=0,0
        while i<len(str1) and j<len(str2):
            if str1[i]==str2[j]:
                ans+=str1[i]
                i+=1
                j+=1
            elif dp[i+1][j]<dp[i][j+1]:
                ans+=str2[j]
                j+=1
            else:
                ans+=str1[i]
                i+=1
        while i<len(str1):
            ans+=str1[i]
            i+=1
        while j<len(str2):
            ans+=str2[j]
            j+=1               
        return ans    