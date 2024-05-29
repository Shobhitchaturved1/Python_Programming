class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrom(sub):
            return sub==sub[::-1]
        res=[]    
        def backtrack(start,comb):
            if start==len(s):
                res.append(comb[:])
                return
            for j in range(start+1,len(s)+1):
                if palindrom(s[start:j]):
                    backtrack(j,comb+[s[start:j]])
        backtrack(0,[])
        return res            
