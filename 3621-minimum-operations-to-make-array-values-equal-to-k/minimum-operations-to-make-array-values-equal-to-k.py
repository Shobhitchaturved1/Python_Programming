class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for i in nums:
            if i<k:
                return -1
        ans=0
        visit=set()
        visit.add(k)
        for i in nums:
            if i not in visit:
                ans+=1
                visit.add(i)
        return ans                