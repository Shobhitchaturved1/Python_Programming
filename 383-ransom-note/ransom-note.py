class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map1=defaultdict(int)
        #hash_map2=defaultdict(int)
        for i in magazine:
            hash_map1[i]+=1
        for i in ransomNote:
            if(i not in hash_map1 or hash_map1[i]==0):
                return False
            hash_map1[i]-=1   
        return True         
        