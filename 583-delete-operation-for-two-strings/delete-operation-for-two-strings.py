class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        text1,text2=word1,word2
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return len(text1)+len(text2)-2*dp[0][0] 