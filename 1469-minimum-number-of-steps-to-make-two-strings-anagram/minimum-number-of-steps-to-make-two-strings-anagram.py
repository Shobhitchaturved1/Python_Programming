class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans=len(s)
        hash_map1=defaultdict(int)
        hash_map2=defaultdict(int)
        for i in range(len(s)):
            hash_map1[s[i]]+=1
            hash_map2[t[i]]+=1
        for i in hash_map1:
            if hash_map1[i]!=0 and hash_map2[i]!=0:
                ans-=min(hash_map1[i],hash_map2[i])
        return ans            