class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap=defaultdict(int)
        ans=0
        res=0
        left=0
        for i in range(len(s)):
            hashmap[s[i]]+=1
            if hashmap[s[i]]==1:
                ans+=1
            else:
                res=max(ans,res)
                ans+=1
                while hashmap[s[i]]!=1:
                    hashmap[s[left]]-=1
                    left+=1
                    ans-=1    
        return max(res,ans)            
