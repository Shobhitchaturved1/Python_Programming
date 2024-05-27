class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(start,comb,total):
            if total==target:
                res.append(comb.copy())
                return
            if total>target:
                return
            prev=-1    
            for j in range(start,len(candidates)):
                if candidates[j]==prev:
                    continue
                comb.append(candidates[j])
                backtrack(j+1,comb,total+candidates[j])
                comb.pop()
                prev=candidates[j]
        backtrack(0,[],0)
        return res               