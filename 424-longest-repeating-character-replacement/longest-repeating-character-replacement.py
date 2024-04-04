class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charmap=defaultdict(int)
        i=0
        j=0
        maxfreq=0
        res=0
        ans=0
        while i<len(s) and j<len(s):
            charmap[s[j]]+=1
            maxfreq=max(maxfreq,charmap[s[j]])
            while (j-i+1-maxfreq>k):
                charmap[s[i]]-=1
                i+=1
            res=max(res,j-i+1)
            j+=1
        return res        
                    