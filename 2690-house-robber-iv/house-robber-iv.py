class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left,right=min(nums),max(nums)
        def check(n):
            count=0
            i=0
            
            while i<len(nums):
                if nums[i]<=n:
                    count+=1
                    i+=1
                i+=1    
            return count>=k
        while left<=right:
            mid=(left+right)//2
            if check(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans            