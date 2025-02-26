class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        #if we look only for positive number
        #but we need to look for negative value as well
        #answer would be either maximum sum or minimum sum
        def helper(arr):
            maxi=0
            curr=0
            for i in arr:
                curr+=i
                if curr<0:
                    curr=0
                maxi=max(maxi,curr)
            return maxi       
        arr2=[-i for i in nums]
        return max(helper(nums),helper(arr2))             