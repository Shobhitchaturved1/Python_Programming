class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=[]
        def backtrack(start,comb):
            res.append(comb.copy())
            for j in range(start,len(nums)):
                comb.append(nums[j])
                backtrack(j+1,comb)
                comb.pop()
        backtrack(0,[])
        ans=0
        for subset in res:
            subans=0
            for num in subset:
                subans^=num
            ans+=subans    
        return ans        