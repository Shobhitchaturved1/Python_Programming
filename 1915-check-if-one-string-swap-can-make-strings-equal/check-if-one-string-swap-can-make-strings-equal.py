class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        map1,map2=defaultdict(int),defaultdict(int)
        if len(s1)!=len(s2):return False
        count=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
            if count>2:return False    
            map1[s1[i]]+=1
            map2[s2[i]]+=1
        return map1==map2    