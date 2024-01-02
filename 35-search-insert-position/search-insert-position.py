class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        pos_out=0
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j-=1
                pos_out=mid
            else:
                i+=1
                pos_out=mid+1
        return pos_out           