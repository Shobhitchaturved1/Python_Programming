class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isprefixandsuffix(a,b):
            if len(a)>len(b):
                return False
            if b[0:len(a)]==a and b[len(b)-len(a):]==a:
                return True
            return False
        count=0    
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if isprefixandsuffix(words[i],words[j]):
                    count+=1
        return count            