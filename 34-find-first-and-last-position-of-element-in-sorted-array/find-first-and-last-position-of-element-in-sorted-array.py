class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #if element is not present
        if target not in nums:
            return [-1,-1]
        
        #for left
        left=0
        right=len(nums)
        while left<right:
            mid=(left+right)//2
            if nums[mid]==target and mid==0:
                ans1=mid
                break
            elif nums[mid]==target and nums[mid-1]==target:
                right=mid
            elif nums[mid]==target and nums[mid-1]!=target:
                ans1=mid
                break
            else:
                if nums[mid]<target:
                    left=mid+1
                else:
                    right=mid
        #for right
        left=0
        right=len(nums)
        while left<right:
            mid=(left+right)//2
            if nums[mid]==target:
                if mid==len(nums)-1:
                    ans2=mid
                    break
                elif nums[mid+1]==target:
                    left=mid+1
                else:
                    ans2=mid
                    break
            else:
                if nums[mid]<target:
                    left=mid+1
                else:
                    right=mid
        return [ans1,ans2]            