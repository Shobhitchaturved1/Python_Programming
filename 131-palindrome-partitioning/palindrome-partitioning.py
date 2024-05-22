class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrom(sub):
            return sub==sub[::-1]
        def backtrack(start,path):
            if start==len(s):
                result.append(path[:])
                return
            for end in range(start+1,len(s)+1):
                if ispalindrom(s[start:end]):
                    backtrack(end,path + [s[start:end]])
        result=[]
        backtrack(0,[])
        return result                
