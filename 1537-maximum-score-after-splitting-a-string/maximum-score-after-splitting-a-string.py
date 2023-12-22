class Solution:
    def maxScore(self, s: str) -> int:
        count1=0
        count0=0
        ans=0
        for i in s:
            if i=='1':
                count1+=1
        if count1==len(s) or count1==0:
            return len(s)-1  
        ans=count1-1         
        for i in range(len(s)):
            if s[i]=='0' and i!=len(s)-1:
                count0+=1
                ans=max(ans,count0+count1)
            else:
                count1-=1
        return ans                   
        