class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=[i for i in range(1,len(nums)+1)]
        for i in nums:
            if i in ans:
                ans.remove(i)
            else:
                ans=[i]+ans
        return ans            