class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f=0
        l=len(nums)
        while (f!=l):
            if nums[f]==0:
                nums.pop(f)
                nums.insert(0,0)
                f+=1
            elif nums[f]==2:
                nums.pop(f)
                nums.append(2)
                l-=1
            else:
                f+=1        