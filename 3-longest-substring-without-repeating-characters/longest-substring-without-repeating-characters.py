class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        i=0
        j=1
        if(len(s)<=1):
            return len(s)
        hash_map=defaultdict(int)
        hash_map[s[i]]=1
        while(j<len(s) and i<len(s)):
            hash_map[s[j]]+=1
            if hash_map[s[j]]>1:
                ans=max(ans,j-i)
                while(hash_map[s[j]]>1):
                    hash_map[s[i]]-=1
                    i+=1
            j+=1
        return max(ans,j-i)           


        