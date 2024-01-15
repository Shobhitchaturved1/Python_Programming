class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #case1
        map1=defaultdict(int)
        map2=defaultdict(int)
        if len(word1)!=len(word2):
            return False
        for i in range(len(word1)):
            map1[word1[i]]+=1
            map2[word2[i]]+=1
        if map1==map2:
            return True
        #case2
        count=0
        for i in word1:
            if map2[i]==0:
                count+=1
            if count==2:
                return False    
        return sorted(map1.values())==sorted(map2.values())        