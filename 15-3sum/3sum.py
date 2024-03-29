class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            a=nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                threesome=a+nums[j]+nums[k]
                if threesome>0:
                    k-=1
                elif threesome<0:
                    j+=1
                else:
                    ans.append([a,nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1    
        return ans                    