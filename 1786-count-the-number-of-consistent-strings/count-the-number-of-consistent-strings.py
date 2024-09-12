class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashmap=defaultdict(int)
        for i in allowed:
            hashmap[i]=1
        count=0    
        for i in words:
            flag=False
            for s in i:
                if hashmap[s]!=1:
                    flag=True
            if flag==False:
                count+=1
        return count        
                