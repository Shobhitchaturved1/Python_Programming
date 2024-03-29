class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi=max(nums)
        ans=0
        i=0
        j=0
        while i<len(nums) and j<len(nums):
            if nums[j]==maxi:
                k-=1
            j+=1
            while k==0:
                if nums[i]==maxi:
                    k+=1
                i+=1
            ans+=i                       
        return ans                            
                    