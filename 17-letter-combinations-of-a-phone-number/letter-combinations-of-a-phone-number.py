class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitmap={"2":"abc",
                  "3":"def",
                  "4":"ghi",
                  "5":"jkl",
                  "6":"mno",
                  "7":"pqrs",
                  "8":"tuv",
                  "9":"wxyz"}
        res=[]
        def dfs(start,comb):
            if len(comb)==len(digits):
                res.append(comb)
                return
            for i in digitmap[digits[start]]:
                dfs(start+1,comb + i)
        if digits:
            dfs(0,"")
        return res
            