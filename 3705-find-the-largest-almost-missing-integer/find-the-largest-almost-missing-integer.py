class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        for i in nums:
            count[i]+=1
        if len(nums)==k or k==1:
            ans=-1
            for i in nums:
                if count[i]<=k:
                    ans=max(ans,i)
            return ans
        if nums[0]>nums[-1]:
            if count[nums[0]]==1:
                return nums[0]
            elif count[nums[-1]]==1:
                return nums[-1]
        else:
            if count[nums[-1]]==1:
                return nums[-1] 
            elif count[nums[0]]==1:
                return nums[0]     
        return -1            