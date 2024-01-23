class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def search(nums,i,j):
            if i==j:
                return i
            mid=(i+j)//2
            if nums[mid]>nums[mid+1]:
                return search(nums,i,mid)
            return search(nums,mid+1,j)
        return search(nums,0,len(nums)-1)            