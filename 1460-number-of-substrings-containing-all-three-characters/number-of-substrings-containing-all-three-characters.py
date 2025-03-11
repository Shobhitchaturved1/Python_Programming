class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans=0
        def check(map1):
            for i in map1:
                if map1[i]==0:
                    return False
            return True
        hashmap={"a":0,"b":0,"c":0}
        l=0
        for r in range(len(s)):
            hashmap[s[r]]+=1
            while check(hashmap):
                hashmap[s[l]]-=1
                ans+=len(s)-r
                l+=1
        return ans        
