class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hash_map=defaultdict(int)
        for i in words:
            for j in i:
                hash_map[j]+=1
        for i in hash_map:
            if hash_map[i]%len(words)!=0:
                return False
        return True                
        