class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last=defaultdict(int)
        for i,x in enumerate(s):
            last[x]=i
        ans=[]
        l=0
        maxi=last[s[0]]
        for r in range(len(s)):
            if maxi==r:
                ans.append(r-l+1)
                maxi=last[s[r+1]] if r+1<len(s) else 0
                l=r+1
            if maxi>r:
                maxi=max(maxi,last[s[r]])  
        return ans        